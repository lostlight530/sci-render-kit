#!/usr/bin/env python3
"""sci-render-kit 测试套件"""

import sys, os, tempfile, json
try:
    import yaml
except ImportError:
    print("⚠️ 需要安装 PyYAML: pip install pyyaml")
    sys.exit(1)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_manifest_schema_exists():
    assert os.path.exists('metadata/reproducibility.schema.yaml'), "manifest schema 必须存在"
    assert os.path.exists('metadata/recipe.schema.yaml'), "recipe schema 必须存在"
    print("  [OK] Schema 文件存在")

def test_profiles_exist():
    profiles = ['nature', 'science', 'ieee', 'presentation']
    for p in profiles:
        path = f'profiles/{p}.yaml'
        assert os.path.exists(path), f"profile {p} 必须存在"
    print("  [OK] 所有 profile 存在")

def test_recipes_exist():
    recipes = ['line-chart', 'bar-chart', 'scatter-plot', 'heatmap', 'boxplot', 'histogram',
               'semantic-line-chart', 'line-chart-interactive']
    for r in recipes:
        path = f'recipes/{r}.yaml'
        assert os.path.exists(path), f"recipe {r} 必须存在"
    print("  [OK] 所有 recipe 存在")

def test_recipe_schema_compliance():
    with open('metadata/recipe.schema.yaml', 'r') as f:
        schema = yaml.safe_load(f)
    
    required = schema.get('required', [])
    for recipe_name in ['line-chart', 'bar-chart']:
        with open(f'recipes/{recipe_name}.yaml', 'r') as f:
            recipe = yaml.safe_load(f)
        for key in required:
            assert key in recipe, f"recipe {recipe_name} 缺少 {key}"
    print("  [OK] Recipe Schema 合规")

def test_backends_exist():
    backends = ['matplotlib_adapter.py', 'ggplot2_adapter.R', 'observable_adapter.js']
    for b in backends:
        path = f'backends/{b}'
        assert os.path.exists(path), f"backend {b} 必须存在"
    print("  [OK] 所有后端适配器存在")


def test_central_cli_validation():
    import subprocess
    # Test valid (using presentation profile to avoid nature's PDF vector requirement vs PNG recipe config)
    res = subprocess.run(["python3", "sci_render.py", "recipes/line-chart.yaml", "--profile", "presentation", "--backend", "matplotlib"], capture_output=True, text=True)
    assert "P0 Schema 验证通过" in res.stdout, f"合法配方应该通过 Schema 验证, stdout: {res.stdout}"
    assert "P1 美学规范检查通过" in res.stdout, f"合法配方应该通过 P1 验证, stdout: {res.stdout}"
    assert "✅ P2/P3 输出检查通过" in res.stdout, f"合法配方应该通过输出检查, stdout: {res.stdout}"
    
    # Test invalid schema -> P0_SCHEMA_FAILURE
    res2 = subprocess.run(["python3", "sci_render.py", "profiles/nature.yaml", "--backend", "matplotlib"], capture_output=True, text=True)
    assert res2.returncode != 0, "不合法的配方文件应该被拦截并返回非零"
    assert "P0_SCHEMA_FAILURE" in res2.stdout, "不合法的配方应触发 P0_SCHEMA_FAILURE"

    # Test missing profile -> MISSING_PROFILE
    res3 = subprocess.run(["python3", "sci_render.py", "recipes/line-chart.yaml", "--profile", "unknown_profile"], capture_output=True, text=True)
    assert res3.returncode != 0, "缺失的 profile 应该被拦截并返回非零"
    assert "MISSING_PROFILE" in res3.stdout, "缺失的 profile 应触发 MISSING_PROFILE"

    # Test invalid YAML parse -> YAML_PARSE_FAILURE
    with open("recipes/bad.yaml", "w") as bad_f:
        bad_f.write("invalid: yaml: \n  [ - foo")
    res4 = subprocess.run(["python3", "sci_render.py", "recipes/bad.yaml"], capture_output=True, text=True)
    assert res4.returncode != 0, "损坏的 YAML 应该被拦截并返回非零"
    assert "YAML_PARSE_FAILURE" in res4.stdout, "损坏的 YAML 应触发 YAML_PARSE_FAILURE"
    import os
    os.remove("recipes/bad.yaml")

def test_manifest_output():
    # 检查是否生成 manifest 示例
    assert os.path.exists('metadata/reproducibility.schema.yaml')
    with open('metadata/reproducibility.schema.yaml', 'r') as f:
        schema = yaml.safe_load(f)
    assert 'required' in schema
    assert 'generated_at' in schema['required']
    print("  [OK] Manifest Schema 定义正确")

def test_quality_gates():
    assert os.path.exists('quality/gates.yaml')
    with open('quality/gates.yaml', 'r') as f:
        gates = yaml.safe_load(f)
    assert 'gates' in gates
    assert len(gates['gates']) >= 3
    print("  [OK] 质量门定义存在且完整")

def test_recipe_palette_constraint():
    with open('recipes/line-chart.yaml', 'r') as f:
        recipe = yaml.safe_load(f)
    palette = recipe['aesthetics'].get('palette', [])
    assert len(palette) <= 8, "色板颜色数不应超过 8"
    print("  [OK] 色板约束满足")

def test_color_encoding_module():
    from core.color_encoding import CognitiveColorEncoder
    enc = CognitiveColorEncoder()
    # WCAG 对比度：黑 vs 白 = 21:1
    assert abs(enc.contrast_ratio((0, 0, 0), (255, 255, 255)) - 21.0) < 0.01
    # 语义标签命中
    assert enc.encode('positive').hex_code == '#009E73'
    assert enc.encode('negative').hex_code == '#D55E00'
    # 混合系列：命中语义标签用语义色，否则按索引取感知色板
    pal = enc.resolve_series_palette(['positive', 'foo', 'negative'])
    assert pal == ['#009E73', '#E69F00', '#D55E00']
    print("  [OK] 色彩编码模块功能正确")

def test_palette_contrast_gate():
    from sci_render import run_quality_gates, load_yaml
    gates = load_yaml('quality/gates.yaml')
    # 声明 background 后，低对比度配色必须被拦截
    bad = {'type': 'line-chart', 'data': {'a': [1, 2]},
           'aesthetics': {'palette': ['#FFFFFF'], 'background': '#FFFFFF'}, 'output': {}}
    errors = run_quality_gates(bad, {}, gates)
    assert any('对比度' in e for e in errors), "白底白色板应触发 palette-contrast"
    # 高对比度配色应通过
    good = {'type': 'line-chart', 'data': {'a': [1, 2]},
            'aesthetics': {'palette': ['#0072B2'], 'background': '#FFFFFF'}, 'output': {}}
    assert not any('对比度' in e for e in run_quality_gates(good, {}, gates))
    # 未声明 background/semantic_palette 时不启用该检查（向后兼容）
    legacy = {'type': 'line-chart', 'data': {'a': [1, 2]},
              'aesthetics': {'palette': ['#F0E442']}, 'output': {}}
    assert not any('对比度' in e for e in run_quality_gates(legacy, {}, gates))
    print("  [OK] palette-contrast 质量门工作正常")

def test_semantic_palette_resolution():
    from sci_render import resolve_effective_palette
    recipe = {'type': 'line-chart', 'data': {'positive': [1], 'custom': [2]}}
    pal = resolve_effective_palette(recipe, {'semantic_palette': True})
    assert pal == ['#009E73', '#E69F00'], f"语义色板解析错误: {pal}"
    # 未启用时回退到显式 palette
    pal2 = resolve_effective_palette(recipe, {'palette': ['#123456']})
    assert pal2 == ['#123456']
    print("  [OK] 语义色板解析正确")

def test_semantic_palette_matplotlib_adapter():
    from backends.matplotlib_adapter import generate_python_code
    recipe = {'id': 't', 'type': 'line-chart',
              'data': {'positive': [1, 2], 'stable': [3, 4]},
              'aesthetics': {'semantic_palette': True},
              'output': {'dir': 'output', 'filename': 't.png'}}
    code = generate_python_code(recipe, {})
    assert '#009E73' in code and '#0072B2' in code, "生成的代码应包含语义色"
    print("  [OK] Matplotlib 适配器语义色板生成正确")

def test_semantic_recipe_e2e():
    import subprocess
    # 合法语义配方：端到端通过所有质量门
    res = subprocess.run(["python3", "sci_render.py", "recipes/semantic-line-chart.yaml",
                          "--profile", "presentation", "--backend", "matplotlib"],
                         capture_output=True, text=True)
    assert res.returncode == 0, f"语义配方应渲染成功, stdout: {res.stdout}\nstderr: {res.stderr}"
    assert "P1 美学规范检查通过" in res.stdout
    assert "✅ P2/P3 输出检查通过" in res.stdout
    assert os.path.exists('output/semantic-line-chart.png')
    assert os.path.exists('output/semantic-line-chart.manifest.json')
    # 非法配方：声明 background 后白底白色板必须被 CLI 拦截
    with open("recipes/_bad_contrast.yaml", "w") as f:
        f.write('id: bad-contrast\ntype: line-chart\ndata:\n  a: [1, 2]\n'
                'aesthetics:\n  palette: ["#FFFFFF"]\n  background: "#FFFFFF"\n'
                'output:\n  dir: output\n  filename: bad.png\n  format: png\n')
    res2 = subprocess.run(["python3", "sci_render.py", "recipes/_bad_contrast.yaml",
                           "--profile", "presentation", "--backend", "matplotlib"],
                          capture_output=True, text=True)
    os.remove("recipes/_bad_contrast.yaml")
    assert res2.returncode != 0, "低对比度配方应被质量门拦截"
    assert '对比度' in res2.stdout, "应报告 palette-contrast 违规"
    print("  [OK] 语义配方端到端渲染与门禁拦截正常")

def test_backend_capability_gate():
    import subprocess
    # observable 后端只支持 html；png 配方必须在 dispatch 前被拦截
    res = subprocess.run(["python3", "sci_render.py", "recipes/line-chart.yaml",
                          "--profile", "presentation", "--backend", "observable"],
                         capture_output=True, text=True)
    assert res.returncode != 0, "格式超出后端能力集应被拦截"
    assert "BACKEND_CAPABILITY_MISMATCH" in res.stdout, f"应触发 BACKEND_CAPABILITY_MISMATCH, stdout: {res.stdout}"
    print("  [OK] 后端能力门禁工作正常")


def test_observable_html_e2e():
    import shutil, subprocess
    # 无 node 或缺少 yaml 依赖时跳过而非失败
    if not shutil.which("node"):
        print("  [SKIP] 无 node 环境，跳过 observable E2E")
        return
    probe = subprocess.run(["node", "-e", "require('yaml')"], capture_output=True)
    if probe.returncode != 0:
        print("  [SKIP] 缺少 npm yaml 依赖（npm install），跳过 observable E2E")
        return
    res = subprocess.run(["python3", "sci_render.py", "recipes/line-chart-interactive.yaml",
                          "--profile", "presentation", "--backend", "observable"],
                         capture_output=True, text=True)
    assert res.returncode == 0, f"交互式配方应渲染成功, stdout: {res.stdout}\nstderr: {res.stderr}"
    assert os.path.exists('output/line-chart.html')
    assert os.path.exists('output/line-chart.manifest.json')
    with open('output/line-chart.html') as f:
        assert f.read(15).lstrip().lower().startswith('<!doctype'), "输出必须是 HTML 文档"
    print("  [OK] observable HTML 端到端渲染正常")


def test_p3_dpi_size_checks():
    import subprocess
    # dpi 低于期刊最低要求 + 图宽超过版宽上限，必须被 P3 拦截
    with open("recipes/_p3_violation.yaml", "w") as f:
        f.write('id: p3-violation\ntype: line-chart\ndata:\n  a: [1, 2]\n'
                'aesthetics:\n  dpi: 300\n  figsize: [8.0, 4.0]\n'
                'output:\n  dir: output\n  filename: p3v.png\n  format: png\n')
    res = subprocess.run(["python3", "sci_render.py", "recipes/_p3_violation.yaml",
                          "--profile", "science", "--backend", "matplotlib"],
                         capture_output=True, text=True)
    os.remove("recipes/_p3_violation.yaml")
    assert res.returncode != 0, "违反 P3 期刊规范的配方应被拦截"
    assert "DPI 300 低于 science 最低要求 600" in res.stdout, f"应触发 dpi-check, stdout: {res.stdout}"
    assert "超过 science 版宽上限" in res.stdout, f"应触发 size-check, stdout: {res.stdout}"
    print("  [OK] P3 dpi-check / size-check 工作正常")


def test_adapter_semantic_parity():
    """R/JS 适配器内嵌的语义色常量必须与 core/color_encoding.py 完全一致（静态一致性）"""
    import re
    from core.color_encoding import CognitiveColorEncoder
    expected = {k: f"#{v[0]:02X}{v[1]:02X}{v[2]:02X}" for k, v in CognitiveColorEncoder.SEMANTIC_MAP.items()}
    for path, pattern in [
        ('backends/ggplot2_adapter.R', r"(\w+)='(#[0-9A-Fa-f]{6})'"),
        ('backends/observable_adapter.js', r"(\w+): '(#[0-9A-Fa-f]{6})'"),
    ]:
        with open(path) as f:
            found = dict(re.findall(pattern, f.read()))
        for tag, hex_code in expected.items():
            assert found.get(tag, '').upper() == hex_code.upper(), \
                f"{path} 中语义标签 {tag} 应为 {hex_code}，实际 {found.get(tag)}"
    # 感知色板（fallback）的 hex 序列与顺序也必须一致
    perceptual_expected = [f"#{v[0]:02X}{v[1]:02X}{v[2]:02X}".upper()
                           for v in CognitiveColorEncoder.PERCEPTUAL_PALETTE]
    for path in ['backends/ggplot2_adapter.R', 'backends/observable_adapter.js']:
        with open(path) as f:
            text = f.read()
        idx = text.lower().index('perceptual')
        hexes = [h.upper() for h in re.findall(r"#[0-9A-Fa-f]{6}", text[idx:])[:8]]
        assert hexes == perceptual_expected, f"{path} 感知色板序列与 core 不一致: {hexes}"
    print("  [OK] R/JS 适配器语义色常量与 core 一致")


def test_nature_profile_constraints():
    with open('profiles/nature.yaml', 'r') as f:
        profile = yaml.safe_load(f)
    assert 'constraints' in profile['aesthetics']
    constraints = profile['aesthetics']['constraints']
    assert any('字号' in c for c in constraints), "Nature profile 应包含字号约束"
    assert any('矢量' in c for c in constraints), "Nature profile 应包含矢量格式约束"
    print("  [OK] Nature Profile 约束完整")

if __name__ == '__main__':
    tests = [v for k, v in globals().items() if k.startswith('test_')]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as e:
            print(f"  [FAIL] {t.__name__}: {e}")
            failed += 1
    print(f"\n  {passed}/{passed + failed} passed")
    sys.exit(0 if failed == 0 else 1)

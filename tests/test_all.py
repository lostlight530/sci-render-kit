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
    recipes = ['line-chart', 'bar-chart', 'scatter-plot', 'heatmap', 'boxplot', 'histogram']
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

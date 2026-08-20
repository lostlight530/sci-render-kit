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
    profiles = ['nature', 'science', 'cell', 'ieee', 'presentation']
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


def test_cvd_simulation_module():
    from core.cvd_simulation import simulate_cvd, cvd_contrast_report, CVD_TYPES
    from core.color_encoding import CognitiveColorEncoder
    # 消色差刺激（灰）在三种模拟下近似不变
    for t in CVD_TYPES:
        r, g, b = simulate_cvd((128, 128, 128), t)
        assert abs(r - 128) <= 1 and abs(g - 128) <= 1 and abs(b - 128) <= 1
    # Machado 2009 protanopia：纯红显著变暗（L 锥缺失）
    r, g, b = simulate_cvd((255, 0, 0), 'protanopia')
    assert r < 100 and g < 100 and b < 60, f"protanopia 模拟异常: {(r, g, b)}"
    # 输出裁剪在 [0, 255]
    assert all(0 <= c <= 255 for c in simulate_cvd((255, 255, 255), 'tritanopia'))
    # 对比度报告按最坏情况排序
    enc = CognitiveColorEncoder()
    rep = cvd_contrast_report((204, 121, 167), (255, 255, 255), enc.contrast_ratio)
    assert len(rep) == 3 and rep[0][1] <= rep[-1][1]
    # 未知类型报错
    try:
        simulate_cvd((0, 0, 0), 'achromatopsia')
        assert False, "未知 CVD 类型应抛 ValueError"
    except ValueError:
        pass
    print("  [OK] CVD 模拟模块（Machado 2009）工作正常")


def test_cvd_contrast_gate():
    from sci_render import run_quality_gates, load_yaml
    gates = load_yaml('quality/gates.yaml')
    # #CC79A7 白底：正常对比度 3.06 通过 palette-contrast，但 tritanopia 模拟下 < 3.0 必须被拦截
    rec = {'type': 'line-chart', 'data': {'a': [1, 2]},
           'aesthetics': {'palette': ['#CC79A7'], 'background': '#FFFFFF'}, 'output': {}}
    errors = run_quality_gates(rec, {}, gates)
    assert any('tritanopia' in e and '模拟' in e for e in errors), f"应触发 cvd-contrast: {errors}"
    # 语义色板在三种模拟下均 ≥ 3.0（positive 最坏 ≈3.13），不应误报
    good = {'type': 'line-chart', 'data': {'positive': [1], 'stable': [2]},
            'aesthetics': {'semantic_palette': True, 'background': '#FFFFFF'}, 'output': {}}
    assert not any('模拟' in e for e in run_quality_gates(good, {}, gates))
    # 未声明 background/semantic_palette 时不启用（向后兼容）
    legacy = {'type': 'line-chart', 'data': {'a': [1, 2]},
              'aesthetics': {'palette': ['#CC79A7']}, 'output': {}}
    assert not any('模拟' in e for e in run_quality_gates(legacy, {}, gates))
    print("  [OK] cvd-contrast 质量门（Machado 2009 模拟）工作正常")


def test_text_contrast_and_adjacency_gates():
    from sci_render import run_quality_gates, load_yaml
    gates = load_yaml('quality/gates.yaml')
    base = {'type': 'line-chart', 'data': {'a': [1, 2], 'b': [2, 3]}, 'output': {}}
    # SC 1.4.3：#777777 白底 ≈ 4.48 < 4.5 拦截；#595959 ≈ 7.0 通过
    bad = {**base, 'aesthetics': {'text_color': '#777777', 'background': '#FFFFFF'}}
    assert any('SC 1.4.3' in e for e in run_quality_gates(bad, {}, gates))
    good = {**base, 'aesthetics': {'text_color': '#595959', 'background': '#FFFFFF'}}
    assert not any('SC 1.4.3' in e for e in run_quality_gates(good, {}, gates))
    # 未声明 text_color 不启用
    assert not any('SC 1.4.3' in e for e in run_quality_gates({**base, 'aesthetics': {}}, {}, gates))
    # SC 1.4.11：声明 adjacency_check 后两两 ≥ 3.0；#0072B2 vs #D55E00 ≈ 1.34 拦截并报告色对
    adj_bad = {**base, 'aesthetics': {'palette': ['#0072B2', '#D55E00'], 'adjacency_check': True}}
    errs = run_quality_gates(adj_bad, {}, gates)
    assert any('SC 1.4.11' in e and '#0072B2' in e and '#D55E00' in e for e in errs), errs
    adj_good = {**base, 'aesthetics': {'palette': ['#000000', '#0072B2'], 'adjacency_check': True}}
    assert not any('SC 1.4.11' in e for e in run_quality_gates(adj_good, {}, gates))
    # 未声明 adjacency_check 不启用（向后兼容）
    adj_off = {**base, 'aesthetics': {'palette': ['#0072B2', '#D55E00']}}
    assert not any('SC 1.4.11' in e for e in run_quality_gates(adj_off, {}, gates))
    print("  [OK] text-contrast (4.5:1, SC 1.4.3) 与 palette-adjacency (SC 1.4.11) 门禁工作正常")


def test_named_palette_registry():
    from core.palettes import PALETTE_REGISTRY, describe_palette, resolve_categorical
    # petroff10：10 色、互异、合法 hex
    colors = resolve_categorical('petroff10')
    assert len(colors) == 10 and len(set(colors)) == 10
    assert all(c.startswith('#') and len(c) == 7 for c in colors)
    # 与 matplotlib 3.10 官方 color_sequences 一致（环境有 matplotlib 时验证）
    try:
        from matplotlib import color_sequences
        official = ['#%02X%02X%02X' % tuple(round(v * 255) for v in rgb)
                    for rgb in color_sequences['petroff10']]
        assert colors == official, f"petroff10 与 matplotlib 官方值不一致: {colors} vs {official}"
    except ImportError:
        pass
    # 元数据完整性：kind / cvd_safety / source / availability
    for name, entry in PALETTE_REGISTRY.items():
        assert entry['kind'] in ('categorical', 'sequential', 'diverging')
        assert entry['cvd_safety'] in ('high', 'medium', 'unverified')
        assert entry.get('source') and entry.get('availability'), f"{name} 元数据不完整"
    # 能力诚实：mako / Crameri 发散系非 matplotlib 内置，不得伪装为可用
    for name in ('mako', 'berlin', 'managua', 'vanimo'):
        assert PALETTE_REGISTRY[name]['mpl_name'] is None
        assert '不可用' in PALETTE_REGISTRY[name]['availability']['matplotlib']
    # 非 categorical 色板按分类解析必须报错
    try:
        resolve_categorical('viridis')
        assert False, "sequential 色阶不应解析为分类色板"
    except ValueError:
        pass
    # 未知名称报错并列出可用项
    try:
        describe_palette('jet')
        assert False
    except ValueError as e:
        assert 'petroff10' in str(e)
    print("  [OK] 命名色板注册表（petroff10 / viridis / cividis / Crameri 系）工作正常")


def test_named_palette_gate():
    from sci_render import run_quality_gates, resolve_effective_palette, load_yaml
    gates = load_yaml('quality/gates.yaml')
    # 合法注册色板：按系列数截取前三色
    rec = {'type': 'line-chart', 'data': {'a': [1], 'b': [2], 'c': [3]},
           'aesthetics': {'palette_name': 'petroff10'}, 'output': {}}
    pal = resolve_effective_palette(rec, rec['aesthetics'])
    assert pal == ['#3F90DA', '#FFA90E', '#BD1F01'], pal
    assert not run_quality_gates(rec, {}, gates)
    # matplotlib 适配器同样支持 palette_name
    from backends.matplotlib_adapter import generate_python_code
    rec2 = {'id': 't2', 'type': 'line-chart', 'data': {'a': [1, 2]},
            'aesthetics': {'palette_name': 'petroff10'},
            'output': {'dir': 'output', 'filename': 't2.png'}}
    assert '#3F90DA' in generate_python_code(rec2, {})
    # 未注册名 → P1 拦截并列出可用项
    bad = {'type': 'line-chart', 'data': {'a': [1]},
           'aesthetics': {'palette_name': 'jet'}, 'output': {}}
    assert any('未知色板' in e for e in run_quality_gates(bad, {}, gates))
    # 系列图误用 sequential 色阶 → 拦截并提示改用 cmap
    wrong_kind = {'type': 'bar-chart', 'data': {'a': 1},
                  'aesthetics': {'palette_name': 'viridis'}, 'output': {}}
    assert any('cmap' in e for e in run_quality_gates(wrong_kind, {}, gates))
    print("  [OK] palette-name 门禁与注册色板解析工作正常")


def test_provenance_sidecar_and_embedding():
    import subprocess, hashlib
    res = subprocess.run(["python3", "sci_render.py", "recipes/semantic-line-chart.yaml",
                          "--profile", "presentation", "--backend", "matplotlib"],
                         capture_output=True, text=True)
    assert res.returncode == 0, f"渲染应成功: {res.stdout}\n{res.stderr}"
    # FAIR R1.2 溯源旁车
    sidecar = 'output/semantic-line-chart.prov.json'
    assert os.path.exists(sidecar), "必须生成 .prov.json 溯源旁车"
    with open(sidecar) as f:
        prov = json.load(f)
    assert prov['schema'] == 'sci-render-kit/provenance@1'
    assert prov['backend'] == 'matplotlib' and prov['backend_version']
    recipe_bytes = open('recipes/semantic-line-chart.yaml', 'rb').read()
    assert prov['recipe_sha256'] == 'sha256:' + hashlib.sha256(recipe_bytes).hexdigest()
    with open('recipes/semantic-line-chart.yaml') as f:
        loaded = yaml.safe_load(f)
    data_json = json.dumps(loaded['data'], sort_keys=True, ensure_ascii=False)
    assert prov['input_data_sha256'] == 'sha256:' + hashlib.sha256(data_json.encode('utf-8')).hexdigest()
    out_bytes = open('output/semantic-line-chart.png', 'rb').read()
    assert prov['output_sha256'] == 'sha256:' + hashlib.sha256(out_bytes).hexdigest()
    # 内嵌 metadata：PNG 文本块可由 PIL 读回且与旁车一致
    from PIL import Image
    info = Image.open('output/semantic-line-chart.png').info
    assert 'srk:provenance' in info, "PNG 必须内嵌 srk:provenance 文本块"
    embedded = json.loads(info['srk:provenance'])
    assert embedded['recipe_sha256'] == prov['recipe_sha256']
    assert embedded['input_data_sha256'] == prov['input_data_sha256']
    assert embedded['backend_version'] == prov['backend_version']
    print("  [OK] 图件溯源内嵌 + .prov.json 旁车（FAIR R1.2）工作正常")


def test_profiles_refreshed():
    import re
    for name in ['nature', 'science', 'cell', 'ieee', 'presentation']:
        with open(f'profiles/{name}.yaml') as f:
            prof = yaml.safe_load(f)
        assert 'verified_date' in prof, f"{name} 缺 verified_date"
        assert 'source_url' in prof, f"{name} 缺 source_url"
        assert re.match(r'^\d{4}-\d{2}-\d{2}$', prof['verified_date']), f"{name} verified_date 格式错误"
    with open('profiles/cell.yaml') as f:
        cell = yaml.safe_load(f)
    assert cell['aesthetics']['font'] == 'Arial', "Cell 仅允许 Arial 字体"
    assert cell['aesthetics']['dpi'] == 1000, "Cell 线图分辨率应 ≥ 1000 DPI"
    assert abs(cell['aesthetics']['max_width_in'] - 174 / 25.4) < 0.01
    with open('profiles/ieee.yaml') as f:
        ieee = yaml.safe_load(f)
    assert ieee['aesthetics'].get('max_height_in') == 8.8, "IEEE 版面高度上限 8.8in"
    assert ieee['aesthetics'].get('font_whitelist'), "IEEE 应声明字体白名单"
    with open('profiles/nature.yaml') as f:
        nature = yaml.safe_load(f)
    assert any('面板标签' in c for c in nature['aesthetics']['constraints']), "Nature 应含面板标签约束"
    print("  [OK] 期刊 profile 刷新（source_url/verified_date、Cell、IEEE 上限）完整")

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

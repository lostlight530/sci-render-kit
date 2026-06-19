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
    # Test valid
    res = subprocess.run(["python3", "sci_render.py", "recipes/line-chart.yaml", "--backend", "matplotlib"], capture_output=True, text=True)
    assert "P0 Schema 验证通过" in res.stdout, "合法配方应该通过 Schema 验证"
    assert "P1 美学规范检查通过" in res.stdout, "合法配方应该通过 P1 验证"
    
    # Test invalid schema
    res2 = subprocess.run(["python3", "sci_render.py", "profiles/nature.yaml", "--backend", "matplotlib"], capture_output=True, text=True)
    assert res2.returncode != 0, "不合法的配方文件应该被拦截并返回非零"

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

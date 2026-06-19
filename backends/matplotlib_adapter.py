#!/usr/bin/env python3
"""
Matplotlib 后端适配器 — 将 YAML 配方渲染为图表
零外部依赖声明：仅依赖 matplotlib 和 numpy（学术环境标配）
"""

import yaml
import json
import sys
import os
from pathlib import Path
from datetime import datetime
from string import Template

def load_recipe(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_profile(name: str) -> dict:
    profile_path = Path('profiles') / f'{name}.yaml'
    if not profile_path.exists():
        return {}
    with open(profile_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def validate_recipe(recipe: dict) -> list[str]:
    """静态验证：配方合规检查"""
    errors = []
    required = ['type', 'data', 'aesthetics']
    for key in required:
        if key not in recipe:
            errors.append(f'缺少必需字段: {key}')
    if 'output' not in recipe:
        errors.append('缺少 output 配置')
    return errors

def generate_python_code(recipe: dict, profile: dict) -> str:
    """将配方 + 配置转换为 Python 代码"""
    code_template = '''#!/usr/bin/env python3
"""自动生成 — 由 sci-render-kit 从配方渲染"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# 配置
plt.rcParams.update(${rc_params})

# 数据
data = ${data}

# 创建图表
fig, ax = plt.subplots(figsize=${figsize})

${render_logic}

# 保存
Path('${output_dir}').mkdir(parents=True, exist_ok=True)
fig.savefig('${output_path}', dpi=${dpi}, format='${format}', 
            bbox_inches='tight', pad_inches=0.05)
plt.close(fig)
print(f"已保存: ${output_path}")
'''
    
    # 合并配置
    aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}
    rc_params = {
        'font.family': aesthetics.get('font', 'sans-serif'),
        'font.size': aesthetics.get('font_size', 10),
        'axes.linewidth': aesthetics.get('axes_linewidth', 0.8),
        'lines.linewidth': aesthetics.get('line_width', 1.2),
        'savefig.dpi': max(aesthetics.get('dpi', 300), 300),
    }
    
    figsize = aesthetics.get('figsize', [6.0, 4.0])
    
    # 根据图表类型生成渲染逻辑
    chart_type = recipe['type']
    render_logic = generate_render_logic(chart_type, recipe['data'], aesthetics)
    
    output = recipe['output']
    output_path = Path(output.get('dir', 'output')) / output.get('filename', 'figure.png')
    
    t = Template(code_template)
    return t.substitute(
        rc_params=json.dumps(rc_params),
        data=json.dumps(recipe['data']),
        figsize=figsize,
        render_logic=render_logic,
        output_dir=str(output_path.parent),
        output_path=str(output_path),
        dpi=rc_params['savefig.dpi'],
        format=output.get('format', 'png').lower()
    )

def generate_render_logic(chart_type: str, data: dict, aesthetics: dict) -> str:
    """根据图表类型生成 matplotlib 渲染逻辑"""
    palette = aesthetics.get('palette', ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000'])
    
    if chart_type == 'line-chart':
        lines = []
        for i, (label, values) in enumerate(data.items()):
            color = palette[i % len(palette)]
            lines.append(f'x = np.arange(len({json.dumps(values)}))')
            lines.append(f'ax.plot(x, {json.dumps(values)}, color="{color}", linewidth=1.0, label="{label}", marker="o", markersize=2.5)')
        lines.append('ax.legend(frameon=False)')
        return '\n'.join(lines)
    
    elif chart_type == 'bar-chart':
        lines = []
        categories = list(data.keys())
        values = list(data.values())
        n = len(categories)
        bar_width = 0.6
        x = np.arange(n)
        for i, (label, val) in enumerate(zip(categories, values)):
            color = palette[i % len(palette)]
            lines.append(f'ax.bar(x[{i}] + {bar_width/2}, {val}, width={bar_width}, color="{color}", edgecolor="black", linewidth=0.5)')
        lines.append(f'ax.set_xticks(x + {bar_width/2})')
        lines.append(f'ax.set_xticklabels({json.dumps(categories)})')
        return '\n'.join(lines)
    
    elif chart_type == 'scatter-plot':
        lines = []
        for i, (label, (x, y)) in enumerate(data.items()):
            color = palette[i % len(palette)]
            lines.append(f'ax.scatter({json.dumps(x)}, {json.dumps(y)}, c="{color}", s=16, label="{label}", edgecolors="black", linewidths=0.3)')
        lines.append('ax.legend(frameon=False)')
        return '\n'.join(lines)

    elif chart_type == 'heatmap':
        lines = []
        matrix = data.get('matrix', [])
        row_labels = data.get('row_labels', [])
        col_labels = data.get('col_labels', [])
        cmap = aesthetics.get('cmap', 'viridis')
        lines.append(f'cax = ax.imshow({json.dumps(matrix)}, cmap="{cmap}")')
        lines.append(f'fig.colorbar(cax)')
        if col_labels:
            lines.append(f'ax.set_xticks(np.arange(len({json.dumps(col_labels)})))')
            lines.append(f'ax.set_xticklabels({json.dumps(col_labels)})')
        if row_labels:
            lines.append(f'ax.set_yticks(np.arange(len({json.dumps(row_labels)})))')
            lines.append(f'ax.set_yticklabels({json.dumps(row_labels)})')
        return '\n'.join(lines)

    elif chart_type == 'boxplot':
        lines = []
        labels = list(data.keys())
        values = list(data.values())
        lines.append(f'bplot = ax.boxplot({json.dumps(values)}, patch_artist=True, labels={json.dumps(labels)})')
        lines.append(f'colors = {json.dumps(palette[:len(labels)])}')
        lines.append('for patch, color in zip(bplot["boxes"], colors):')
        lines.append('    patch.set_facecolor(color)')
        lines.append('    patch.set_alpha(0.7)')
        return '\n'.join(lines)

    elif chart_type == 'histogram':
        lines = []
        values = data.get('values', [])
        bins = aesthetics.get('bins', 10)
        color = palette[0] if palette else '#1f77b4'
        lines.append(f'ax.hist({json.dumps(values)}, bins={bins}, color="{color}", edgecolor="black", alpha=0.7)')
        return '\n'.join(lines)

    else:
        return f'# TODO: 实现 {chart_type} 的渲染逻辑'

def write_manifest(recipe: dict, profile: dict, output_path: str) -> None:
    """输出渲染溯源元数据"""
    manifest = {
        'generated_at': datetime.now().isoformat(),
        'generator': 'sci-render-kit/matplotlib',
        'recipe': recipe.get('id', 'unknown'),
        'profile': profile.get('name', 'default'),
        'backend': 'matplotlib',
        'output': output_path,
        'checksum': 'sha256:placeholder',
        'parameters': {
            'aesthetics': recipe.get('aesthetics', {}),
            'data_keys': list(recipe.get('data', {}).keys()),
        }
    }
    manifest_path = Path(output_path).with_suffix('.manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

def render(recipe_path: str, profile_name: str = 'nature') -> None:
    """主渲染入口"""
    recipe = load_recipe(recipe_path)
    

    profile = load_profile(profile_name)
    
    # 生成代码
    code = generate_python_code(recipe, profile)
    
    # 输出到临时文件
    output = recipe['output']
    output_dir = Path(output.get('dir', 'output'))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    script_path = output_dir / '_generated_render.py'
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(code)
    
    print(f'✅ 已生成渲染脚本: {script_path}')
    print(f'📋 运行以下命令执行渲染:')
    print(f'   python {script_path}')
    
    # 写入 manifest（预览版）
    output_path = output_dir / output.get('filename', 'figure.png')
    write_manifest(recipe, profile, str(output_path))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='sci-render-kit matplotlib 后端')
    parser.add_argument('action', choices=['render'], help='操作')
    parser.add_argument('recipe', help='配方文件路径')
    parser.add_argument('--profile', default='nature', help='配置文件名')
    args = parser.parse_args()
    
    if args.action == 'render':
        render(args.recipe, args.profile)

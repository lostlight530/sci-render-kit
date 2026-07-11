#!/usr/bin/env python3
"""
Plotly 后端适配器 — 交互式科学可视化
Enhanced: Interactive hover, zoom, export to HTML/PNG
"""

import yaml
import json
import numpy as np
import sys
import os
from pathlib import Path
from datetime import datetime
import hashlib

try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.subplots import make_subplots
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    print("PLOTLY_NOT_INSTALLED")
    sys.exit(1)


def load_recipe(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_profile(name: str) -> dict:
    profile_path = Path('profiles') / f'{name}.yaml'
    if not profile_path.exists():
        return {}
    with open(profile_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_plotly_figure(recipe: dict, profile: dict) -> go.Figure:
    aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}
    palette = aesthetics.get('palette', px.colors.qualitative.Set1)
    chart_type = recipe['type']
    data = recipe['data']

    fig = None

    if chart_type == 'line-chart':
        fig = go.Figure()
        for i, (label, values) in enumerate(data.items()):
            color = palette[i % len(palette)] if isinstance(palette, list) else palette
            fig.add_trace(go.Scatter(
                x=list(range(len(values))),
                y=values,
                mode='lines+markers',
                name=label,
                line=dict(color=color, width=aesthetics.get('line_width', 2)),
                marker=dict(size=6)
            ))

    elif chart_type == 'bar-chart':
        fig = go.Figure()
        categories = list(data.keys())
        values = list(data.values())
        colors = [palette[i % len(palette)] for i in range(len(categories))]
        fig.add_trace(go.Bar(
            x=categories,
            y=values,
            marker_color=colors
        ))

    elif chart_type == 'scatter-plot':
        fig = go.Figure()
        for i, (label, (x, y)) in enumerate(data.items()):
            color = palette[i % len(palette)] if isinstance(palette, list) else palette
            fig.add_trace(go.Scatter(
                x=x, y=y,
                mode='markers',
                name=label,
                marker=dict(color=color, size=8)
            ))

    elif chart_type == 'heatmap':
        matrix = data.get('matrix', [])
        fig = go.Figure(data=go.Heatmap(
            z=matrix,
            colorscale=aesthetics.get('cmap', 'Viridis')
        ))

    elif chart_type == 'boxplot':
        fig = go.Figure()
        for i, (label, values) in enumerate(data.items()):
            fig.add_trace(go.Box(y=values, name=label))

    else:
        fig = go.Figure()
        fig.add_annotation(text=f"Unsupported chart type: {chart_type}", showarrow=False)

    # Apply layout
    font_size = aesthetics.get('font_size', 12)
    figsize = aesthetics.get('figsize', [800, 600])

    fig.update_layout(
        title=recipe.get('title', ''),
        font=dict(size=font_size, family=aesthetics.get('font', 'Arial')),
        width=figsize[0] if len(figsize) == 2 else 800,
        height=figsize[1] if len(figsize) == 2 else 600,
        template='plotly_white',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    return fig


def write_manifest(recipe: dict, profile: dict, output_path: str) -> None:
    manifest = {
        'generated_at': datetime.now().isoformat(),
        'generator': 'sci-render-kit/plotly',
        'recipe': recipe.get('id', 'unknown'),
        'profile': profile.get('name', 'default'),
        'backend': 'plotly',
        'output': output_path,
        'checksum': 'sha256:' + hashlib.sha256(open(output_path, 'rb').read()).hexdigest() if Path(output_path).exists() else 'none',
    }
    manifest_path = Path(output_path).with_suffix('.manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)


def render(recipe_path: str, profile_name: str = 'nature', output_dir: str = 'output') -> None:
    recipe = load_recipe(recipe_path)
    profile = load_profile(profile_name)

    output = recipe['output']
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    output_file = output.get('filename', 'figure.html')
    output_path = out_dir / output_file

    fig = generate_plotly_figure(recipe, profile)

    # Export
    if str(output_path).endswith('.html'):
        fig.write_html(str(output_path))
    else:
        fig.write_image(str(output_path), scale=2)

    print(f'✅ Plotly render complete: {output_path}')
    write_manifest(recipe, profile, str(output_path))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='sci-render-kit Plotly backend')
    parser.add_argument('action', choices=['render'])
    parser.add_argument('recipe')
    parser.add_argument('--profile', default='nature')
    parser.add_argument('--output-dir', default='output')
    args = parser.parse_args()

    if args.action == 'render':
        render(args.recipe, args.profile, args.output_dir)

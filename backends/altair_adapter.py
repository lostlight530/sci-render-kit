#!/usr/bin/env python3
"""
Altair 后端适配器 — 声明式可视化 (Vega-Lite)
Enhanced: Declarative grammar, automatic encoding, JSON export
"""

import yaml
import json
import sys
import os
from pathlib import Path
from datetime import datetime
import hashlib

try:
    import altair as alt
    import pandas as pd
    ALTAIR_AVAILABLE = True
except ImportError:
    ALTAIR_AVAILABLE = False
    print("ALTAIR_NOT_INSTALLED")
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


def generate_altair_chart(recipe: dict, profile: dict) -> alt.Chart:
    aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}
    palette = aesthetics.get('palette', ['#E69F00', '#56B4E9', '#009E73'])
    chart_type = recipe['type']
    data = recipe['data']

    # Convert to DataFrame
    if chart_type in ('line-chart', 'bar-chart'):
        df_data = []
        for label, values in data.items():
            for i, v in enumerate(values):
                df_data.append({'category': label, 'x': i, 'y': v})
        df = pd.DataFrame(df_data)
    elif chart_type == 'scatter-plot':
        df_data = []
        for label, (x_vals, y_vals) in data.items():
            for x, y in zip(x_vals, y_vals):
                df_data.append({'category': label, 'x': x, 'y': y})
        df = pd.DataFrame(df_data)
    else:
        df = pd.DataFrame(data)

    # Base chart
    base = alt.Chart(df).encode(
        color=alt.Color('category:N', scale=alt.Scale(range=palette))
    )

    if chart_type == 'line-chart':
        chart = base.mark_line().encode(
            x='x:Q',
            y='y:Q'
        )
    elif chart_type == 'bar-chart':
        chart = base.mark_bar().encode(
            x='category:N',
            y='y:Q'
        )
    elif chart_type == 'scatter-plot':
        chart = base.mark_circle(size=60).encode(
            x='x:Q',
            y='y:Q'
        )
    else:
        chart = base.mark_text().encode(
            text=alt.value(f"Unsupported: {chart_type}")
        )

    # Apply aesthetics
    font_size = aesthetics.get('font_size', 12)
    figsize = aesthetics.get('figsize', [400, 300])

    chart = chart.properties(
        width=figsize[0] if len(figsize) >= 2 else 400,
        height=figsize[1] if len(figsize) >= 2 else 300,
        title=recipe.get('title', '')
    ).configure_axis(
        labelFontSize=font_size,
        titleFontSize=font_size + 2
    )

    return chart


def write_manifest(recipe: dict, profile: dict, output_path: str) -> None:
    manifest = {
        'generated_at': datetime.now().isoformat(),
        'generator': 'sci-render-kit/altair',
        'recipe': recipe.get('id', 'unknown'),
        'profile': profile.get('name', 'default'),
        'backend': 'altair',
        'output': output_path,
    }
    manifest_path = Path(output_path).with_suffix('.manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)


def render(recipe_path: str, profile_name: str = 'nature', output_dir: str = 'output') -> None:
    recipe = load_recipe(recipe_path)
    profile = load_profile(profile_name)

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    output_file = recipe.get('output', {}).get('filename', 'figure.png')
    output_path = out_dir / output_file

    chart = generate_altair_chart(recipe, profile)

    if str(output_path).endswith('.json'):
        chart.save(str(output_path))
    else:
        chart.save(str(output_path))

    print(f'✅ Altair render complete: {output_path}')
    write_manifest(recipe, profile, str(output_path))


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='sci-render-kit Altair backend')
    parser.add_argument('action', choices=['render'])
    parser.add_argument('recipe')
    parser.add_argument('--profile', default='nature')
    parser.add_argument('--output-dir', default='output')
    args = parser.parse_args()

    if args.action == 'render':
        render(args.recipe, args.profile, args.output_dir)

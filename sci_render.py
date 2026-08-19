#!/usr/bin/env python3
"""
sci-render-kit 主入口 (CLI)
负责统一调度：配置读取、严格验证 (Schema & Quality Gates)、后端分发
"""

import argparse
import sys
import os
import yaml
import json
import subprocess
from pathlib import Path
from jsonschema import validate, ValidationError

from core.color_encoding import CognitiveColorEncoder
from core.palettes import describe_palette, resolve_categorical

# 采用离散系列着色的图表类型（语义色板按系列名解析）
SERIES_CHART_TYPES = {"line-chart", "bar-chart", "scatter-plot", "boxplot", "histogram"}

# 后端输出能力声明（与 MANIFEST.yaml 一致；dispatch 前强制校验）
BACKEND_CAPABILITIES = {
    'matplotlib': {'png', 'svg', 'pdf'},
    'ggplot2': {'png', 'svg', 'pdf'},
    'observable': {'html'},
}


def _hex_to_rgb(color: str):
    """解析 #RRGGBB / #RGB 十六进制颜色为 (r, g, b) 元组；无法解析返回 None"""
    if not isinstance(color, str):
        return None
    c = color.strip().lstrip('#')
    if len(c) == 3:
        c = ''.join(ch * 2 for ch in c)
    if len(c) != 6:
        return None
    try:
        return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))
    except ValueError:
        return None


def resolve_effective_palette(recipe: dict, aesthetics: dict) -> list:
    """计算渲染实际使用的色板。

    当配方/配置声明 ``semantic_palette: true`` 时，色板由
    core.color_encoding.CognitiveColorEncoder 按系列名的语义标签生成
    （优先于显式 palette）；否则使用显式声明的 palette。
    """
    chart_type = str(recipe.get('type', ''))
    labels = list(recipe.get('data', {}).keys()) if chart_type in SERIES_CHART_TYPES else []
    if aesthetics.get('semantic_palette'):
        if labels:
            return CognitiveColorEncoder().resolve_series_palette(labels)
    elif aesthetics.get('palette_name'):
        # 注册色板（core/palettes.py，含 CVD 安全标注）；P1 palette-name 门禁负责校验名称
        try:
            colors = resolve_categorical(str(aesthetics['palette_name']))
        except ValueError:
            return []
        return colors[:len(labels)] if labels else colors
    return [str(c) for c in aesthetics.get('palette', [])]


def load_yaml(path: str) -> dict:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print("YAML_PARSE_FAILURE")
        print(f"Error parsing YAML file {path}: {e}")
        sys.exit(1)

def run_quality_gates(recipe: dict, profile: dict, gates_def: dict):
    """根据 quality/gates.yaml 运行静态检查 (P0, P1)"""
    errors = []

    # 获取美学配置 (合并)
    aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}

    for gate in gates_def.get('gates', []):
        level = gate.get('level')
        # 目前只在渲染前做静态检查 (P0, P1)
        if level in ['P0', 'P1']:
            for check in gate.get('checks', []):
                cid = check.get('id')

                # 实现具体规则
                if cid == 'color-count':
                    palette = resolve_effective_palette(recipe, aesthetics)
                    if len(palette) > 8:
                        errors.append(f"[{gate['name']}] {check['name']}: palette 中颜色数({len(palette)})不能超过 8")

                elif cid == 'palette-contrast':
                    # 仅在声明 background 或启用 semantic_palette 时启用（向后兼容）
                    background = aesthetics.get('background')
                    use_semantic = bool(aesthetics.get('semantic_palette', False))
                    if background or use_semantic:
                        bg_value = background or '#FFFFFF'
                        bg_rgb = _hex_to_rgb(bg_value)
                        if bg_rgb is not None:
                            encoder = CognitiveColorEncoder()
                            for color in resolve_effective_palette(recipe, aesthetics):
                                rgb = _hex_to_rgb(color)
                                if rgb is None:
                                    continue
                                ratio = encoder.contrast_ratio(rgb, bg_rgb)
                                if ratio < 3.0:
                                    errors.append(
                                        f"[{gate['name']}] {check['name']}: 颜色 {color} 与背景 {bg_value} "
                                        f"的 WCAG 对比度 {ratio:.2f} 低于 3.0")

                elif cid == 'text-contrast':
                    # WCAG SC 1.4.3：声明 text_color 时，文字与背景对比度必须 ≥ 4.5
                    text_color = aesthetics.get('text_color')
                    if text_color:
                        bg_value = aesthetics.get('background') or '#FFFFFF'
                        fg_rgb = _hex_to_rgb(text_color)
                        bg_rgb = _hex_to_rgb(bg_value)
                        if fg_rgb is not None and bg_rgb is not None:
                            ratio = CognitiveColorEncoder().contrast_ratio(fg_rgb, bg_rgb)
                            if ratio < 4.5:
                                errors.append(
                                    f"[{gate['name']}] {check['name']}: 文字颜色 {text_color} 与背景 {bg_value} "
                                    f"的 WCAG 对比度 {ratio:.2f} 低于 4.5（SC 1.4.3）")

                elif cid == 'palette-adjacency':
                    # WCAG SC 1.4.11：声明 adjacency_check 时，分类色板两两对比度必须 ≥ 3.0
                    if aesthetics.get('adjacency_check'):
                        encoder = CognitiveColorEncoder()
                        colors = [c for c in resolve_effective_palette(recipe, aesthetics)
                                  if _hex_to_rgb(c) is not None]
                        seen = []
                        for color in colors:
                            if color.upper() in [s.upper() for s in seen]:
                                continue
                            for other in seen:
                                ratio = encoder.contrast_ratio(_hex_to_rgb(color), _hex_to_rgb(other))
                                if ratio < 3.0:
                                    errors.append(
                                        f"[{gate['name']}] {check['name']}: 色对 ({other}, {color}) "
                                        f"的 WCAG 对比度 {ratio:.2f} 低于 3.0（SC 1.4.11）")
                            seen.append(color)

                elif cid == 'cvd-contrast':
                    # Machado 2009 CVD 模拟：声明 background 或启用 semantic_palette 时，
                    # 色板颜色在三种色盲模拟下与背景的对比度必须保持 ≥ 3.0
                    background = aesthetics.get('background')
                    use_semantic = bool(aesthetics.get('semantic_palette', False))
                    if background or use_semantic:
                        from core.cvd_simulation import cvd_contrast_report  # 延迟导入（numpy）
                        bg_value = background or '#FFFFFF'
                        bg_rgb = _hex_to_rgb(bg_value)
                        if bg_rgb is not None:
                            encoder = CognitiveColorEncoder()
                            for color in resolve_effective_palette(recipe, aesthetics):
                                rgb = _hex_to_rgb(color)
                                if rgb is None:
                                    continue
                                worst_type, worst_ratio = cvd_contrast_report(
                                    rgb, bg_rgb, encoder.contrast_ratio)[0]
                                if worst_ratio < 3.0:
                                    errors.append(
                                        f"[{gate['name']}] {check['name']}: 颜色 {color} 在 {worst_type} "
                                        f"模拟（Machado 2009）下与背景 {bg_value} 的对比度 "
                                        f"{worst_ratio:.2f} 低于 3.0")

                elif cid == 'palette-name':
                    # 声明 palette_name 时必须命中注册表；系列图要求 categorical 类型
                    name = aesthetics.get('palette_name')
                    if name:
                        try:
                            entry = describe_palette(str(name))
                            chart_type = str(recipe.get('type', ''))
                            if chart_type in SERIES_CHART_TYPES and entry['kind'] != 'categorical':
                                errors.append(
                                    f"[{gate['name']}] {check['name']}: 色板 '{name}' 是 {entry['kind']} 色阶，"
                                    f"不能用于系列图分类着色；顺序/发散色阶请用 aesthetics.cmap")
                        except ValueError as e:
                            errors.append(f"[{gate['name']}] {check['name']}: {e}")

                elif cid == 'font-size':
                    font_size = aesthetics.get('font_size', 10)
                    profile_name = profile.get('name', '')
                    if profile_name == 'nature' and font_size < 5:
                        errors.append(f"[{gate['name']}] {check['name']}: Nature 期刊字号要求 >= 5 (当前 {font_size})")
                    elif profile_name == 'science' and font_size < 6:
                        errors.append(f"[{gate['name']}] {check['name']}: Science 期刊字号要求 >= 6 (当前 {font_size})")

                elif cid == 'forbidden-pairs':
                    # 简单检查红绿并存
                    palette = [c.lower() for c in aesthetics.get('palette', [])]
                    has_red = any(c in ['#ff0000', 'red'] for c in palette)
                    has_green = any(c in ['#00ff00', 'green'] for c in palette)
                    if has_red and has_green:
                        errors.append(f"[{gate['name']}] {check['name']}: 不建议同时包含高饱和度的红绿色")

                elif cid == 'no-3d':
                    if str(recipe.get('type', '')).startswith('3d-'):
                        errors.append(f"[{gate['name']}] {check['name']}: 严禁使用 3D 图表")

    return errors

def main():
    parser = argparse.ArgumentParser(description="sci-render-kit 统一入口")
    parser.add_argument('recipe', help="YAML 配方文件路径")
    parser.add_argument('--profile', default='nature', help="配置文件名，例如 nature, science, presentation")
    parser.add_argument('--backend', default='matplotlib', choices=['matplotlib', 'ggplot2', 'observable'], help="渲染后端")

    args = parser.parse_args()

    recipe_path = args.recipe
    if not os.path.exists(recipe_path):
        print(f"❌ 错误: 找不到配方文件 {recipe_path}")
        sys.exit(1)

    recipe = load_yaml(recipe_path)

    # 1. Schema 验证
    schema_path = 'metadata/recipe.schema.yaml'
    schema = load_yaml(schema_path)
    try:
        validate(instance=recipe, schema=schema)
        print("✅ P0 Schema 验证通过")
    except ValidationError as e:
        print("P0_SCHEMA_FAILURE")
        print("❌ [P0-recipe-valid] Schema 验证失败:")
        print(f"  - {e.message}")
        sys.exit(1)

    # 2. 统一读取 Profile
    profile_path = f'profiles/{args.profile}.yaml'
    if not os.path.exists(profile_path):
        print("MISSING_PROFILE")
        print(f"Error: Profile file not found: {profile_path}")
        sys.exit(1)
    profile = load_yaml(profile_path)

    # 3. 执行 Quality Gates (P0/P1)
    gates_path = 'quality/gates.yaml'
    gates = load_yaml(gates_path)

    gate_errors = run_quality_gates(recipe, profile, gates)
    if gate_errors:
        print("❌ 质量门检查失败:")
        for err in gate_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ P1 美学规范检查通过")

    # 3.5 后端能力校验：声明的输出格式必须在后端能力集内
    output_format = str(recipe.get('output', {}).get('format', 'png')).lower()
    allowed_formats = BACKEND_CAPABILITIES[args.backend]
    if output_format not in allowed_formats:
        print("BACKEND_CAPABILITY_MISMATCH")
        print(f"❌ 后端 {args.backend} 不支持输出格式 '{output_format}'"
              f"（支持: {', '.join(sorted(allowed_formats))}）")
        sys.exit(1)

    # 4. 调用对应的 Backend Adapter
    backend_script_map = {
        'matplotlib': ('python3', 'backends/matplotlib_adapter.py'),
        'ggplot2': ('Rscript', 'backends/ggplot2_adapter.R'),
        'observable': ('node', 'backends/observable_adapter.js')
    }

    cmd, script = backend_script_map[args.backend]

    print(f"🚀 将使用后端 {args.backend} 渲染配方...")
    try:
        # 我们把参数传递给后端的 CLI
        subprocess.run([cmd, script, "render", args.recipe, "--profile", args.profile], check=True)
    except subprocess.CalledProcessError as e:
        print("BACKEND_EXECUTION_FAILURE")
        print(f"❌ 后端执行失败, 返回码: {e.returncode}")
        sys.exit(1)

    # 5. 执行 Quality Gates (P2/P3 输出后检查)
    output_cfg = recipe.get('output', {})
    output_dir = output_cfg.get('dir', 'output')
    output_file = output_cfg.get('filename', 'figure.png')
    output_path = Path(output_dir) / output_file
    manifest_path = output_path.with_suffix('.manifest.json')

    post_errors = []

    # 合并后的美学参数（recipe 覆盖 profile），供 P3 期刊合规检查使用
    merged_aesthetics = {**profile.get('aesthetics', {}), **recipe.get('aesthetics', {})}
    profile_aesthetics = profile.get('aesthetics', {})

    for gate in gates.get('gates', []):
        level = gate.get('level')
        if level in ['P2', 'P3']:
            for check in gate.get('checks', []):
                cid = check.get('id')
                if cid == 'file-exists':
                    if not output_path.exists():
                        post_errors.append(f"[{gate['name']}] {check['name']}: 输出文件未生成")
                elif cid == 'non-empty':
                    if output_path.exists() and output_path.stat().st_size == 0:
                        post_errors.append(f"[{gate['name']}] {check['name']}: 输出文件为空")
                elif cid == 'format-match':
                    expected_ext = '.' + output_cfg.get('format', 'png').lower()
                    if output_path.suffix.lower() != expected_ext:
                        post_errors.append(f"[{gate['name']}] {check['name']}: 期望扩展名 {expected_ext} 但得到 {output_path.suffix.lower()}")
                elif cid == 'manifest-exists':
                    if not manifest_path.exists():
                        print("MANIFEST_MISSING")
                        post_errors.append(f"[{gate['name']}] {check['name']}: 溯源元数据文件未生成")
                elif cid == 'prov-exists':
                    # FAIR R1.2 溯源旁车：matplotlib 后端必须产出同名 .prov.json
                    # （R/JS 侧为可选跟进，能力边界如实声明，见 README）
                    if args.backend == 'matplotlib':
                        prov_path = output_path.with_suffix('.prov.json')
                        if not prov_path.exists():
                            post_errors.append(f"[{gate['name']}] {check['name']}: 溯源旁车文件 {prov_path} 未生成")
                elif cid == 'vector-format':
                    if args.profile in ['nature', 'science', 'cell']:
                        if output_path.suffix.lower() not in ['.pdf', '.eps']:
                            post_errors.append(f"[{gate['name']}] {check['name']}: {args.profile} 期望矢量格式 (.pdf/.eps)，但得到 {output_path.suffix.lower()}")
                elif cid == 'dpi-check':
                    # 合并后的 DPI 不得低于 profile 声明的期刊最低 DPI
                    min_dpi = profile_aesthetics.get('dpi')
                    actual_dpi = merged_aesthetics.get('dpi', min_dpi)
                    if min_dpi is not None and actual_dpi is not None and actual_dpi < min_dpi:
                        post_errors.append(f"[{gate['name']}] {check['name']}: DPI {actual_dpi} 低于 {args.profile} 最低要求 {min_dpi}")
                elif cid == 'size-check':
                    # figsize 必须为正值二元组；profile 声明 max_width_in 时宽度不得超限
                    figsize = merged_aesthetics.get('figsize')
                    if figsize is not None:
                        if (not isinstance(figsize, list) or len(figsize) != 2
                                or any(not isinstance(v, (int, float)) or v <= 0 for v in figsize)):
                            post_errors.append(f"[{gate['name']}] {check['name']}: figsize 必须为正值二元组，当前 {figsize}")
                        else:
                            max_width = profile_aesthetics.get('max_width_in')
                            if max_width is not None and figsize[0] > max_width:
                                post_errors.append(f"[{gate['name']}] {check['name']}: 图宽 {figsize[0]}in 超过 {args.profile} 版宽上限 {max_width}in")
                            max_height = profile_aesthetics.get('max_height_in')
                            if max_height is not None and figsize[1] > max_height:
                                post_errors.append(f"[{gate['name']}] {check['name']}: 图高 {figsize[1]}in 超过 {args.profile} 版面上限 {max_height}in")

    if post_errors:
        print("❌ 渲染后质量门检查失败:")
        for err in post_errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ P2/P3 输出检查通过")


if __name__ == "__main__":
    main()

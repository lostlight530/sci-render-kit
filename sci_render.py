#!/usr/bin/env python3
"""sci-render-kit unified CLI: schema, accessibility, quality gates, backend dispatch."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema import ValidationError, validate

from core.accessibility import (
    accessibility_config,
    build_accessibility_manifest,
    distinct_style_signatures,
    resolve_series_styles,
    write_accessibility_manifest,
)
from core.color_encoding import CognitiveColorEncoder
from core.palettes import describe_palette, resolve_categorical

SERIES_CHART_TYPES = {"line-chart", "bar-chart", "scatter-plot", "boxplot", "histogram"}
REDUNDANT_STYLE_TYPES = {"line-chart", "bar-chart", "scatter-plot"}

BACKEND_CAPABILITIES = {
    "matplotlib": {"png", "svg", "pdf"},
    "ggplot2": {"png", "svg", "pdf"},
    "observable": {"html"},
}

# Today only matplotlib consumes the non-color series-style contract end-to-end.
# Other backends remain available for recipes that do not request it.
BACKEND_ACCESSIBILITY_CAPABILITIES = {
    "matplotlib": {"text-alternative-sidecar", "redundant-series-style"},
    "ggplot2": {"text-alternative-sidecar"},
    "observable": {"text-alternative-sidecar"},
}


def _hex_to_rgb(color: str):
    if not isinstance(color, str):
        return None
    value = color.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        return None
    try:
        return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def resolve_effective_palette(recipe: dict, aesthetics: dict) -> list:
    chart_type = str(recipe.get("type", ""))
    labels = list(recipe.get("data", {}).keys()) if chart_type in SERIES_CHART_TYPES else []
    if aesthetics.get("semantic_palette"):
        if labels:
            return CognitiveColorEncoder().resolve_series_palette(labels)
    elif aesthetics.get("palette_name"):
        try:
            colors = resolve_categorical(str(aesthetics["palette_name"]))
        except ValueError:
            return []
        return colors[:len(labels)] if labels else colors
    return [str(c) for c in aesthetics.get("palette", [])]


def load_yaml(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        print("YAML_PARSE_FAILURE")
        print(f"Error parsing YAML file {path}: {exc}")
        sys.exit(1)


def run_quality_gates(recipe: dict, profile: dict, gates_def: dict):
    """Run deterministic pre-render P0/P1 rules."""
    errors = []
    aesthetics = {**profile.get("aesthetics", {}), **recipe.get("aesthetics", {})}
    access = accessibility_config(recipe)
    chart_type = str(recipe.get("type", ""))
    labels = list(recipe.get("data", {}).keys()) if chart_type in SERIES_CHART_TYPES else []

    for gate in gates_def.get("gates", []):
        if gate.get("level") not in ["P0", "P1"]:
            continue
        for check in gate.get("checks", []):
            cid = check.get("id")

            if cid == "color-count":
                palette = resolve_effective_palette(recipe, aesthetics)
                if len(palette) > 8:
                    errors.append(f"[{gate['name']}] {check['name']}: palette 中颜色数({len(palette)})不能超过 8")

            elif cid == "palette-contrast":
                background = aesthetics.get("background")
                use_semantic = bool(aesthetics.get("semantic_palette", False))
                if background or use_semantic:
                    bg_value = background or "#FFFFFF"
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
                                    f"的 WCAG 对比度 {ratio:.2f} 低于 3.0"
                                )

            elif cid == "text-contrast":
                text_color = aesthetics.get("text_color")
                if text_color:
                    bg_value = aesthetics.get("background") or "#FFFFFF"
                    fg_rgb = _hex_to_rgb(text_color)
                    bg_rgb = _hex_to_rgb(bg_value)
                    if fg_rgb is not None and bg_rgb is not None:
                        ratio = CognitiveColorEncoder().contrast_ratio(fg_rgb, bg_rgb)
                        if ratio < 4.5:
                            errors.append(
                                f"[{gate['name']}] {check['name']}: 文字颜色 {text_color} 与背景 {bg_value} "
                                f"的 WCAG 对比度 {ratio:.2f} 低于 4.5（SC 1.4.3）"
                            )

            elif cid == "palette-adjacency":
                # Legacy project-strict mode: every unique categorical pair is tested.
                # This is intentionally stronger than WCAG's actual-adjacent-object scope.
                if aesthetics.get("adjacency_check"):
                    encoder = CognitiveColorEncoder()
                    colors = [c for c in resolve_effective_palette(recipe, aesthetics) if _hex_to_rgb(c) is not None]
                    seen = []
                    for color in colors:
                        if color.upper() in [s.upper() for s in seen]:
                            continue
                        for other in seen:
                            ratio = encoder.contrast_ratio(_hex_to_rgb(color), _hex_to_rgb(other))
                            if ratio < 3.0:
                                errors.append(
                                    f"[{gate['name']}] {check['name']}: 色对 ({other}, {color}) 的 WCAG 对比度 "
                                    f"{ratio:.2f} 低于 3.0（项目严格策略，参考 SC 1.4.11）"
                                )
                        seen.append(color)

            elif cid == "declared-adjacency":
                pairs = access.get("adjacent_pairs") or []
                if pairs and labels:
                    palette = resolve_effective_palette(recipe, aesthetics)
                    color_by_label = {
                        label: palette[i % len(palette)]
                        for i, label in enumerate(labels)
                    } if palette else {}
                    encoder = CognitiveColorEncoder()
                    for pair in pairs:
                        if not isinstance(pair, list) or len(pair) != 2:
                            continue  # JSON Schema owns shape validation.
                        left, right = pair
                        if left not in color_by_label or right not in color_by_label:
                            errors.append(
                                f"[{gate['name']}] {check['name']}: adjacent_pairs 引用了未知系列 ({left}, {right})"
                            )
                            continue
                        left_rgb = _hex_to_rgb(color_by_label[left])
                        right_rgb = _hex_to_rgb(color_by_label[right])
                        if left_rgb is None or right_rgb is None:
                            continue
                        ratio = encoder.contrast_ratio(left_rgb, right_rgb)
                        if ratio < 3.0:
                            errors.append(
                                f"[{gate['name']}] {check['name']}: 实际相邻系列 ({left}, {right}) 的颜色边界对比度 "
                                f"{ratio:.2f} 低于 3.0（SC 1.4.11 / G209）"
                            )

            elif cid == "text-alternative":
                if access.get("require_alt_text") and not str(access.get("alt_text", "")).strip():
                    errors.append(
                        f"[{gate['name']}] {check['name']}: require_alt_text=true 时必须提供 alt_text（SC 1.1.1）"
                    )

            elif cid == "non-color-cue":
                mode = access.get("redundant_encoding", "off")
                if mode == "required" and chart_type in REDUNDANT_STYLE_TYPES and len(labels) > 1:
                    styles = resolve_series_styles(labels, access)
                    if len(styles) != len(labels) or distinct_style_signatures(styles) < len(labels):
                        errors.append(
                            f"[{gate['name']}] {check['name']}: 多系列图缺少可区分的非颜色视觉线索（SC 1.4.1）"
                        )

            elif cid == "cvd-contrast":
                background = aesthetics.get("background")
                use_semantic = bool(aesthetics.get("semantic_palette", False))
                if background or use_semantic:
                    from core.cvd_simulation import cvd_contrast_report
                    bg_value = background or "#FFFFFF"
                    bg_rgb = _hex_to_rgb(bg_value)
                    if bg_rgb is not None:
                        encoder = CognitiveColorEncoder()
                        for color in resolve_effective_palette(recipe, aesthetics):
                            rgb = _hex_to_rgb(color)
                            if rgb is None:
                                continue
                            worst_type, worst_ratio = cvd_contrast_report(rgb, bg_rgb, encoder.contrast_ratio)[0]
                            if worst_ratio < 3.0:
                                errors.append(
                                    f"[{gate['name']}] {check['name']}: 颜色 {color} 在 {worst_type} 模拟（Machado 2009）下"
                                    f"与背景 {bg_value} 的对比度 {worst_ratio:.2f} 低于 3.0"
                                )

            elif cid == "palette-name":
                name = aesthetics.get("palette_name")
                if name:
                    try:
                        entry = describe_palette(str(name))
                        if chart_type in SERIES_CHART_TYPES and entry["kind"] != "categorical":
                            errors.append(
                                f"[{gate['name']}] {check['name']}: 色板 '{name}' 是 {entry['kind']} 色阶，"
                                "不能用于系列图分类着色；顺序/发散色阶请用 aesthetics.cmap"
                            )
                    except ValueError as exc:
                        errors.append(f"[{gate['name']}] {check['name']}: {exc}")

            elif cid == "font-size":
                font_size = aesthetics.get("font_size", 10)
                profile_name = profile.get("name", "")
                if profile_name == "nature" and font_size < 5:
                    errors.append(f"[{gate['name']}] {check['name']}: Nature 期刊字号要求 >= 5 (当前 {font_size})")
                elif profile_name == "science" and font_size < 6:
                    errors.append(f"[{gate['name']}] {check['name']}: Science 期刊字号要求 >= 6 (当前 {font_size})")

            elif cid == "forbidden-pairs":
                palette = [c.lower() for c in aesthetics.get("palette", [])]
                has_red = any(c in ["#ff0000", "red"] for c in palette)
                has_green = any(c in ["#00ff00", "green"] for c in palette)
                if has_red and has_green:
                    errors.append(f"[{gate['name']}] {check['name']}: 不建议同时包含高饱和度的红绿色")

            elif cid == "no-3d":
                if chart_type.startswith("3d-"):
                    errors.append(f"[{gate['name']}] {check['name']}: 严禁使用 3D 图表")

    return errors


def main():
    parser = argparse.ArgumentParser(description="sci-render-kit 统一入口")
    parser.add_argument("recipe", help="YAML 配方文件路径")
    parser.add_argument("--profile", default="nature", help="配置文件名，例如 nature, science, presentation")
    parser.add_argument("--backend", default="matplotlib", choices=["matplotlib", "ggplot2", "observable"], help="渲染后端")
    args = parser.parse_args()

    if not os.path.exists(args.recipe):
        print(f"❌ 错误: 找不到配方文件 {args.recipe}")
        sys.exit(1)
    recipe = load_yaml(args.recipe)

    schema = load_yaml("metadata/recipe.schema.yaml")
    try:
        validate(instance=recipe, schema=schema)
        print("✅ P0 Schema 验证通过")
    except ValidationError as exc:
        print("P0_SCHEMA_FAILURE")
        print("❌ [P0-recipe-valid] Schema 验证失败:")
        print(f"  - {exc.message}")
        sys.exit(1)

    profile_path = f"profiles/{args.profile}.yaml"
    if not os.path.exists(profile_path):
        print("MISSING_PROFILE")
        print(f"Error: Profile file not found: {profile_path}")
        sys.exit(1)
    profile = load_yaml(profile_path)
    gates = load_yaml("quality/gates.yaml")

    gate_errors = run_quality_gates(recipe, profile, gates)
    if gate_errors:
        print("❌ 质量门检查失败:")
        for err in gate_errors:
            print(f"  - {err}")
        sys.exit(1)
    print("✅ P1 美学/可访问性检查通过")

    output_format = str(recipe.get("output", {}).get("format", "png")).lower()
    allowed_formats = BACKEND_CAPABILITIES[args.backend]
    if output_format not in allowed_formats:
        print("BACKEND_CAPABILITY_MISMATCH")
        print(f"❌ 后端 {args.backend} 不支持输出格式 '{output_format}'（支持: {', '.join(sorted(allowed_formats))}）")
        sys.exit(1)

    access = accessibility_config(recipe)
    if (access.get("redundant_encoding") in {"auto", "required"}
            and str(recipe.get("type")) in REDUNDANT_STYLE_TYPES
            and "redundant-series-style" not in BACKEND_ACCESSIBILITY_CAPABILITIES[args.backend]):
        print("BACKEND_ACCESSIBILITY_MISMATCH")
        print(f"❌ 后端 {args.backend} 尚未实现 accessibility.redundant_encoding 的实际系列样式映射")
        sys.exit(1)

    backend_script_map = {
        "matplotlib": ("python3", "backends/matplotlib_adapter.py"),
        "ggplot2": ("Rscript", "backends/ggplot2_adapter.R"),
        "observable": ("node", "backends/observable_adapter.js"),
    }
    cmd, script = backend_script_map[args.backend]
    print(f"🚀 将使用后端 {args.backend} 渲染配方...")
    try:
        subprocess.run([cmd, script, "render", args.recipe, "--profile", args.profile], check=True)
    except subprocess.CalledProcessError as exc:
        print("BACKEND_EXECUTION_FAILURE")
        print(f"❌ 后端执行失败, 返回码: {exc.returncode}")
        sys.exit(1)

    output_cfg = recipe.get("output", {})
    output_path = Path(output_cfg.get("dir", "output")) / output_cfg.get("filename", "figure.png")
    manifest_path = output_path.with_suffix(".manifest.json")

    # A single backend-independent accessibility sidecar keeps the contract portable.
    if "accessibility" in recipe:
        merged_aesthetics_for_a11y = {**profile.get("aesthetics", {}), **recipe.get("aesthetics", {})}
        a11y_manifest = build_accessibility_manifest(
            recipe, resolve_effective_palette(recipe, merged_aesthetics_for_a11y)
        )
        write_accessibility_manifest(output_path, a11y_manifest)

    post_errors = []
    merged_aesthetics = {**profile.get("aesthetics", {}), **recipe.get("aesthetics", {})}
    profile_aesthetics = profile.get("aesthetics", {})

    for gate in gates.get("gates", []):
        if gate.get("level") not in ["P2", "P3"]:
            continue
        for check in gate.get("checks", []):
            cid = check.get("id")
            if cid == "file-exists":
                if not output_path.exists():
                    post_errors.append(f"[{gate['name']}] {check['name']}: 输出文件未生成")
            elif cid == "non-empty":
                if output_path.exists() and output_path.stat().st_size == 0:
                    post_errors.append(f"[{gate['name']}] {check['name']}: 输出文件为空")
            elif cid == "format-match":
                expected_ext = "." + output_cfg.get("format", "png").lower()
                if output_path.suffix.lower() != expected_ext:
                    post_errors.append(f"[{gate['name']}] {check['name']}: 期望扩展名 {expected_ext} 但得到 {output_path.suffix.lower()}")
            elif cid == "manifest-exists":
                if not manifest_path.exists():
                    print("MANIFEST_MISSING")
                    post_errors.append(f"[{gate['name']}] {check['name']}: 溯源元数据文件未生成")
            elif cid == "prov-exists":
                if args.backend == "matplotlib":
                    prov_path = output_path.with_suffix(".prov.json")
                    if not prov_path.exists():
                        post_errors.append(f"[{gate['name']}] {check['name']}: 溯源旁车文件 {prov_path} 未生成")
            elif cid == "a11y-exists":
                if "accessibility" in recipe:
                    a11y_path = output_path.with_suffix(".a11y.json")
                    if not a11y_path.exists():
                        post_errors.append(f"[{gate['name']}] {check['name']}: 可访问性旁车文件 {a11y_path} 未生成")
            elif cid == "vector-format":
                if args.profile in ["nature", "science", "cell"] and output_path.suffix.lower() not in [".pdf", ".eps"]:
                    post_errors.append(f"[{gate['name']}] {check['name']}: {args.profile} 期望矢量格式 (.pdf/.eps)，但得到 {output_path.suffix.lower()}")
            elif cid == "dpi-check":
                min_dpi = profile_aesthetics.get("dpi")
                actual_dpi = merged_aesthetics.get("dpi", min_dpi)
                if min_dpi is not None and actual_dpi is not None and actual_dpi < min_dpi:
                    post_errors.append(f"[{gate['name']}] {check['name']}: DPI {actual_dpi} 低于 {args.profile} 最低要求 {min_dpi}")
            elif cid == "size-check":
                figsize = merged_aesthetics.get("figsize")
                if figsize is not None:
                    if (not isinstance(figsize, list) or len(figsize) != 2
                            or any(not isinstance(v, (int, float)) or v <= 0 for v in figsize)):
                        post_errors.append(f"[{gate['name']}] {check['name']}: figsize 必须为正值二元组，当前 {figsize}")
                    else:
                        max_width = profile_aesthetics.get("max_width_in")
                        if max_width is not None and figsize[0] > max_width:
                            post_errors.append(f"[{gate['name']}] {check['name']}: 图宽 {figsize[0]}in 超过 {args.profile} 版宽上限 {max_width}in")
                        max_height = profile_aesthetics.get("max_height_in")
                        if max_height is not None and figsize[1] > max_height:
                            post_errors.append(f"[{gate['name']}] {check['name']}: 图高 {figsize[1]}in 超过 {args.profile} 版面上限 {max_height}in")

    if post_errors:
        print("❌ 渲染后质量门检查失败:")
        for err in post_errors:
            print(f"  - {err}")
        sys.exit(1)
    print("✅ P2/P3 输出检查通过")


if __name__ == "__main__":
    main()

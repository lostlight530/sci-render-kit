#!/usr/bin/env python3
"""Accessibility-aware Matplotlib adapter.

The mature renderer/provenance implementation lives in ``matplotlib_base.py``.
This public adapter preserves the established module API while adding a policy
layer for non-color redundant encoding and text-alternative metadata.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Preserve direct script execution from any working directory:
# python3 backends/matplotlib_adapter.py ...
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backends import matplotlib_base as base
from core.accessibility import accessibility_config, resolve_series_styles

# Preserve the public API used by repository tests and downstream callers.
DEFAULT_PALETTE = base.DEFAULT_PALETTE
SERIES_CHART_TYPES = base.SERIES_CHART_TYPES
resolve_palette = base.resolve_palette
load_recipe = base.load_recipe
load_profile = base.load_profile
validate_recipe = base.validate_recipe
build_provenance = base.build_provenance
generate_python_code = base.generate_python_code
generate_render_logic = base.generate_render_logic
write_manifest = base.write_manifest
write_provenance_sidecar = base.write_provenance_sidecar

_ACTIVE_ACCESSIBILITY = {}
_ORIGINAL_RENDER_LOGIC = base.generate_render_logic
_ORIGINAL_METADATA = base._savefig_metadata


def _accessible_render_logic(chart_type: str, data: dict, aesthetics: dict) -> str:
    labels = list(data.keys())
    styles = resolve_series_styles(labels, _ACTIVE_ACCESSIBILITY)
    if not styles or chart_type not in {"line-chart", "scatter-plot", "bar-chart"}:
        return _ORIGINAL_RENDER_LOGIC(chart_type, data, aesthetics)

    palette = base.resolve_palette(aesthetics, chart_type, data)
    lines = []

    if chart_type == "line-chart":
        for i, (label, values) in enumerate(data.items()):
            color = palette[i % len(palette)]
            style = styles[label]
            lines.append(f"x = np.arange(len({json.dumps(values)}))")
            lines.append(
                "ax.plot(x, {values}, color={color}, linewidth=1.0, label={label}, "
                "marker={marker}, linestyle={line_style}, markersize=3.5)".format(
                    values=json.dumps(values),
                    color=json.dumps(color),
                    label=json.dumps(label),
                    marker=json.dumps(style.get("marker", "o")),
                    line_style=json.dumps(style.get("line_style", "-")),
                )
            )
        lines.append("ax.legend(frameon=False)")
        return "\n".join(lines)

    if chart_type == "scatter-plot":
        for i, (label, pair) in enumerate(data.items()):
            x, y = pair
            color = palette[i % len(palette)]
            style = styles[label]
            lines.append(
                "ax.scatter({x}, {y}, c={color}, s=22, label={label}, marker={marker}, "
                "edgecolors=\"black\", linewidths=0.4)".format(
                    x=json.dumps(x), y=json.dumps(y), color=json.dumps(color),
                    label=json.dumps(label), marker=json.dumps(style.get("marker", "o")),
                )
            )
        lines.append("ax.legend(frameon=False)")
        return "\n".join(lines)

    categories = list(data.keys())
    values = list(data.values())
    bar_width = 0.6
    lines.append(f"x = np.arange({len(categories)})")
    for i, (label, value) in enumerate(zip(categories, values)):
        color = palette[i % len(palette)]
        hatch = styles[label].get("hatch", "")
        lines.append(
            "ax.bar(x[{i}] + {offset}, {value}, width={width}, color={color}, "
            "edgecolor=\"black\", linewidth=0.6, hatch={hatch})".format(
                i=i, offset=bar_width / 2, value=json.dumps(value), width=bar_width,
                color=json.dumps(color), hatch=json.dumps(hatch),
            )
        )
    lines.append(f"ax.set_xticks(x + {bar_width / 2})")
    lines.append(f"ax.set_xticklabels({json.dumps(categories)})")
    return "\n".join(lines)


def _accessible_metadata(provenance: dict, fmt: str, recipe: dict):
    metadata = dict(_ORIGINAL_METADATA(provenance, fmt, recipe) or {})
    alt_text = str(accessibility_config(recipe).get("alt_text") or "").strip()
    if not alt_text:
        return metadata or None
    if fmt == "png":
        metadata["srk:alt-text"] = alt_text
    elif fmt == "svg":
        metadata["Description"] = alt_text
    elif fmt == "pdf":
        metadata["Subject"] = alt_text
    return metadata


def render(recipe_path: str, profile_name: str = "nature") -> None:
    global _ACTIVE_ACCESSIBILITY
    recipe = base.load_recipe(recipe_path)
    _ACTIVE_ACCESSIBILITY = accessibility_config(recipe)
    base.generate_render_logic = _accessible_render_logic
    base._savefig_metadata = _accessible_metadata
    try:
        base.render(recipe_path, profile_name)
    finally:
        base.generate_render_logic = _ORIGINAL_RENDER_LOGIC
        base._savefig_metadata = _ORIGINAL_METADATA
        _ACTIVE_ACCESSIBILITY = {}

    # Extend, never replace, the existing reproducibility manifest.
    output = recipe.get("output", {})
    output_path = Path(output.get("dir", "output")) / output.get("filename", "figure.png")
    manifest_path = output_path.with_suffix(".manifest.json")
    if manifest_path.exists() and "accessibility" in recipe:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest["accessibility"] = {
            "profile": "sci-render-kit/a11y@1",
            "sidecar": output_path.with_suffix(".a11y.json").name,
            "redundant_encoding": accessibility_config(recipe).get("redundant_encoding", "off"),
            "alt_text_embedded_where_supported": bool(
                str(accessibility_config(recipe).get("alt_text") or "").strip()
            ),
        }
        manifest_path.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sci-render-kit accessibility-aware matplotlib backend")
    parser.add_argument("action", choices=["render"])
    parser.add_argument("recipe")
    parser.add_argument("--profile", default="nature")
    args = parser.parse_args()
    if args.action == "render":
        render(args.recipe, args.profile)

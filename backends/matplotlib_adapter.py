#!/usr/bin/env python3
"""Accessibility-aware Matplotlib adapter.

The mature renderer/provenance implementation lives in ``matplotlib_base.py``.
This adapter extends render logic through explicit function injection rather
than mutating base-module globals, so independent renders do not share hidden
accessibility state.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from backends import matplotlib_base as base
from core.accessibility import accessibility_config, resolve_series_styles

DEFAULT_PALETTE = base.DEFAULT_PALETTE
SERIES_CHART_TYPES = base.SERIES_CHART_TYPES
resolve_palette = base.resolve_palette
load_recipe = base.load_recipe
load_profile = base.load_profile
validate_recipe = base.validate_recipe
build_provenance = base.build_provenance
generate_render_logic = base.generate_render_logic
write_manifest = base.write_manifest
write_provenance_sidecar = base.write_provenance_sidecar


def _accessible_render_logic(accessibility: dict):
    """Return a render-logic function bound to one recipe's accessibility config."""

    def render_logic(chart_type: str, data: dict, aesthetics: dict) -> str:
        labels = list(data.keys())
        styles = resolve_series_styles(labels, accessibility)
        if not styles or chart_type not in {"line-chart", "scatter-plot", "bar-chart"}:
            return base.generate_render_logic(chart_type, data, aesthetics)

        palette = base.resolve_palette(aesthetics, chart_type, data)
        lines = []

        if chart_type == "line-chart":
            for index, (label, values) in enumerate(data.items()):
                color = palette[index % len(palette)]
                style = styles[label]
                lines.append(f"x = np.arange(len({repr(values)}))")
                lines.append(
                    "ax.plot(x, {values}, color={color}, label={label}, marker={marker}, "
                    "linestyle={line_style}, markersize=3.5)".format(
                        values=repr(values),
                        color=repr(color),
                        label=repr(str(label)),
                        marker=repr(style.get("marker", "o")),
                        line_style=repr(style.get("line_style", "-")),
                    )
                )
            lines.append("ax.legend(frameon=False)")
            return "\n".join(lines)

        if chart_type == "scatter-plot":
            for index, (label, pair) in enumerate(data.items()):
                if not isinstance(pair, (list, tuple)) or len(pair) != 2:
                    raise ValueError(f"scatter series {label!r} must be [x_values, y_values]")
                x, y = pair
                color = palette[index % len(palette)]
                style = styles[label]
                lines.append(
                    "ax.scatter({x}, {y}, c={color}, s=22, label={label}, marker={marker}, "
                    "edgecolors='black', linewidths=0.4)".format(
                        x=repr(x),
                        y=repr(y),
                        color=repr(color),
                        label=repr(str(label)),
                        marker=repr(style.get("marker", "o")),
                    )
                )
            lines.append("ax.legend(frameon=False)")
            return "\n".join(lines)

        categories = list(data.keys())
        values = list(data.values())
        lines.append(f"x = np.arange({len(categories)})")
        for index, (label, value) in enumerate(zip(categories, values)):
            color = palette[index % len(palette)]
            hatch = styles[label].get("hatch", "")
            lines.append(
                "ax.bar(x[{index}], {value}, width=0.6, color={color}, "
                "edgecolor='black', linewidth=0.6, hatch={hatch})".format(
                    index=index,
                    value=repr(value),
                    color=repr(color),
                    hatch=repr(hatch),
                )
            )
        lines.append("ax.set_xticks(x)")
        lines.append(f"ax.set_xticklabels({repr([str(value) for value in categories])})")
        return "\n".join(lines)

    return render_logic


def _accessible_metadata(accessibility: dict):
    """Return a format metadata function bound to one recipe's alt text."""

    def metadata(provenance: dict, fmt: str, recipe: dict):
        result = dict(base._savefig_metadata(provenance, fmt, recipe) or {})
        alt_text = str(accessibility.get("alt_text") or "").strip()
        if not alt_text:
            return result or None
        if fmt == "png":
            result["srk:alt-text"] = alt_text
        elif fmt == "svg":
            result["Description"] = alt_text
        elif fmt == "pdf":
            result["Subject"] = alt_text
        return result

    return metadata


def render(recipe_path: str, profile_name: str = "nature") -> None:
    recipe = base.load_recipe(recipe_path)
    accessibility = accessibility_config(recipe)
    base.render(
        recipe_path,
        profile_name,
        render_logic_fn=_accessible_render_logic(accessibility),
        metadata_fn=_accessible_metadata(accessibility),
    )

    output = recipe.get("output") or {}
    output_path = Path(output.get("dir", "output")) / output.get("filename", "figure.png")
    manifest_path = output_path.with_suffix(".manifest.json")
    if manifest_path.exists() and "accessibility" in recipe:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest.setdefault("provenance", {})["accessibility_sidecar"] = output_path.with_suffix(".a11y.json").name
        manifest["accessibility"] = {
            "profile": "sci-render-kit/a11y@1",
            "redundant_encoding": accessibility.get("redundant_encoding", "off"),
            "alt_text_embedded_where_supported": bool(str(accessibility.get("alt_text") or "").strip()),
        }
        temp = manifest_path.with_suffix(".manifest.json.tmp")
        temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temp.replace(manifest_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sci-render-kit accessibility-aware matplotlib backend")
    parser.add_argument("action", choices=["render"])
    parser.add_argument("recipe")
    parser.add_argument("--profile", default="nature")
    args = parser.parse_args()
    if args.action == "render":
        render(args.recipe, args.profile)

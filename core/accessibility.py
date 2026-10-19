#!/usr/bin/env python3
"""Accessibility contract helpers for recipe-driven scientific figures.

The module implements project-level support for WCAG 2.2 design principles:
- SC 1.1.1: text alternatives for non-text content
- SC 1.4.1: do not use color as the only visual means of conveying information
- SC 1.4.11: contrast for graphical objects required for understanding

These helpers support better figures; they do not by themselves constitute a
WCAG conformance claim for a paper, PDF, website, or publishing platform.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Dict, Iterable, List

PROFILE = "sci-render-kit/a11y"

STYLE_CYCLE = [
    {"marker": "o", "line_style": "-", "hatch": ""},
    {"marker": "s", "line_style": "--", "hatch": "//"},
    {"marker": "^", "line_style": "-.", "hatch": "\\\\"},
    {"marker": "D", "line_style": ":", "hatch": "xx"},
    {"marker": "v", "line_style": "-", "hatch": ".."},
    {"marker": "P", "line_style": "--", "hatch": "++"},
    {"marker": "X", "line_style": "-.", "hatch": "oo"},
    {"marker": "*", "line_style": ":", "hatch": "**"},
]


def accessibility_config(recipe: dict) -> dict:
    value = recipe.get("accessibility") or {}
    return value if isinstance(value, dict) else {}


def resolve_series_styles(labels: Iterable[str], accessibility: dict) -> Dict[str, dict]:
    """Resolve declared or generated non-color cues for series labels.

    The eight historical defaults are unchanged. For up to 32 distinct labels,
    generated marker/line/hatch tuples are unique; larger plots may need
    caller-declared overrides and remain subject to the runtime duplicate check.
    Tuple identity is not a measured visual-perception guarantee.
    """
    labels = list(labels)
    declared = accessibility.get("series_styles") or {}
    mode = accessibility.get("redundant_encoding", "off")
    if mode == "off" and not declared:
        return {}

    resolved: Dict[str, dict] = {}
    for index, label in enumerate(labels):
        # Bounded generated styles: after 32, collisions remain visible
        # to the chart-type-aware non-color-cue check unless overridden.
        slot = index % (len(STYLE_CYCLE) * 4)
        base = dict(STYLE_CYCLE[slot % len(STYLE_CYCLE)])
        if slot >= len(STYLE_CYCLE):
            variant = slot // len(STYLE_CYCLE)
            cue = slot % len(STYLE_CYCLE)
            line_styles = ("-", "--", "-.", ":")
            base["line_style"] = line_styles[(cue % 4 + variant) % 4]
            # Matplotlib accepts (num_sides, style, angle) marker tuples.
            # Unlike line-style-only changes, markers affect scatter output.
            base["marker"] = (3 + cue, 0, variant * 15)
            # Hatch density varies independently of line style/marker;
            # bar charts only draw this non-color cue.
            hatch_symbols = ("|", "/", "\\", "x", ".", "+", "o", "*")
            base["hatch"] = hatch_symbols[cue] * (variant + 2)
        override = declared.get(label) or {}
        if isinstance(override, dict):
            base.update({k: v for k, v in override.items() if k in {"marker", "line_style", "hatch"}})
        resolved[label] = base
    return resolved


def _effective_cue_identity(field: str, value: object) -> object:
    """Canonicalize explicitly absent cue aliases used by Matplotlib.

    Markers and line styles named none/None are not drawn.
    For hatch, whitespace and empty strings both give a plain fill.
    Other values are preserved; this is not perceptual equivalence.
    """
    if field in {"marker", "line_style"}:
        if value is None or (
            isinstance(value, str) and value.strip().lower() in {"", "none"}
        ):
            return None
    if field == "hatch" and isinstance(value, str) and not value.strip():
        return ""
    return value


def missing_required_non_color_cues(styles: Dict[str, dict], chart_type: str) -> bool:
    """Find a series with no rendered non-color cue on this chart type.

    A plain bar may distinguish itself from hatched bars, but a scatter
    series without a marker, or a line with neither line nor marker, has no
    non-color channel even if other series do.
    """
    for style in styles.values():
        marker = _effective_cue_identity("marker", style.get("marker"))
        line = _effective_cue_identity("line_style", style.get("line_style"))
        if chart_type == "scatter-plot" and marker is None:
            return True
        if chart_type == "line-chart" and marker is None and line is None:
            return True
    return False


def distinct_style_signatures(styles: Dict[str, dict], chart_type: str | None = None) -> int:
    """Count chart-effective cues, normalizing equivalent absent-style aliases.

    Lines use marker + linestyle; scatter uses marker; bars use hatch.
    Without chart_type retain the original full-tuple field selection.
    """
    fields = {
        "line-chart": ("marker", "line_style"),
        "scatter-plot": ("marker",),
        "bar-chart": ("hatch",),
    }.get(chart_type, ("marker", "line_style", "hatch"))
    return len({
        tuple(_effective_cue_identity(field, style.get(field)) for field in fields)
        for style in styles.values()
    })


def build_accessibility_manifest(recipe: dict, palette: List[str]) -> dict:
    cfg = accessibility_config(recipe)
    labels = list((recipe.get("data") or {}).keys())
    styles = resolve_series_styles(labels, cfg)
    series = []
    for index, label in enumerate(labels):
        item = {"label": label}
        if palette:
            item["color"] = palette[index % len(palette)]
        if label in styles:
            item["non_color_cue"] = styles[label]
        series.append(item)

    return {
        "profile": PROFILE,
        "recipe_id": recipe.get("id", "unknown"),
        "chart_type": recipe.get("type"),
        "alt_text": cfg.get("alt_text"),
        "long_description": cfg.get("long_description"),
        "redundant_encoding": cfg.get("redundant_encoding", "off"),
        "adjacent_pairs": cfg.get("adjacent_pairs", []),
        "series": series,
        "standards_scope": {
            "wcag_2_2": ["1.1.1 text alternative support", "1.4.1 non-color cue support", "1.4.11 declared adjacent-object contrast support"],
            "conformance_claim": False,
        },
    }


def write_accessibility_manifest(output_path: Path, manifest: dict) -> Path:
    path = output_path.with_suffix(".a11y.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".a11y.json.tmp")
    tmp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)
    return path

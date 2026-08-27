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
    """Resolve declared or generated non-color cues for series labels."""
    labels = list(labels)
    declared = accessibility.get("series_styles") or {}
    mode = accessibility.get("redundant_encoding", "off")
    if mode == "off" and not declared:
        return {}

    resolved: Dict[str, dict] = {}
    for index, label in enumerate(labels):
        base = dict(STYLE_CYCLE[index % len(STYLE_CYCLE)])
        override = declared.get(label) or {}
        if isinstance(override, dict):
            base.update({k: v for k, v in override.items() if k in {"marker", "line_style", "hatch"}})
        resolved[label] = base
    return resolved


def distinct_style_signatures(styles: Dict[str, dict]) -> int:
    return len({
        (style.get("marker"), style.get("line_style"), style.get("hatch"))
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

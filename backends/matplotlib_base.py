#!/usr/bin/env python3
"""Matplotlib backend for recipe-driven scientific figures.

The backend renders supported recipes and writes two project-owned evidence
sidecars:

- ``sci-render-kit/render-manifest`` — replay-addressable render identity;
- ``sci-render-kit/provenance`` — backend/run provenance metadata.

Actual runtime versions such as Matplotlib, NumPy and Python are retained as
execution evidence. Project-owned profile identifiers remain stable and
unversioned.

These records support FAIR R1.2-style provenance practice, but they are not a
claim of FAIR certification, scientific validity, publisher acceptance, or
independent reproduction.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from string import Template
from typing import Callable, Optional

import numpy as np
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.color_encoding import CognitiveColorEncoder
from core.palettes import resolve_categorical

DEFAULT_PALETTE = [
    "#E69F00",
    "#56B4E9",
    "#009E73",
    "#F0E442",
    "#0072B2",
    "#D55E00",
    "#CC79A7",
    "#000000",
]

SERIES_CHART_TYPES = (
    "line-chart",
    "bar-chart",
    "scatter-plot",
    "boxplot",
    "histogram",
)

PROVENANCE_PROFILE = "sci-render-kit/provenance"
MANIFEST_PROFILE = "sci-render-kit/render-manifest"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_sha256(value) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def file_sha256(path: str | Path | None) -> Optional[str]:
    if not path:
        return None
    candidate = Path(path)
    if not candidate.is_file():
        return None
    digest = hashlib.sha256()
    with candidate.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _atomic_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)


def resolve_palette(aesthetics: dict, chart_type: str, data: dict) -> list:
    """Resolve an effective categorical palette for supported series charts."""
    if aesthetics.get("semantic_palette") and chart_type in SERIES_CHART_TYPES:
        labels = list(data.keys())
        if labels:
            return CognitiveColorEncoder().resolve_series_palette(labels)
    if aesthetics.get("palette_name"):
        colors = resolve_categorical(str(aesthetics["palette_name"]))
        labels = list(data.keys()) if chart_type in SERIES_CHART_TYPES else []
        return colors[: len(labels)] if labels else colors
    return list(aesthetics.get("palette") or DEFAULT_PALETTE)


def load_recipe(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"recipe root must be a mapping: {path}")
    return data


def load_profile(name: str) -> dict:
    profile_path = Path("profiles") / f"{name}.yaml"
    if not profile_path.exists():
        return {}
    with profile_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    return data if isinstance(data, dict) else {}


def validate_recipe(recipe: dict) -> list[str]:
    """Compatibility lightweight validation; the unified CLI owns JSON Schema."""
    errors = []
    for key in ("type", "data", "aesthetics", "output"):
        if key not in recipe:
            errors.append(f"missing required field: {key}")
    return errors


def build_provenance(recipe: dict, profile: dict, recipe_path: str = None) -> dict:
    """Build project provenance for one Matplotlib render."""
    import matplotlib

    profile_path = Path("profiles") / f"{profile.get('name')}.yaml" if profile.get("name") else None
    return {
        "profile": PROVENANCE_PROFILE,
        "generated_at": _now(),
        "generator": "sci-render-kit",
        "backend": {
            "name": "matplotlib",
            "version": matplotlib.__version__,
            "runtime": f"Python {platform.python_version()}",
            "numpy_version": np.__version__,
        },
        "recipe": {
            "id": recipe.get("id", "unknown"),
            "source": recipe_path,
            "canonical_sha256": canonical_sha256(recipe),
            "file_sha256": file_sha256(recipe_path),
        },
        "target_profile": {
            "id": profile.get("name"),
            "canonical_sha256": canonical_sha256(profile),
            "file_sha256": file_sha256(profile_path) if profile_path else None,
        },
        "input_data": {
            "canonical_sha256": canonical_sha256(recipe.get("data", {})),
            "keys": list((recipe.get("data") or {}).keys()),
        },
        "standards_scope": {
            "fair_r1_2": "provenance-oriented metadata practice",
            "certification_claim": False,
        },
        "scientific_validity_claim": False,
    }


def _savefig_metadata(provenance: dict, fmt: str, recipe: dict):
    """Build format-compatible embedded metadata where Matplotlib supports it."""
    if not provenance:
        return None
    prov_json = json.dumps(provenance, ensure_ascii=False, separators=(",", ":"))
    backend_version = (provenance.get("backend") or {}).get("version", "unknown")
    creator = f"sci-render-kit/matplotlib (Matplotlib {backend_version})"
    title = str(recipe.get("id", "figure"))
    if fmt == "png":
        return {"srk:provenance": prov_json, "Software": creator}
    if fmt == "pdf":
        return {
            "Title": title,
            "Author": "sci-render-kit",
            "Subject": "recipe-driven scientific figure",
            "Keywords": prov_json,
            "Creator": creator,
        }
    if fmt == "svg":
        return {
            "Title": title,
            "Creator": creator,
            "Description": "recipe-driven scientific figure",
            "Keywords": prov_json,
        }
    return None


def _axis_decoration(aesthetics: dict) -> str:
    lines = []
    if aesthetics.get("title"):
        lines.append(f"ax.set_title({json.dumps(str(aesthetics['title']))})")
    if aesthetics.get("x_label"):
        lines.append(f"ax.set_xlabel({json.dumps(str(aesthetics['x_label']))})")
    if aesthetics.get("y_label"):
        lines.append(f"ax.set_ylabel({json.dumps(str(aesthetics['y_label']))})")
    return "\n".join(lines)


def generate_python_code(
    recipe: dict,
    profile: dict,
    provenance: dict = None,
    *,
    render_logic_fn: Optional[Callable[[str, dict, dict], str]] = None,
    metadata_fn: Optional[Callable[[dict, str, dict], Optional[dict]]] = None,
) -> str:
    """Generate a self-contained Matplotlib render script.

    Optional callables let the public accessibility adapter extend rendering
    without monkeypatching module globals.
    """
    render_logic_fn = render_logic_fn or generate_render_logic
    metadata_fn = metadata_fn or _savefig_metadata

    aesthetics = {**(profile.get("aesthetics") or {}), **(recipe.get("aesthetics") or {})}
    dpi = int(aesthetics.get("dpi", 300))
    rc_params = {
        "font.family": aesthetics.get("font", "sans-serif"),
        "font.size": aesthetics.get("font_size", 10),
        "axes.linewidth": aesthetics.get("axes_linewidth", 0.8),
        "lines.linewidth": aesthetics.get("line_width", 1.2),
        "savefig.dpi": dpi,
    }
    figsize = aesthetics.get("figsize", [6.0, 4.0])
    chart_type = recipe["type"]
    render_logic = render_logic_fn(chart_type, recipe["data"], aesthetics)
    decoration = _axis_decoration(aesthetics)

    output = recipe["output"]
    output_path = Path(output.get("dir", "output")) / output.get("filename", "figure.png")
    fmt = str(output.get("format", output_path.suffix.lstrip(".") or "png")).lower()
    savefig_metadata = metadata_fn(provenance, fmt, recipe)

    code_template = '''#!/usr/bin/env python3
"""Generated by sci-render-kit from a declarative recipe."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

plt.rcParams.update(${rc_params})
data = ${data}
fig, ax = plt.subplots(figsize=${figsize})
${render_logic}
${decoration}
Path(${output_dir}).mkdir(parents=True, exist_ok=True)
fig.savefig(${output_path}, dpi=${dpi}, format=${format},
            bbox_inches='tight', pad_inches=0.05, metadata=${savefig_metadata})
plt.close(fig)
print("saved:", ${output_path})
'''
    return Template(code_template).substitute(
        rc_params=repr(rc_params),
        data=repr(recipe["data"]),
        figsize=repr(figsize),
        render_logic=render_logic,
        decoration=decoration,
        output_dir=repr(str(output_path.parent)),
        output_path=repr(str(output_path)),
        dpi=dpi,
        format=repr(fmt),
        savefig_metadata=repr(savefig_metadata),
    )


def generate_render_logic(chart_type: str, data: dict, aesthetics: dict) -> str:
    """Generate Matplotlib statements for the supported chart family."""
    palette = resolve_palette(aesthetics, chart_type, data)

    if chart_type == "line-chart":
        lines = []
        for i, (label, values) in enumerate(data.items()):
            color = palette[i % len(palette)]
            lines.append(f"x = np.arange(len({repr(values)}))")
            lines.append(
                "ax.plot(x, {values}, color={color}, label={label}, marker='o', markersize=2.5)".format(
                    values=repr(values), color=repr(color), label=repr(str(label))
                )
            )
        lines.append("ax.legend(frameon=False)")
        return "\n".join(lines)

    if chart_type == "bar-chart":
        categories = list(data.keys())
        values = list(data.values())
        lines = [f"x = np.arange({len(categories)})"]
        for i, (label, value) in enumerate(zip(categories, values)):
            color = palette[i % len(palette)]
            lines.append(
                f"ax.bar(x[{i}], {repr(value)}, width=0.6, color={repr(color)}, edgecolor='black', linewidth=0.5)"
            )
        lines.append("ax.set_xticks(x)")
        lines.append(f"ax.set_xticklabels({repr([str(v) for v in categories])})")
        return "\n".join(lines)

    if chart_type == "scatter-plot":
        lines = []
        for i, (label, pair) in enumerate(data.items()):
            if not isinstance(pair, (list, tuple)) or len(pair) != 2:
                raise ValueError(f"scatter series {label!r} must be [x_values, y_values]")
            x, y = pair
            color = palette[i % len(palette)]
            lines.append(
                "ax.scatter({x}, {y}, c={color}, s=16, label={label}, edgecolors='black', linewidths=0.3)".format(
                    x=repr(x), y=repr(y), color=repr(color), label=repr(str(label))
                )
            )
        lines.append("ax.legend(frameon=False)")
        return "\n".join(lines)

    if chart_type == "heatmap":
        matrix = data.get("matrix", [])
        row_labels = data.get("row_labels", [])
        col_labels = data.get("col_labels", [])
        cmap = aesthetics.get("cmap", "viridis")
        lines = [f"cax = ax.imshow({repr(matrix)}, cmap={repr(str(cmap))})", "fig.colorbar(cax)"]
        if col_labels:
            lines.extend([
                f"ax.set_xticks(np.arange(len({repr(col_labels)})))",
                f"ax.set_xticklabels({repr(col_labels)})",
            ])
        if row_labels:
            lines.extend([
                f"ax.set_yticks(np.arange(len({repr(row_labels)})))",
                f"ax.set_yticklabels({repr(row_labels)})",
            ])
        return "\n".join(lines)

    if chart_type == "boxplot":
        labels = [str(label) for label in data.keys()]
        values = list(data.values())
        lines = [
            f"bplot = ax.boxplot({repr(values)}, patch_artist=True, tick_labels={repr(labels)})",
            f"colors = {repr(palette[: len(labels)])}",
            'for patch, color in zip(bplot["boxes"], colors):',
            "    patch.set_facecolor(color)",
            "    patch.set_alpha(0.7)",
        ]
        return "\n".join(lines)

    if chart_type == "histogram":
        values = data.get("values", [])
        bins = int(aesthetics.get("bins", 10))
        color = palette[0] if palette else "#1f77b4"
        return f"ax.hist({repr(values)}, bins={bins}, color={repr(color)}, edgecolor='black', alpha=0.7)"

    raise ValueError(f"unsupported chart type: {chart_type}")


def write_manifest(recipe: dict, profile: dict, output_path: str, *, recipe_path: str = None) -> None:
    """Write the R1 replay-addressable Matplotlib render manifest."""
    import matplotlib

    output = Path(output_path)
    profile_path = Path("profiles") / f"{profile.get('name')}.yaml" if profile.get("name") else None
    manifest = {
        "profile": MANIFEST_PROFILE,
        "generated_at": _now(),
        "generator": "sci-render-kit",
        "recipe": {
            "id": recipe.get("id", "unknown"),
            "canonical_sha256": canonical_sha256(recipe),
            "file_sha256": file_sha256(recipe_path),
            "source": recipe_path,
        },
        "target_profile": {
            "id": profile.get("name"),
            "canonical_sha256": canonical_sha256(profile),
            "file_sha256": file_sha256(profile_path) if profile_path else None,
        },
        "backend": {
            "name": "matplotlib",
            "version": matplotlib.__version__,
            "runtime": f"Python {platform.python_version()}",
        },
        "output": str(output),
        "output_sha256": file_sha256(output),
        "parameters": {
            "aesthetics": {**(profile.get("aesthetics") or {}), **(recipe.get("aesthetics") or {})},
            "data_canonical_sha256": canonical_sha256(recipe.get("data", {})),
            "data_keys": list((recipe.get("data") or {}).keys()),
        },
        "provenance": {
            "sidecar": output.with_suffix(".prov.json").name,
            "accessibility_sidecar": output.with_suffix(".a11y.json").name if "accessibility" in recipe else None,
            "figure_evidence_sidecar": None,
        },
        "reproducibility": {
            "level": "R1",
            "semantics": "Replay-addressable render evidence; no independent rerun claimed.",
            "independently_rerun": False,
        },
    }
    _atomic_json(output.with_suffix(".manifest.json"), manifest)


def write_provenance_sidecar(provenance: dict, output_path: str) -> None:
    """Write project provenance with output byte identity."""
    record = dict(provenance)
    record["output"] = {
        "path": output_path,
        "file_sha256": file_sha256(output_path),
    }
    _atomic_json(Path(output_path).with_suffix(".prov.json"), record)


def render(
    recipe_path: str,
    profile_name: str = "nature",
    *,
    render_logic_fn: Optional[Callable[[str, dict, dict], str]] = None,
    metadata_fn: Optional[Callable[[dict, str, dict], Optional[dict]]] = None,
) -> None:
    """Render one recipe and write Matplotlib-owned evidence sidecars."""
    recipe = load_recipe(recipe_path)
    errors = validate_recipe(recipe)
    if errors:
        raise ValueError("; ".join(errors))
    profile = load_profile(profile_name)
    provenance = build_provenance(recipe, profile, recipe_path)
    code = generate_python_code(
        recipe,
        profile,
        provenance,
        render_logic_fn=render_logic_fn,
        metadata_fn=metadata_fn,
    )

    output = recipe["output"]
    output_dir = Path(output.get("dir", "output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    script_path = output_dir / "_generated_render.py"
    script_path.write_text(code, encoding="utf-8")
    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
    finally:
        try:
            script_path.unlink(missing_ok=True)
        except OSError:
            pass

    output_path = output_dir / output.get("filename", "figure.png")
    if not output_path.is_file():
        raise RuntimeError(f"render completed without declared output: {output_path}")
    write_provenance_sidecar(provenance, str(output_path))
    write_manifest(recipe, profile, str(output_path), recipe_path=recipe_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sci-render-kit matplotlib backend")
    parser.add_argument("action", choices=["render"])
    parser.add_argument("recipe")
    parser.add_argument("--profile", default="nature")
    args = parser.parse_args()
    if args.action == "render":
        render(args.recipe, args.profile)

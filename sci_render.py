#!/usr/bin/env python3
"""sci-render-kit unified CLI: schema, runtime rules, backend dispatch, evidence.

The CLI evaluates explicit project rules before and after rendering. It also
runs the separate ``sci-render-kit/figure-claim-audit`` over declared
research/process metadata so claim-binding inconsistencies remain visible
instead of being silently normalized by the evidence writer.

Only ``severity: error`` findings stop the run. Warnings remain evidence; they
are not GitHub merge policy, scientific-validity decisions, WCAG certification,
claim-truth decisions, or publisher acceptance decisions.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

import yaml
from jsonschema import ValidationError, validate

from core.accessibility import (
    accessibility_config,
    build_accessibility_manifest,
    distinct_style_signatures,
    resolve_series_styles,
    write_accessibility_manifest,
)
from core.claim_binding_audit import (
    PROFILE as CLAIM_AUDIT_PROFILE,
    audit_claim_communication,
)
from core.color_encoding import CognitiveColorEncoder
from core.figure_evidence import build_figure_evidence, write_figure_evidence
from core.palettes import describe_palette, resolve_categorical

SERIES_CHART_TYPES = {"line-chart", "bar-chart", "scatter-plot", "boxplot", "histogram"}
REDUNDANT_STYLE_TYPES = {"line-chart", "bar-chart", "scatter-plot"}
RASTER_FORMATS = {"png", "jpg", "jpeg", "tif", "tiff"}

BACKEND_CAPABILITIES = {
    "matplotlib": {"png", "svg", "pdf"},
    "ggplot2": {"png", "svg", "pdf"},
    "observable": {"html"},
}

BACKEND_ACCESSIBILITY_CAPABILITIES = {
    "matplotlib": {"text-alternative-sidecar", "redundant-series-style"},
    "ggplot2": {"text-alternative-sidecar"},
    "observable": {"text-alternative-sidecar"},
}


def load_yaml(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            value = yaml.safe_load(handle)
    except yaml.YAMLError as exc:
        raise ValueError(f"YAML parse failure in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return value


def _hex_to_rgb(color: str):
    if not isinstance(color, str):
        return None
    value = color.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(ch * 2 for ch in value)
    if len(value) != 6:
        return None
    try:
        return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def resolve_effective_palette(recipe: dict, aesthetics: dict) -> list:
    chart_type = str(recipe.get("type", ""))
    labels = list((recipe.get("data") or {}).keys()) if chart_type in SERIES_CHART_TYPES else []
    if aesthetics.get("semantic_palette"):
        if labels:
            return CognitiveColorEncoder().resolve_series_palette(labels)
    elif aesthetics.get("palette_name"):
        try:
            colors = resolve_categorical(str(aesthetics["palette_name"]))
        except ValueError:
            return []
        return colors[: len(labels)] if labels else colors
    return [str(color) for color in aesthetics.get("palette", [])]


def _rule_index(rule_catalog: dict) -> Dict[str, dict]:
    index: Dict[str, dict] = {}
    for group in rule_catalog.get("rules", []) or []:
        if not isinstance(group, dict):
            continue
        default_severity = str(group.get("default_severity") or "error")
        for check in group.get("checks", []) or []:
            if not isinstance(check, dict) or not check.get("id"):
                continue
            item = dict(check)
            item.setdefault("severity", default_severity)
            item["level"] = group.get("level")
            item["group_id"] = group.get("id")
            item["group_name"] = group.get("name")
            index[str(check["id"])] = item
    return index


def finding(rule_index: Dict[str, dict], check_id: str, message: str, *, severity: Optional[str] = None,
            details: Optional[dict] = None) -> dict:
    rule = rule_index.get(check_id, {})
    return {
        "check_id": check_id,
        "level": rule.get("level"),
        "severity": severity or rule.get("severity", "error"),
        "name": rule.get("name", check_id),
        "message": message,
        "details": details or {},
    }


def has_errors(findings: Iterable[dict]) -> bool:
    return any(str(item.get("severity")) == "error" for item in findings)


def print_findings(items: Iterable[dict], heading: str) -> None:
    items = list(items)
    if not items:
        return
    print(heading)
    icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}
    for item in items:
        severity = str(item.get("severity") or "error")
        print(f"  {icon.get(severity, '•')} [{severity}] {item.get('check_id')}: {item.get('message')}")


def evaluate_pre_render_rules(recipe: dict, profile: dict, rule_catalog: dict) -> List[dict]:
    """Evaluate project P1 visual/accessibility rules."""
    rules = _rule_index(rule_catalog)
    findings: List[dict] = []
    aesthetics = {**(profile.get("aesthetics") or {}), **(recipe.get("aesthetics") or {})}
    publication = profile.get("publication") or {}
    access = accessibility_config(recipe)
    chart_type = str(recipe.get("type", ""))
    labels = list((recipe.get("data") or {}).keys()) if chart_type in SERIES_CHART_TYPES else []
    palette = resolve_effective_palette(recipe, aesthetics)
    encoder = CognitiveColorEncoder()

    if len(palette) > 8:
        findings.append(finding(
            rules,
            "color-count",
            f"effective categorical palette has {len(palette)} colors; consider grouping or another encoding",
        ))

    font_size = aesthetics.get("font_size")
    font_min = publication.get("font_min_pt")
    font_max = publication.get("font_max_pt")
    if font_size is not None and font_min is not None and float(font_size) < float(font_min):
        findings.append(finding(rules, "font-size", f"font_size {font_size}pt is below target minimum {font_min}pt"))
    if font_size is not None and font_max is not None and float(font_size) > float(font_max):
        findings.append(finding(rules, "font-size", f"font_size {font_size}pt exceeds target maximum {font_max}pt"))

    explicit_palette = [str(color).lower() for color in (aesthetics.get("palette") or [])]
    has_red = any(color in {"#ff0000", "red"} for color in explicit_palette)
    has_green = any(color in {"#00ff00", "green"} for color in explicit_palette)
    if has_red and has_green:
        findings.append(finding(
            rules,
            "forbidden-pairs",
            "pure saturated red and green are both used; add non-color cues rather than relying on hue alone",
        ))

    background = aesthetics.get("background")
    if background or aesthetics.get("semantic_palette"):
        bg_value = str(background or "#FFFFFF")
        bg_rgb = _hex_to_rgb(bg_value)
        if bg_rgb is not None:
            for color in palette:
                rgb = _hex_to_rgb(color)
                if rgb is None:
                    continue
                ratio = encoder.contrast_ratio(rgb, bg_rgb)
                if ratio < 3.0:
                    findings.append(finding(
                        rules,
                        "palette-contrast",
                        f"color {color} vs background {bg_value} has contrast {ratio:.2f}:1; project safeguard threshold is 3:1",
                        details={"ratio": ratio, "standard_scope": "WCAG applicability depends on graphical-object role"},
                    ))

    text_color = aesthetics.get("text_color")
    if text_color:
        bg_value = str(background or "#FFFFFF")
        fg_rgb = _hex_to_rgb(str(text_color))
        bg_rgb = _hex_to_rgb(bg_value)
        if fg_rgb is not None and bg_rgb is not None:
            ratio = encoder.contrast_ratio(fg_rgb, bg_rgb)
            if ratio < 4.5:
                findings.append(finding(
                    rules,
                    "text-contrast",
                    f"text color {text_color} vs background {bg_value} has contrast {ratio:.2f}:1, below 4.5:1",
                    details={"ratio": ratio, "standard_scope": "WCAG 2.2 SC 1.4.3 design support"},
                ))

    if aesthetics.get("adjacency_check"):
        seen: List[str] = []
        for color in [color for color in palette if _hex_to_rgb(color) is not None]:
            if color.lower() in {item.lower() for item in seen}:
                continue
            for other in seen:
                ratio = encoder.contrast_ratio(_hex_to_rgb(color), _hex_to_rgb(other))
                if ratio < 3.0:
                    findings.append(finding(
                        rules,
                        "palette-adjacency",
                        f"project all-pairs policy: ({other}, {color}) has contrast {ratio:.2f}:1 below 3:1",
                        details={"ratio": ratio, "standard_scope": "stricter project policy, not universal WCAG palette rule"},
                    ))
            seen.append(color)

    pairs = access.get("adjacent_pairs") or []
    if pairs and labels:
        color_by_label = {
            label: palette[index % len(palette)]
            for index, label in enumerate(labels)
        } if palette else {}
        for pair in pairs:
            if not isinstance(pair, list) or len(pair) != 2:
                continue
            left, right = pair
            if left not in color_by_label or right not in color_by_label:
                findings.append(finding(rules, "declared-adjacency", f"adjacent_pairs references unknown series ({left}, {right})"))
                continue
            left_rgb = _hex_to_rgb(color_by_label[left])
            right_rgb = _hex_to_rgb(color_by_label[right])
            if left_rgb is None or right_rgb is None:
                continue
            ratio = encoder.contrast_ratio(left_rgb, right_rgb)
            if ratio < 3.0:
                findings.append(finding(
                    rules,
                    "declared-adjacency",
                    f"declared adjacent graphical series ({left}, {right}) have boundary contrast {ratio:.2f}:1 below 3:1",
                    details={"ratio": ratio, "standard_scope": "WCAG 2.2 SC 1.4.11 when boundary is required for understanding"},
                ))

    if access.get("require_alt_text") and not str(access.get("alt_text", "")).strip():
        findings.append(finding(rules, "text-alternative", "require_alt_text=true but alt_text is empty"))

    mode = access.get("redundant_encoding", "off")
    if mode == "required" and chart_type in REDUNDANT_STYLE_TYPES and len(labels) > 1:
        styles = resolve_series_styles(labels, access)
        if len(styles) != len(labels) or distinct_style_signatures(styles) < len(labels):
            findings.append(finding(
                rules,
                "non-color-cue",
                "multiple series do not have distinct non-color marker/line/hatch signatures",
                details={"standard_scope": "WCAG 2.2 SC 1.4.1 design support"},
            ))

    if background or aesthetics.get("semantic_palette"):
        from core.cvd_simulation import cvd_contrast_report
        bg_value = str(background or "#FFFFFF")
        bg_rgb = _hex_to_rgb(bg_value)
        if bg_rgb is not None:
            for color in palette:
                rgb = _hex_to_rgb(color)
                if rgb is None:
                    continue
                worst_type, worst_ratio = cvd_contrast_report(rgb, bg_rgb, encoder.contrast_ratio)[0]
                if worst_ratio < 3.0:
                    findings.append(finding(
                        rules,
                        "cvd-contrast",
                        f"project CVD simulation safeguard: {color} under {worst_type} has background contrast {worst_ratio:.2f}:1 below 3:1",
                        details={"ratio": worst_ratio, "standard_scope": "project safeguard; not a WCAG-mandated CVD simulation test"},
                    ))

    palette_name = aesthetics.get("palette_name")
    if palette_name:
        try:
            entry = describe_palette(str(palette_name))
            if chart_type in SERIES_CHART_TYPES and entry["kind"] != "categorical":
                findings.append(finding(rules, "palette-name", f"palette '{palette_name}' is {entry['kind']}; categorical series require a categorical palette"))
        except ValueError as exc:
            findings.append(finding(rules, "palette-name", str(exc)))

    if chart_type.startswith("3d-"):
        findings.append(finding(rules, "no-3d", f"chart type {chart_type} is outside the current supported 2D recipe model"))

    return findings


def evaluate_post_render_rules(recipe: dict, profile: dict, backend: str, output_path: Path,
                               rule_catalog: dict) -> List[dict]:
    """Evaluate P2 artifact integrity and P3 publisher-target alignment."""
    rules = _rule_index(rule_catalog)
    findings: List[dict] = []
    output_cfg = recipe.get("output") or {}
    manifest_path = output_path.with_suffix(".manifest.json")
    prov_path = output_path.with_suffix(".prov.json")
    a11y_path = output_path.with_suffix(".a11y.json")

    if not output_path.exists():
        findings.append(finding(rules, "file-exists", f"output file was not generated: {output_path}"))
        return findings
    if output_path.stat().st_size == 0:
        findings.append(finding(rules, "non-empty", f"output file is empty: {output_path}"))

    expected_ext = "." + str(output_cfg.get("format", "png")).lower()
    if output_path.suffix.lower() != expected_ext:
        findings.append(finding(rules, "format-match", f"expected {expected_ext}, got {output_path.suffix.lower()}"))

    if not manifest_path.exists():
        findings.append(finding(rules, "manifest-exists", f"render manifest missing: {manifest_path}"))
    if backend == "matplotlib" and not prov_path.exists():
        findings.append(finding(rules, "prov-exists", f"matplotlib provenance sidecar missing: {prov_path}"))
    if "accessibility" in recipe and not a11y_path.exists():
        findings.append(finding(rules, "a11y-exists", f"accessibility sidecar missing: {a11y_path}"))

    publication = profile.get("publication") or {}
    fmt = str(output_cfg.get("format", "png")).lower()
    preferred = [str(value).lower() for value in (publication.get("preferred_formats") or [])]
    required = [str(value).lower() for value in (publication.get("required_formats") or [])]
    if required and fmt not in required:
        findings.append(finding(rules, "preferred-format", f"format {fmt} is not in required target formats {required}", severity="error"))
    elif preferred and fmt not in preferred:
        findings.append(finding(rules, "preferred-format", f"format {fmt} is outside publisher-target preferred formats {preferred}"))

    aesthetics = {**(profile.get("aesthetics") or {}), **(recipe.get("aesthetics") or {})}
    if fmt in RASTER_FORMATS:
        min_dpi = publication.get("raster_min_dpi")
        actual_dpi = aesthetics.get("dpi")
        if min_dpi is not None and actual_dpi is not None and float(actual_dpi) < float(min_dpi):
            findings.append(finding(rules, "dpi-check", f"raster DPI {actual_dpi} is below target minimum {min_dpi}"))

    figsize = aesthetics.get("figsize")
    if figsize is not None:
        if (
            not isinstance(figsize, list)
            or len(figsize) != 2
            or any(not isinstance(value, (int, float)) or value <= 0 for value in figsize)
        ):
            findings.append(finding(rules, "size-check", f"figsize must be a positive two-number list, got {figsize!r}"))
        else:
            max_width = publication.get("max_width_in")
            max_height = publication.get("max_height_in")
            if max_width is not None and float(figsize[0]) > float(max_width):
                findings.append(finding(rules, "size-check", f"figure width {figsize[0]}in exceeds target maximum {max_width}in"))
            if max_height is not None and float(figsize[1]) > float(max_height):
                findings.append(finding(rules, "size-check", f"figure height {figsize[1]}in exceeds target maximum {max_height}in"))

    font_size = aesthetics.get("font_size")
    font_min = publication.get("font_min_pt")
    font_max = publication.get("font_max_pt")
    if font_size is not None and font_min is not None and float(font_size) < float(font_min):
        findings.append(finding(rules, "font-range", f"font_size {font_size}pt is below target minimum {font_min}pt"))
    if font_size is not None and font_max is not None and float(font_size) > float(font_max):
        findings.append(finding(rules, "font-range", f"font_size {font_size}pt exceeds target maximum {font_max}pt"))

    return findings


def _update_render_manifest(manifest_path: Path, evidence_path: Path, findings: List[dict]) -> None:
    if not manifest_path.exists():
        return
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return

    runtime_counts = {"error": 0, "warning": 0, "info": 0}
    claim_counts = {"error": 0, "warning": 0, "info": 0}
    for item in findings:
        severity = str(item.get("severity") or "error")
        target = claim_counts if item.get("profile") == CLAIM_AUDIT_PROFILE else runtime_counts
        target[severity] = target.get(severity, 0) + 1

    manifest["runtime_validation"] = {
        "profile": "sci-render-kit/runtime-quality",
        "status": "failed" if runtime_counts.get("error", 0) else (
            "passed_with_warnings" if runtime_counts.get("warning", 0) else "passed"
        ),
        "counts": runtime_counts,
    }
    manifest["claim_communication_audit"] = {
        "profile": CLAIM_AUDIT_PROFILE,
        "status": "failed" if claim_counts.get("error", 0) else (
            "observations" if claim_counts.get("warning", 0) or claim_counts.get("info", 0) else "clean"
        ),
        "counts": claim_counts,
        "details": "full findings are retained in the figure evidence sidecar",
    }
    manifest["figure_evidence"] = {
        "profile": "sci-render-kit/figure-evidence",
        "sidecar": evidence_path.name,
    }
    temp = manifest_path.with_suffix(".manifest.json.tmp")
    temp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, manifest_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="sci-render-kit unified scientific figure renderer")
    parser.add_argument("recipe", help="YAML recipe path")
    parser.add_argument("--profile", default="nature", help="target profile name")
    parser.add_argument("--backend", default="matplotlib", choices=sorted(BACKEND_CAPABILITIES))
    args = parser.parse_args()

    if not os.path.exists(args.recipe):
        print(f"RECIPE_NOT_FOUND: {args.recipe}")
        raise SystemExit(1)

    try:
        recipe = load_yaml(args.recipe)
        schema = load_yaml("metadata/recipe.schema.yaml")
        validate(instance=recipe, schema=schema)
    except (ValueError, ValidationError) as exc:
        print("P0_SCHEMA_FAILURE")
        print(f"  - {getattr(exc, 'message', str(exc))}")
        raise SystemExit(1)
    print("✅ P0 recipe structure valid")

    profile_path = f"profiles/{args.profile}.yaml"
    if not os.path.exists(profile_path):
        print(f"MISSING_PROFILE: {profile_path}")
        raise SystemExit(1)
    try:
        profile = load_yaml(profile_path)
        rules = load_yaml("quality/rules.yaml")
    except ValueError as exc:
        print(exc)
        raise SystemExit(1)

    findings = evaluate_pre_render_rules(recipe, profile, rules)
    claim_audit_findings = audit_claim_communication(recipe)
    findings.extend(claim_audit_findings)
    print_findings(findings, "P1 runtime + claim-communication findings:")
    if has_errors(findings):
        print("PRE_RENDER_RULE_FAILURE")
        raise SystemExit(1)

    output_format = str((recipe.get("output") or {}).get("format", "png")).lower()
    if output_format not in BACKEND_CAPABILITIES[args.backend]:
        print("BACKEND_CAPABILITY_MISMATCH")
        print(f"backend {args.backend} does not support {output_format}; supports {sorted(BACKEND_CAPABILITIES[args.backend])}")
        raise SystemExit(1)

    access = accessibility_config(recipe)
    if (
        access.get("redundant_encoding") in {"auto", "required"}
        and str(recipe.get("type")) in REDUNDANT_STYLE_TYPES
        and "redundant-series-style" not in BACKEND_ACCESSIBILITY_CAPABILITIES[args.backend]
    ):
        print("BACKEND_ACCESSIBILITY_MISMATCH")
        print(f"backend {args.backend} does not implement redundant series-style mapping")
        raise SystemExit(1)

    backend_script_map = {
        "matplotlib": ("python3", "backends/matplotlib_adapter.py"),
        "ggplot2": ("Rscript", "backends/ggplot2_adapter.R"),
        "observable": ("node", "backends/observable_adapter.js"),
    }
    command, script = backend_script_map[args.backend]
    print(f"🚀 rendering with {args.backend}")
    try:
        subprocess.run([command, script, "render", args.recipe, "--profile", args.profile], check=True)
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print("BACKEND_EXECUTION_FAILURE")
        print(f"  - {type(exc).__name__}: {exc}")
        raise SystemExit(1)

    output_cfg = recipe.get("output") or {}
    output_path = Path(output_cfg.get("dir", "output")) / output_cfg.get("filename", "figure.png")

    if "accessibility" in recipe:
        merged_aesthetics = {**(profile.get("aesthetics") or {}), **(recipe.get("aesthetics") or {})}
        a11y_manifest = build_accessibility_manifest(
            recipe,
            resolve_effective_palette(recipe, merged_aesthetics),
        )
        write_accessibility_manifest(output_path, a11y_manifest)

    post_findings = evaluate_post_render_rules(recipe, profile, args.backend, output_path, rules)
    findings.extend(post_findings)
    print_findings(post_findings, "P2/P3 runtime findings:")
    if has_errors(findings):
        print("POST_RENDER_RULE_FAILURE")
        raise SystemExit(1)

    sidecars: Dict[str, Path] = {}
    for kind, path in (
        ("render-manifest", output_path.with_suffix(".manifest.json")),
        ("provenance", output_path.with_suffix(".prov.json")),
        ("accessibility", output_path.with_suffix(".a11y.json")),
    ):
        if path.exists():
            sidecars[kind] = path

    try:
        evidence_record = build_figure_evidence(
            recipe_path=args.recipe,
            recipe=recipe,
            profile_path=profile_path,
            profile=profile,
            backend=args.backend,
            output_path=output_path,
            findings=findings,
            sidecars=sidecars,
        )
        evidence_path = write_figure_evidence(evidence_record, output_path)
    except (OSError, ValueError) as exc:
        print("FIGURE_EVIDENCE_FAILURE")
        print(f"  - {exc}")
        raise SystemExit(1)

    if not evidence_path.exists():
        print("FIGURE_EVIDENCE_FAILURE: sidecar was not written")
        raise SystemExit(1)

    _update_render_manifest(output_path.with_suffix(".manifest.json"), evidence_path, findings)

    warning_count = sum(1 for item in findings if item.get("severity") == "warning")
    status = "passed_with_warnings" if warning_count else "passed"
    print(f"✅ render runtime validation: {status}")
    print(f"📦 figure evidence: {evidence_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Versioned evidence envelope for rendered scientific figures.

The figure evidence record is a project-owned cross-tool handoff object. It
indexes the rendered figure, recipe, publisher/profile preset, backend sidecars,
upstream research references and runtime-rule findings without claiming that a
successful render establishes scientific validity or publisher acceptance.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

PROFILE = "sci-render-kit/figure-evidence@1"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def canonical_sha256(value: Any) -> str:
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


def _file_ref(kind: str, path: str | Path | None) -> Optional[dict]:
    digest = file_sha256(path)
    if not digest:
        return None
    return {"kind": kind, "path": str(path), "file_sha256": digest}


def _reference(value: Any) -> Optional[dict]:
    """Normalize a local path or opaque URI/reference without dereferencing it."""
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    result = {"ref": text}
    digest = file_sha256(text)
    if digest:
        result["file_sha256"] = digest
        result["resolution"] = "local-file"
    else:
        result["resolution"] = "opaque-reference-not-dereferenced"
    return result


def summarize_findings(findings: Iterable[dict]) -> dict:
    items = [dict(item) for item in findings if isinstance(item, dict)]
    counts = {"error": 0, "warning": 0, "info": 0}
    for item in items:
        severity = str(item.get("severity") or "error")
        counts[severity] = counts.get(severity, 0) + 1
    status = "failed" if counts.get("error", 0) else (
        "passed_with_warnings" if counts.get("warning", 0) else "passed"
    )
    return {
        "profile": "sci-render-kit/runtime-quality@1",
        "status": status,
        "counts": counts,
        "findings": items,
    }


def build_figure_evidence(
    *,
    recipe_path: str,
    recipe: dict,
    profile_path: str,
    profile: dict,
    backend: str,
    output_path: str | Path,
    findings: Iterable[dict],
    sidecars: Optional[Dict[str, str | Path]] = None,
) -> dict:
    """Build the figure evidence record after a render attempt succeeds."""
    output_path = Path(output_path)
    if not output_path.is_file():
        raise ValueError(f"figure output does not exist: {output_path}")

    runtime_validation = summarize_findings(findings)
    research_context = recipe.get("research_context") or {}
    if not isinstance(research_context, dict):
        research_context = {}
    uncertainty = recipe.get("uncertainty") or {}
    if not isinstance(uncertainty, dict):
        uncertainty = {}

    artifact_refs = []
    figure_ref = _file_ref("figure", output_path)
    if figure_ref:
        artifact_refs.append(figure_ref)
    for kind, path in sorted((sidecars or {}).items()):
        ref = _file_ref(kind, path)
        if ref:
            artifact_refs.append(ref)

    upstream = {
        "evidence_envelope": _reference(research_context.get("evidence_envelope_ref")),
        "provenance": _reference(research_context.get("provenance_ref")),
        "data_artifact": _reference(research_context.get("data_artifact_ref")),
        "claim_refs": [str(value) for value in (research_context.get("claim_refs") or [])],
    }

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "figure_id": str(recipe.get("id") or output_path.stem),
        "chart_type": recipe.get("type"),
        "backend": backend,
        "figure": {
            "path": str(output_path),
            "file_sha256": file_sha256(output_path),
            "format": output_path.suffix.lower().lstrip("."),
        },
        "recipe": {
            "id": recipe.get("id"),
            "path": recipe_path,
            "canonical_sha256": canonical_sha256(recipe),
            "file_sha256": file_sha256(recipe_path),
        },
        "profile_target": {
            "id": profile.get("name"),
            "path": profile_path,
            "canonical_sha256": canonical_sha256(profile),
            "file_sha256": file_sha256(profile_path),
            "publisher_compliance_claim": False,
        },
        "artifacts": artifact_refs,
        "upstream_research": upstream,
        "uncertainty": {
            "kind": uncertainty.get("kind", "not_declared"),
            "level": uncertainty.get("level"),
            "semantics": uncertainty.get(
                "semantics",
                "No uncertainty semantics were declared in the recipe.",
            ),
            "source_ref": uncertainty.get("source_ref"),
        },
        "runtime_validation": runtime_validation,
        "reproducibility": {
            "level": "R1",
            "semantics": (
                "render inputs and artifact identities are replay-addressable; "
                "R3 requires a separate rerun and declared comparison criterion"
            ),
        },
        "scientific_validity_claim": False,
        "statistical_validity_claim": False,
        "causal_validity_claim": False,
        "publisher_acceptance_claim": False,
    }


def write_figure_evidence(record: dict, output_path: str | Path) -> Path:
    """Atomically write ``<figure>.evidence.json`` next to the figure."""
    output_path = Path(output_path)
    path = output_path.with_suffix(".evidence.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".evidence.json.tmp")
    temp.write_text(
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    os.replace(temp, path)
    return path

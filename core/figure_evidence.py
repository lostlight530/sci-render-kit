#!/usr/bin/env python3
"""Evidence envelope for rendered scientific figures.

The figure evidence record is a project-owned cross-tool handoff object. It
indexes the rendered figure, recipe, publisher/profile preset, backend sidecars,
upstream research references, declared claim-to-visual bindings, process
disclosure and runtime findings without claiming that a successful render
establishes scientific validity, authorship, peer review, entailment, source
credibility, or publisher acceptance.

Two evidence planes remain distinct:

- ``sci-render-kit/runtime-quality`` for visual/accessibility/artifact/publisher predicates;
- ``sci-render-kit/figure-claim-audit`` for consistency of declared claim/process/reference metadata.
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

from core.claim_binding_audit import PROFILE as CLAIM_AUDIT_PROFILE, summarize_claim_audit

PROFILE = "sci-render-kit/figure-evidence"
CLAIM_BINDING_PROFILE = "sci-render-kit/figure-claim-binding"
PROCESS_DISCLOSURE_PROFILE = "sci-render-kit/process-disclosure"
RUNTIME_QUALITY_PROFILE = "sci-render-kit/runtime-quality"
AI_ASSISTANCE_VALUES = {"none", "used", "not_declared"}
HUMAN_REVIEW_VALUES = {"reviewed", "partial", "not_reviewed", "not_declared"}
CLAIM_RELATIONS = {"supports", "illustrates", "contextualizes", "compares", "derived-from"}


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


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result = []
    seen = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _normalize_claim_bindings(value: Any) -> list[dict]:
    """Normalize declared visual-to-claim bindings without inferring new relations."""
    if not isinstance(value, list):
        return []
    bindings = []
    for item in value:
        if not isinstance(item, dict):
            continue
        visual_ref = str(item.get("visual_ref") or "").strip()
        relation = str(item.get("relation") or "").strip()
        claim_refs = _string_list(item.get("claim_refs"))
        if not visual_ref or not claim_refs or relation not in CLAIM_RELATIONS:
            continue
        record = {
            "visual_ref": visual_ref,
            "claim_refs": claim_refs,
            "relation": relation,
        }
        evidence_ref = str(item.get("evidence_ref") or "").strip()
        note = str(item.get("note") or "").strip()
        if evidence_ref:
            record["evidence_ref"] = evidence_ref
        if note:
            record["note"] = note
        bindings.append(record)
    return bindings


def _normalize_process_disclosure(value: Any) -> dict:
    """Normalize optional recipe disclosure without inventing missing claims."""
    if not isinstance(value, dict):
        value = {}

    ai_assistance = str(value.get("ai_assistance") or "not_declared").strip()
    if ai_assistance not in AI_ASSISTANCE_VALUES:
        ai_assistance = "not_declared"

    human_review = str(value.get("human_review") or "not_declared").strip()
    if human_review not in HUMAN_REVIEW_VALUES:
        human_review = "not_declared"

    disclosure_ref = str(value.get("disclosure_ref") or "").strip()
    result = {
        "profile": PROCESS_DISCLOSURE_PROFILE,
        "ai_assistance": ai_assistance,
        "ai_tools": _string_list(value.get("ai_tools")),
        "human_review": human_review,
        "semantics": (
            "declared figure-generation/communication process metadata only; "
            "not authorship adjudication, peer review, scientific validity, or publisher compliance"
        ),
    }
    if disclosure_ref:
        result["disclosure_ref"] = _reference(disclosure_ref)
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
        "profile": RUNTIME_QUALITY_PROFILE,
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

    all_findings = [dict(item) for item in findings if isinstance(item, dict)]
    claim_audit_findings = [
        item for item in all_findings if item.get("profile") == CLAIM_AUDIT_PROFILE
    ]
    runtime_findings = [
        item for item in all_findings if item.get("profile") != CLAIM_AUDIT_PROFILE
    ]
    runtime_validation = summarize_findings(runtime_findings)
    communication_audit = summarize_claim_audit(claim_audit_findings)

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

    claim_refs = _string_list(research_context.get("claim_refs"))
    claim_bindings = _normalize_claim_bindings(research_context.get("claim_bindings"))
    all_bound_claims = sorted(
        set(claim_refs).union(
            claim_ref
            for binding in claim_bindings
            for claim_ref in binding.get("claim_refs", [])
        )
    )

    upstream = {
        "artifact_id": research_context.get("artifact_id"),
        "source_refs": _string_list(research_context.get("source_refs")),
        "evidence_envelope": _reference(research_context.get("evidence_envelope_ref")),
        "claim_audit": _reference(research_context.get("claim_audit_ref")),
        "provenance": _reference(research_context.get("provenance_ref")),
        "data_artifact": _reference(research_context.get("data_artifact_ref")),
        "claim_refs": claim_refs,
        "scientific_validity_inherited": False,
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
        "claim_communication": {
            "profile": CLAIM_BINDING_PROFILE,
            "claim_refs": all_bound_claims,
            "bindings": claim_bindings,
            "binding_count": len(claim_bindings),
            "inferred_bindings": False,
            "semantics": (
                "recipe-declared relationships between visual references and upstream claim IDs; "
                "not verified entailment, evidence sufficiency, or scientific truth"
            ),
        },
        "communication_audit": communication_audit,
        "process_disclosure": _normalize_process_disclosure(recipe.get("process_disclosure")),
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
        "authorship_claim": False,
        "peer_review_claim": False,
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

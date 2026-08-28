#!/usr/bin/env python3
"""Portable scientific-communication handoff for sci-render-kit.

The transfer record summarizes an existing ``sci-render-kit/figure-evidence``
sidecar for downstream publication, review, archival or agent workflows. It
preserves declared claim bindings, upstream research references, uncertainty,
process disclosure and audit summaries without inheriting truth, entailment,
statistical validity, peer review or publisher acceptance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

PROFILE = "sci-render-kit/communication-transfer"
SOURCE_PROFILE = "sci-render-kit/figure-evidence"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _file_sha256(path: str | Path) -> str:
    candidate = Path(path)
    digest = hashlib.sha256()
    with candidate.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()


def _load_json(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("figure evidence must be a JSON object")
    source_profile = data.get("profile")
    if source_profile != SOURCE_PROFILE:
        raise ValueError(
            f"communication transfer requires source profile {SOURCE_PROFILE!r}, got {source_profile!r}"
        )
    return data


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result: list[str] = []
    seen: set[str] = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _coverage(evidence: dict) -> dict:
    communication = evidence.get("claim_communication") or {}
    bindings = communication.get("bindings") or []
    if not isinstance(bindings, list):
        bindings = []
    claim_refs = _string_list(communication.get("claim_refs"))
    upstream = evidence.get("upstream_research") or {}
    uncertainty = evidence.get("uncertainty") or {}
    disclosure = evidence.get("process_disclosure") or {}

    upstream_fields = [
        key
        for key in ("evidence_envelope", "claim_audit", "provenance", "data_artifact")
        if upstream.get(key)
    ]
    process_fields = [
        key
        for key in ("ai_assistance", "ai_tools", "human_review", "disclosure_ref")
        if disclosure.get(key) not in (None, "", [], "not_declared")
    ]
    uncertainty_declared = uncertainty.get("kind") not in (None, "", "not_declared")

    return {
        "claim_ref_count": len(claim_refs),
        "binding_count": len([item for item in bindings if isinstance(item, dict)]),
        "upstream_context_fields": upstream_fields,
        "upstream_context_field_count": len(upstream_fields),
        "process_disclosure_fields": process_fields,
        "process_disclosure_field_count": len(process_fields),
        "uncertainty_semantics_declared": bool(uncertainty_declared),
        "communication_audit_present": isinstance(evidence.get("communication_audit"), dict),
        "runtime_validation_present": isinstance(evidence.get("runtime_validation"), dict),
        "aggregate_score": None,
        "semantics": (
            "descriptive communication-handoff coverage only; not entailment, evidence sufficiency, "
            "statistical validity, scientific quality, accessibility conformance, or publisher acceptance"
        ),
    }


def build_communication_transfer(
    figure_evidence_path: str | Path,
    *,
    destination: Optional[str] = None,
    purpose: Optional[str] = None,
) -> dict:
    evidence_path = Path(figure_evidence_path)
    evidence = _load_json(evidence_path)
    communication = evidence.get("claim_communication") or {}
    upstream = evidence.get("upstream_research") or {}

    return {
        "profile": PROFILE,
        "generated_at": _now(),
        "source_figure_evidence": {
            "path": str(evidence_path),
            "file_sha256": _file_sha256(evidence_path),
            "source_profile": evidence.get("profile"),
            "figure_id": evidence.get("figure_id"),
            "basis": "runtime-observed-local-bytes",
        },
        "destination": destination,
        "destination_basis": "caller-declared" if destination else "not_declared",
        "purpose": purpose,
        "purpose_basis": "caller-declared" if purpose else "not_declared",
        "claim_communication": {
            "claim_refs": _string_list(communication.get("claim_refs")),
            "bindings": [dict(item) for item in (communication.get("bindings") or []) if isinstance(item, dict)],
            "inferred_bindings": bool(communication.get("inferred_bindings", False)),
            "semantics": communication.get("semantics"),
        },
        "upstream_research": dict(upstream) if isinstance(upstream, dict) else {},
        "uncertainty": dict(evidence.get("uncertainty") or {}),
        "process_disclosure": dict(evidence.get("process_disclosure") or {}),
        "communication_audit": dict(evidence.get("communication_audit") or {}),
        "runtime_validation": dict(evidence.get("runtime_validation") or {}),
        "transfer_coverage": _coverage(evidence),
        "transfer_constraints": {
            "scientific_validity_inherited": False,
            "entailment_inherited": False,
            "evidence_sufficiency_inherited": False,
            "statistical_validity_inherited": False,
            "peer_review_inherited": False,
            "publisher_acceptance_inherited": False,
            "accessibility_conformance_inherited": False,
        },
        "assertion_basis": {
            "figure_evidence": "copied-from-local-figure-evidence-sidecar",
            "destination": "caller-declared" if destination else "not_declared",
            "purpose": "caller-declared" if purpose else "not_declared",
            "basis_inferred": False,
        },
        "scientific_validity_claim": False,
        "publisher_acceptance_claim": False,
        "peer_review_claim": False,
    }


def write_communication_transfer(record: dict, output: str | Path) -> Path:
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(temp, path)
    return path


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Create a bounded scientific-communication transfer record")
    parser.add_argument("figure_evidence", help="existing <figure>.evidence.json")
    parser.add_argument("--destination", help="caller-declared destination/context")
    parser.add_argument("--purpose", help="caller-declared downstream purpose")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)
    record = build_communication_transfer(
        args.figure_evidence,
        destination=args.destination,
        purpose=args.purpose,
    )
    write_communication_transfer(record, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

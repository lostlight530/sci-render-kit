#!/usr/bin/env python3
"""Runtime audit for declared claim-to-visual communication relationships.

``sci-render-kit/figure-claim-audit@1`` evaluates only explicit recipe metadata.
It never inspects pixels, infers claims from titles/legends, dereferences remote
resources, or decides whether a scientific claim is true.

The audit exists to prevent a more mundane but important failure mode: a recipe
can be syntactically valid while its handoff metadata is internally
inconsistent. Examples include duplicate visual bindings, a ``supports``
relation with no evidence context, or AI tool identifiers declared while the
AI-assistance field says ``none``.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit

PROFILE = "sci-render-kit/figure-claim-audit@1"
CLAIM_RELATIONS = {"supports", "illustrates", "contextualizes", "compares", "derived-from"}


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, (list, tuple, set)):
        return []
    result: list[str] = []
    seen = set()
    for item in value:
        text = str(item).strip()
        if text and text not in seen:
            result.append(text)
            seen.add(text)
    return result


def _issue(check_id: str, message: str, severity: str = "warning", **details: Any) -> dict:
    return {
        "profile": PROFILE,
        "check_id": check_id,
        "severity": severity,
        "message": message,
        "details": details,
        "scientific_validity_claim": False,
    }


def _reference_state(value: Any) -> tuple[str, str | None]:
    """Classify a declared reference without dereferencing remote resources."""
    text = str(value or "").strip()
    if not text:
        return "absent", None
    parsed = urlsplit(text)
    if parsed.scheme:
        return "opaque-uri-not-dereferenced", text
    if Path(text).is_file():
        return "local-file", text
    return "local-or-opaque-reference-not-resolved", text


def audit_claim_communication(recipe: dict) -> list[dict]:
    """Return bounded runtime findings for research/claim/process metadata."""
    findings: list[dict] = []
    research = recipe.get("research_context") or {}
    if not isinstance(research, dict):
        research = {}
    disclosure = recipe.get("process_disclosure") or {}
    if not isinstance(disclosure, dict):
        disclosure = {}

    figure_claims = set(_string_list(research.get("claim_refs")))
    bindings = research.get("claim_bindings") or []
    if not isinstance(bindings, list):
        bindings = []

    seen_bindings: set[tuple[str, str, tuple[str, ...], str]] = set()
    seen_visual_refs: dict[str, int] = {}
    bound_claims: set[str] = set()

    upstream_evidence_present = any(
        str(research.get(key) or "").strip()
        for key in ("evidence_envelope_ref", "claim_audit_ref", "provenance_ref")
    )

    for index, item in enumerate(bindings):
        if not isinstance(item, dict):
            findings.append(
                _issue(
                    "claim-binding-structure",
                    f"claim_bindings[{index}] is not a mapping",
                    "error",
                    binding_index=index,
                )
            )
            continue

        visual_ref = str(item.get("visual_ref") or "").strip()
        relation = str(item.get("relation") or "").strip()
        claim_refs = _string_list(item.get("claim_refs"))
        evidence_ref = str(item.get("evidence_ref") or "").strip()

        if not visual_ref or not claim_refs or relation not in CLAIM_RELATIONS:
            # JSON Schema should normally catch these, but keeping a runtime
            # finding makes direct callers of this helper fail visibly too.
            findings.append(
                _issue(
                    "claim-binding-structure",
                    f"claim_bindings[{index}] lacks a usable visual_ref/claim_refs/relation",
                    "error",
                    binding_index=index,
                )
            )
            continue

        seen_visual_refs[visual_ref] = seen_visual_refs.get(visual_ref, 0) + 1
        bound_claims.update(claim_refs)

        identity = (visual_ref, relation, tuple(sorted(claim_refs)), evidence_ref)
        if identity in seen_bindings:
            findings.append(
                _issue(
                    "claim-binding-duplicate",
                    f"duplicate claim binding for visual_ref={visual_ref!r}",
                    "warning",
                    binding_index=index,
                    visual_ref=visual_ref,
                    relation=relation,
                    claim_refs=claim_refs,
                )
            )
        else:
            seen_bindings.add(identity)

        missing_from_figure_index = [claim for claim in claim_refs if claim not in figure_claims]
        if figure_claims and missing_from_figure_index:
            findings.append(
                _issue(
                    "claim-binding-index",
                    "binding references claims not present in research_context.claim_refs",
                    "warning",
                    binding_index=index,
                    visual_ref=visual_ref,
                    missing_claim_refs=missing_from_figure_index,
                )
            )

        if relation == "supports" and not evidence_ref and not upstream_evidence_present:
            findings.append(
                _issue(
                    "claim-support-reference",
                    "relation='supports' is declared without evidence_ref or upstream evidence/audit context",
                    "warning",
                    binding_index=index,
                    visual_ref=visual_ref,
                    claim_refs=claim_refs,
                    semantics="missing reference context; not a judgment that support is scientifically insufficient",
                )
            )

        if evidence_ref:
            state, ref = _reference_state(evidence_ref)
            if state == "local-or-opaque-reference-not-resolved":
                findings.append(
                    _issue(
                        "research-reference-resolution",
                        "binding evidence_ref does not resolve as a local file and has no URI scheme",
                        "warning",
                        binding_index=index,
                        reference=ref,
                        resolution=state,
                    )
                )

    if bindings and not figure_claims:
        findings.append(
            _issue(
                "claim-binding-index",
                "claim bindings exist but research_context.claim_refs is empty; figure evidence will derive a union index from bindings",
                "info",
                derived_claim_refs=sorted(bound_claims),
            )
        )

    repeated_visual_refs = sorted(ref for ref, count in seen_visual_refs.items() if count > 1)
    if repeated_visual_refs:
        findings.append(
            _issue(
                "claim-visual-multiplicity",
                "a visual_ref participates in multiple declared claim relations; this is allowed but should be intentional",
                "info",
                visual_refs=repeated_visual_refs,
            )
        )

    ai_assistance = str(disclosure.get("ai_assistance") or "not_declared").strip()
    ai_tools = _string_list(disclosure.get("ai_tools"))
    if ai_assistance == "used" and not ai_tools:
        findings.append(
            _issue(
                "process-disclosure-consistency",
                "ai_assistance='used' but no ai_tools identifiers are declared",
                "warning",
            )
        )
    if ai_tools and ai_assistance in {"none", "not_declared", ""}:
        findings.append(
            _issue(
                "process-disclosure-consistency",
                "ai_tools are declared but ai_assistance is not 'used'",
                "warning",
                ai_assistance=ai_assistance,
            )
        )

    reference_fields = {
        "evidence_envelope_ref": research.get("evidence_envelope_ref"),
        "claim_audit_ref": research.get("claim_audit_ref"),
        "provenance_ref": research.get("provenance_ref"),
        "data_artifact_ref": research.get("data_artifact_ref"),
        "disclosure_ref": disclosure.get("disclosure_ref"),
    }
    for field, value in reference_fields.items():
        state, ref = _reference_state(value)
        if state == "local-or-opaque-reference-not-resolved":
            findings.append(
                _issue(
                    "research-reference-resolution",
                    f"{field} does not resolve as a local file and has no URI scheme",
                    "warning",
                    field=field,
                    reference=ref,
                    resolution=state,
                )
            )

    return findings


def summarize_claim_audit(findings: Iterable[dict]) -> dict:
    """Summarize only claim/process/reference audit findings."""
    items = [dict(item) for item in findings if isinstance(item, dict)]
    counts = {"error": 0, "warning": 0, "info": 0}
    for item in items:
        severity = str(item.get("severity") or "warning")
        counts[severity] = counts.get(severity, 0) + 1
    status = "failed" if counts["error"] else (
        "observations" if counts["warning"] or counts["info"] else "clean"
    )
    return {
        "profile": PROFILE,
        "status": status,
        "counts": counts,
        "findings": items,
        "semantics": (
            "runtime consistency audit over declared communication/process metadata; "
            "not scientific validation, entailment checking, citation verification, or truth adjudication"
        ),
    }

# Assertion Basis & Communication Coverage — sci-render-kit

**Calibration:** 2026-08-31  
**Status:** implemented companion contract for `sci-render-kit/figure-claim-audit`, `sci-render-kit/figure-evidence`, and downstream communication handoff

## Purpose

Scientific communication metadata should expose both

1. **what the recipe declares** about claims, evidence context, uncertainty and process
2. **where that declaration or identity came from**

The repository therefore keeps

```text
assertion basis
communication coverage
runtime validation
scientific validity
```

as separate concepts

## Assertion bases

Current figure-side bases include

| Surface | Basis |
|---|---|
| figure bytes | `runtime-observed-local-bytes` |
| recipe/profile file identity | runtime-observed local bytes + canonical serialization |
| claim refs | `recipe-declared` |
| visual-to-claim bindings | `recipe-declared` |
| process disclosure | `recipe-declared` |
| uncertainty semantics | `recipe-declared` |
| upstream research refs | recipe-declared with optional local resolution |
| local reference resolution | `runtime-observed-local-filesystem` |
| transferred context | copied from local figure-evidence sidecar |
| transfer destination/purpose | caller-declared or `not_declared` |

A declared relation such as `supports` remains a communication assertion
Its basis being explicit does not make it scientific entailment

```text
assertion basis != correctness
copied-from-sidecar != independently reverified
recipe-declared support != verified support
```

## No automatic AI detection

Figure evidence emits

```json
{
  "automatic_ai_detection_used": false
}
```

The renderer does not inspect labels, captions, prose, pixels or metadata to infer AI authorship/use
It preserves explicit process disclosure supplied in the recipe

```text
AI disclosure != AI detection
AI detection != authorship adjudication
human review != peer review
```

## Communication coverage

`figure-claim-audit` exposes dimensional coverage including

- figure-level claim count
- valid visual binding count
- distinct visual references
- distinct bound claim IDs
- figure-index claims that have at least one binding
- bindings with direct `evidence_ref`
- bindings with any evidence/audit/provenance context
- `supports` bindings and the subset with evidence context
- process-disclosure fields actually declared

Derived ratios include

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

These ratios describe **metadata coverage only**

For example

```text
supports_evidence_context_ratio = 1.0
```

means every declared `supports` binding has some declared evidence/audit/provenance reference context

It does **not** mean

- all support relations are correct
- evidence is sufficient
- the figure proves the claim
- the statistical analysis is valid
- the figure is publication-ready
- claim truth probability is 1.0

## No aggregate communication-quality score

The coverage record intentionally emits

```json
{
  "aggregate_score": null
}
```

Binding coverage, evidence-reference presence, accessibility, publisher presets, uncertainty semantics and scientific validity are different dimensions
This repository has no validated basis for combining them into one research-quality number

## Transfer coverage stays separate

`communication-transfer` may report counts or presence for the subset of figure context carried downstream
That transfer coverage is a different descriptive surface from figure claim coverage

```text
transfer coverage != entailment
transfer coverage != publisher readiness
transfer coverage != evidence sufficiency
```

The handoff must retain explicit non-inheritance constraints rather than treating coverage as inherited authority

## Runtime validation remains separate

```text
runtime_validation
  visual/accessibility/artifact/publisher predicates

communication_audit
  claim/process/reference consistency + dimensional coverage

communication_transfer
  bounded downstream copy + non-inheritance constraints
```

These objects are related but not interchangeable proof objects

## Relation to current research-agent work

External research motivates the inspectability goal without defining this repository

- claim-level auditability work treats provenance coverage and contradiction transparency as first-class evaluation concerns
- artifact-centered claim-aware observability argues for portable claim/artifact/verification relations
- trajectory-to-evidence work distinguishes completed execution from qualified evidence
- Brain Researcher emphasizes claims bounded by evidence and methodological alternatives
- EarthVerse demonstrates end-to-end consistency failures even when local steps succeed
- scientific-publishing guidance emphasizes transparency, accountability and human oversight
- long-horizon research work motivates re-validating assumptions and constraints across changing phases

The Sci Render response remains communication-layer specific

> preserve declared claim-to-visual relations, their basis, their coverage, and their downstream constraints without pretending to verify the science

## Current document and maintenance authority

See [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md) for CURRENT versus HISTORICAL documentation
See [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md) for daily / weekly / monthly maintenance semantics
The August stage is closed in [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

## Hard boundaries

```text
Assertion basis != correctness
Communication coverage != entailment
Binding coverage != evidence sufficiency
Supports label != proof
Runtime validation != scientific validity
Transfer coverage != inherited validity
Accessibility support != whole-publication WCAG conformance
Publisher profile alignment != acceptance
AI disclosure != authorship adjudication
Human review != peer review
Figure evidence != scientific verification
Calendar-month close != reproduction
```

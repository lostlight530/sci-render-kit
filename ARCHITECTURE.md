# Architecture — sci-render-kit

> Calibrated 2026-08-28. This document describes scientific-figure runtime and evidence semantics, not GitHub platform governance.

## Thesis

A scientific figure is a bounded transformation from declared data/specification into a visual artifact plus evidence describing what was rendered, what it is declared to communicate, how those declarations entered the record, and which runtime predicates were checked.

None of those facts alone establishes scientific truth.

## Canonical path

```text
recipe YAML
  ↓
JSON Schema structure
  ↓
runtime visual/accessibility rules
  ↓
claim/process communication audit
    ├─ assertion basis
    └─ dimensional communication coverage
  ↓
backend capability check
  ↓
Matplotlib / ggplot2 / Observable render
  ↓
post-render artifact/publisher-target checks
  ↓
render/provenance/accessibility sidecars
  ↓
figure-evidence
```

## Stable project identifiers

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

Project-owned identifiers are unversioned. Actual external/runtime versions remain evidence where meaningful: WCAG 2.2 references, Matplotlib/NumPy/Python/R/ggplot2 versions and pinned Observable Plot 0.6.17.

## Recipe layer

`metadata/recipe.schema.yaml` defines chart/data/aesthetics/accessibility/research context/claim binding/uncertainty/process disclosure/output structure.

```text
schema success != scientific correctness
```

## Runtime-quality plane

`sci-render-kit/runtime-quality` covers project predicates for visual encoding, declared contrast support, redundant cues, output existence/format, sidecars and explicit publisher-target properties.

It is not a scientific-validity or publisher-acceptance engine.

## Accessibility semantics

WCAG 2.2 is referenced narrowly:

- SC 1.1.1 — text-alternative support;
- SC 1.4.1 — color not the sole required information channel;
- SC 1.4.3 — text contrast support where applicable;
- SC 1.4.11 — required non-text graphical objects/boundaries against adjacent colors.

Project all-pairs `adjacency_check` is deliberately stricter than universal WCAG scope. CVD simulation is an extra safeguard, not certification.

## Claim communication layer

Recipes may declare whole-figure claim refs, visual-to-claim bindings, relation labels, evidence refs and upstream audit/provenance/evidence references.

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are declared communication semantics, not logical proof. The renderer never infers relations from pixels, titles, legends, colors or data values.

## Assertion-basis layer

Day 5 makes acquisition provenance explicit:

| Surface | Basis |
|---|---|
| figure bytes | runtime-observed local bytes |
| recipe/profile identities | runtime-observed local bytes + canonical serialization |
| claim refs/bindings | recipe-declared |
| process disclosure | recipe-declared |
| uncertainty semantics | recipe-declared |
| upstream refs | recipe-declared with optional local resolution |
| local reference resolution | runtime-observed local filesystem |

```text
assertion basis != correctness
recipe-declared support != verified support
```

Process disclosure records `automatic_ai_detection_used: false`; the canonical renderer does not infer AI use/authorship from prose, pixels or metadata.

## Figure Claim Audit

`core/claim_binding_audit.py` produces findings under `sci-render-kit/figure-claim-audit` for metadata-level consistency: malformed/duplicate bindings, index mismatch, missing evidence context for `supports`, disclosure inconsistency, unresolved local-looking refs and visual multiplicity.

It answers whether declared communication metadata is inspectable/self-consistent. It does not answer whether a visual scientifically entails or proves a claim.

## Communication-coverage layer

`claim_communication_coverage(recipe)` summarizes separate dimensions:

```text
figure_claim_count
valid_binding_count
distinct_visual_ref_count
distinct_bound_claim_count
indexed_claims_with_binding_count
bindings_with_evidence_ref_count
bindings_with_any_evidence_context_count
supports_binding_count
supports_with_evidence_context_count
process_disclosure_declared_field_count
```

Ratios:

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

No aggregate score is computed:

```json
{"aggregate_score": null}
```

```text
communication coverage != entailment
coverage ratio != probability
reference context != evidence sufficiency
```

This borrows the measurable-coverage idea from current auditability research without claiming provenance soundness or scientific validity.

## Two evidence planes

```text
runtime_validation
  -> sci-render-kit/runtime-quality

communication_audit
  -> sci-render-kit/figure-claim-audit
       + communication coverage
```

Rendering/accessibility/publisher-target findings remain separate from claim/process/reference findings.

## Backend layer

### Matplotlib

Writes `sci-render-kit/render-manifest` and `sci-render-kit/provenance`, recording real Matplotlib, NumPy and Python versions.

### ggplot2

Writes the stable manifest identifier and records actual ggplot2/R versions where available.

### Observable Plot

Generates HTML and pins `@observablehq/plot` 0.6.17 at view time. Offline reproduction requires separate vendoring/snapshotting.

## Figure Evidence layer

`core/figure_evidence.py` writes `sci-render-kit/figure-evidence` after a successful canonical render.

It indexes figure/recipe/profile identity, backend artifacts, upstream research refs, claim bindings, assertion basis, communication audit/coverage, process disclosure, uncertainty semantics, runtime validation and reproducibility declaration.

Scientific validity is never inherited from upstream references.

## Process disclosure

`sci-render-kit/process-disclosure` records recipe-declared AI assistance/tool identifiers/human review.

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

Unknown tool/model versions stay unknown.

## Uncertainty layer

The recipe distinguishes standard error/deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges and heuristic bounds. The renderer preserves declared semantics; it does not independently validate statistical methods.

## Publisher profiles

Publisher presets are project configuration targets.

```text
profile match != official publisher validation
profile match != acceptance
```

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
epistemic-pipeline/claim-verification
  observation basis + claim audit coverage
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
  communication coverage
        ↓
sci-render-kit/figure-evidence
```

This chain is reference-based; repositories remain independently usable.

## Reproducibility

R0–R3 are local project terms. R3 requires a genuinely separate rerun and declared comparison criterion; manifests/evidence sidecars cannot self-award it.

## Five-day global calibration

The architecture is informed by re-openable autonomous-science provenance, transparent AI use/human oversight, artifact-centered claim-aware observability, trajectory-to-evidence qualification, Brain Researcher evidence-bounded claims, EarthVerse strict end-to-end scientific consistency, and claim-level auditability separating coverage from soundness.

Borrowed: explicit claim/artifact relations, assertion provenance and dimensional coverage.

Not claimed: entailment verification, evidence sufficiency, provenance soundness, automatic AI detection, scientific validity, whole-publication WCAG certification or publisher acceptance.

## Non-goals

- scientific truth adjudication;
- pixel-based claim inference;
- entailment verification;
- provenance soundness validation;
- automatic citation verification;
- automatic AI-text detection;
- statistical-method validation;
- whole-publication WCAG certification;
- official publisher compliance certification;
- peer review;
- automatic R3 reproduction.

## Hard invariants

```text
Render success != scientific validity
Assertion basis != correctness
Communication coverage != entailment
Coverage ratio != probability
Supports label != evidence sufficiency
Uncertainty label != statistical validity
Accessibility support != WCAG certification
Publisher alignment != acceptance
Provenance != truth
Human review != peer review
```

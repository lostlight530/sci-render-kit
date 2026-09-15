# Architecture — sci-render-kit

> Calibrated 2026-08-31. This document describes scientific-figure runtime/evidence semantics, communication transfer, and maintenance/document governance, not GitHub platform governance

## Thesis

A scientific figure is a bounded transformation from declared data/specification into a visual artifact plus evidence describing what was rendered, what it is declared to communicate, how those declarations entered the record, which runtime predicates were checked, and which interpretation constraints must survive downstream handoff

None of those facts alone establishes scientific truth

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
  ↓ optional bounded handoff
communication-transfer
  ├─ declared claim/upstream context
  └─ explicit non-inheritance constraints

repository state
  ↓
daily / weekly / monthly maintenance
  ├─ current-document authority
  ├─ communication-stack reconciliation
  ├─ calendar / stage status
  └─ optional canonical SHA-256 baseline
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
sci-render-kit/communication-transfer
sci-render-kit/maintenance-cadence
sci-render-kit/maintenance-report
```

Project-owned identifiers are unversioned

Actual external/runtime versions remain evidence where meaningful, including WCAG 2.2 references, CFF 1.2.0, Matplotlib/NumPy/Python/R/ggplot2 versions, and pinned Observable Plot 0.6.17

## Recipe layer

`metadata/recipe.schema.yaml` defines chart/data/aesthetics/accessibility/research context/claim binding/uncertainty/process disclosure/output structure

It is a current machine contract under `DOCUMENT_STATUS.md`

```text
schema success != scientific correctness
```

## Runtime-quality plane

`sci-render-kit/runtime-quality` covers project predicates for visual encoding, declared contrast support, redundant cues, output existence/format, sidecars, and explicit publisher-target properties

It is not a scientific-validity or publisher-acceptance engine

## Accessibility semantics

WCAG 2.2 is referenced narrowly

- SC 1.1.1 — text-alternative support
- SC 1.4.1 — color not the sole required information channel
- SC 1.4.3 — text contrast support where applicable
- SC 1.4.11 — required non-text graphical objects/boundaries against adjacent colors

Project all-pairs `adjacency_check` is deliberately stricter than universal WCAG scope

CVD simulation is an extra safeguard, not certification

## Claim communication layer

Recipes may declare whole-figure claim refs, visual-to-claim bindings, relation labels, evidence refs, and upstream audit/provenance/evidence references

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are declared communication semantics, not logical proof

The renderer never infers relations from pixels, titles, legends, colors, or data values

## Assertion-basis layer

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

Process disclosure records `automatic_ai_detection_used: false`; the canonical renderer does not infer AI use/authorship from prose, pixels, or metadata

## Figure Claim Audit

`core/claim_binding_audit.py` produces findings under `sci-render-kit/figure-claim-audit` for metadata-level consistency: malformed/duplicate bindings, index mismatch, missing evidence context for `supports`, disclosure inconsistency, unresolved local-looking refs, and visual multiplicity

It answers whether declared communication metadata is inspectable/self-consistent

It does not answer whether a visual scientifically entails or proves a claim

## Communication-coverage layer

`claim_communication_coverage(recipe)` summarizes separate dimensions

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

Ratios

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

No aggregate score is computed

```json
{"aggregate_score": null}
```

```text
communication coverage != entailment
coverage ratio != probability
reference context != evidence sufficiency
```

The repository borrows measurable coverage from auditability research without claiming provenance soundness or scientific validity

## Two evidence planes

```text
runtime_validation
  -> sci-render-kit/runtime-quality

communication_audit
  -> sci-render-kit/figure-claim-audit
       + communication coverage
```

Rendering/accessibility/publisher-target findings remain separate from claim/process/reference findings

## Backend layer

### Matplotlib

Writes `sci-render-kit/render-manifest` and `sci-render-kit/provenance`, recording real Matplotlib, NumPy, and Python versions

### ggplot2

Writes the stable manifest identifier and records actual ggplot2/R versions where available

### Observable Plot

Generates HTML and pins `@observablehq/plot` 0.6.17 at view time

Offline reproduction requires separate vendoring/snapshotting

## Figure Evidence layer

`core/figure_evidence.py` writes `sci-render-kit/figure-evidence` after a successful canonical render

It indexes figure/recipe/profile identity, backend artifacts, upstream research refs, claim bindings, assertion basis, communication audit/coverage, process disclosure, uncertainty semantics, runtime validation, and reproducibility declaration

Scientific validity is never inherited from upstream references

## Communication-transfer layer

`core/communication_transfer.py` writes `sci-render-kit/communication-transfer` as a bounded view over an existing figure-evidence sidecar

`metadata/communication_transfer.contract.yaml` is the current machine-readable transfer contract

Wrong-profile JSON fails explicitly

The transfer may preserve

```text
claim refs / bindings
upstream research refs
uncertainty semantics
process disclosure
communication audit
runtime validation
```

Required non-inheritance constraints include

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

Destination and purpose remain caller-declared when present

```text
communication transfer != entailment
upstream reference != inherited scientific validity
uncertainty metadata != statistical validation
publisher target != acceptance
```

## Process disclosure

`sci-render-kit/process-disclosure` records recipe-declared AI assistance/tool identifiers/human review

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

Unknown tool/model versions stay unknown

## Uncertainty layer

The recipe distinguishes standard error/deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges, and heuristic bounds

The renderer preserves declared semantics; it does not independently validate statistical methods

```text
bounds != automatically valid confidence interval
uncertainty label != statistical validation
```

## Publisher profiles

Publisher presets are project configuration targets

```text
profile match != official publisher validation
profile match != acceptance
```

## Maintenance and document-governance plane

`core/maintenance_cadence.py` emits `sci-render-kit/maintenance-report`

`maintenance/cadence.yaml` defines canonical current paths, scan paths, cadence behavior, and the configured research stage

`DOCUMENT_STATUS.md` classifies current authority, historical snapshots, examples, and external/citation metadata

The scanner can report

```text
canonical path presence
decorative project profile versions
Manifest calibration age
historical snapshot inventory
canonical SHA-256 baseline
calendar-month status
configured stage status
```

For 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

The maintenance scanner is read-only

It does not render figures, inspect pixels, validate statistics, certify WCAG, predict publisher acceptance, run tests, call GitHub, delete history, or establish scientific validity

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

This chain is reference/transfer based; repositories remain independently usable and scientific validity is not inherited

## Reproducibility

R0–R3 are local project terms

R3 requires a genuinely separate rerun and declared comparison criterion

Manifests, figure-evidence, transfer sidecars, and maintenance baselines cannot self-award it

## Document history

Current document authority is mapped in `DOCUMENT_STATUS.md`

Historical

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

remain time-scoped records rather than current scientific-communication contracts

```text
historical snapshot != current contract
later renderer capability != permission to rewrite history
```

## Stage-close global calibration

The 2026-08-24 → 2026-08-31 architecture is informed by

- re-openable autonomous-science provenance
- transparent AI use/human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency evaluation
- claim-level auditability separating coverage from soundness
- Praxist-style solution/evidence lineage
- ReproAgent-style persistent contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level evaluation beyond final scores
- living research-software maintenance and metadata

Borrowed: explicit claim/artifact relations, assertion provenance, dimensional coverage, transfer constraints, and phase-aware review

Not claimed: entailment verification, evidence sufficiency, provenance soundness, automatic AI detection, scientific validity, whole-publication WCAG certification, publisher acceptance, or independent reproduction

## Non-goals

- scientific truth adjudication
- pixel-based claim inference
- entailment verification
- provenance soundness validation
- automatic citation verification
- automatic AI-text detection
- statistical-method validation
- whole-publication WCAG certification
- official publisher compliance certification
- peer review
- automatic R3 reproduction
- automatic repository scheduler/history deletion

## Hard invariants

```text
Render success != scientific validity
Assertion basis != correctness
Communication coverage != entailment
Coverage ratio != probability
Supports label != evidence sufficiency
Communication transfer != entailment
Uncertainty label != statistical validity
Accessibility support != WCAG certification
Publisher alignment != acceptance
Provenance != truth
Human review != peer review
Maintenance clean != scientific validity
Calendar-month close != reproduction
```

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, and merge-gate architecture remain outside the repository design

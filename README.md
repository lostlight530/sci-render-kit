# sci-render-kit

> Declarative scientific-figure compilation with explicit uncertainty semantics, accessibility intent, publisher-target boundaries, claim-to-visual communication, assertion basis, dimensional communication coverage, runtime audit, portable figure evidence, bounded communication transfer, and phase-aware maintenance

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Figure Claim Contract](FIGURE_CLAIM_CONTRACT.md) · [Communication Transfer](COMMUNICATION_TRANSFER_CONTRACT.md) · [Assertion Basis & Communication Coverage](ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md) · [Maintenance](MAINTENANCE_CADENCE.md) · [Document Status](DOCUMENT_STATUS.md) · [August Stage Close](STAGE_2026_08_MAINTENANCE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Examples](examples/README.md)

## Positioning

`sci-render-kit` does not decide whether a scientific conclusion is correct. It compiles a declarative recipe into a supported visual artifact while keeping communication semantics inspectable and portable

```text
recipe
  ↓ P0 schema
visual/accessibility runtime checks
  ↓ P1 communication audit
claim/process communication audit
  ├─ assertion basis
  └─ dimensional communication coverage
  ↓ backend capability resolution
backend render
  ↓
P2 artifact-integrity checks
  ↓
P3 publisher-target checks
  ↓
render manifest + provenance/accessibility sidecars
  ↓
figure-evidence
  ↓ optional bounded handoff
communication-transfer
  ├─ claim bindings / upstream context
  ├─ uncertainty/process/audit context
  └─ explicit non-inheritance constraints
```

Repository maintenance is a separate read-only plane over this communication stack

```text
daily -> local drift
weekly -> full current communication/document reconciliation
monthly / phase-close -> canonical baseline + history inventory
```

The repository separates renderability, runtime visual/accessibility predicates, declared communication coverage, transfer context, and scientific validity

## Stable internal identifiers

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

Project identifiers are unversioned

Real external/runtime versions remain evidence when genuinely known, including WCAG 2.2 references, CFF 1.2.0, Matplotlib/NumPy/Python/ggplot2/R versions, and pinned Observable Plot 0.6.17

## Capability map

| Surface | Status | Boundary |
|---|---|---|
| `metadata/recipe.schema.yaml` | Implemented current machine contract | recipe structure; schema success != scientific validity |
| `metadata/communication_transfer.contract.yaml` | Implemented current machine contract | bounded transfer shape; not publisher/scientific validation |
| `sci_render.py` | Implemented | unified schema/rule/backend/evidence path |
| `core/accessibility.py` | Implemented | text alternatives/redundant-style intent; not whole-publication WCAG certification |
| `core/color_encoding.py`, `core/palettes.py`, `core/cvd_simulation.py` | Implemented | project safeguards, not universal perceptual guarantees |
| `core/uncertainty_legend.py` | Implemented | explicit uncertainty terminology; not statistical-validity inference |
| `core/claim_binding_audit.py` | Implemented | claim/process consistency + communication coverage; no pixel/entailment inference |
| `core/figure_evidence.py` | Implemented | portable identity/upstream/basis/audit evidence index |
| `core/communication_transfer.py` | Implemented | bounded downstream communication handoff + non-inheritance constraints |
| `core/maintenance_cadence.py` | Implemented maintenance scanner | read-only local structural maintenance evidence |
| Matplotlib backend | Implemented | PNG/SVG/PDF + manifest/provenance evidence |
| ggplot2 backend | Environment-dependent implementation | PNG/SVG/PDF where runtime exists |
| Observable backend | Implemented | HTML; pinned view-time network dependency unless vendored |
| experimental modules | Experimental | not canonical scientific-communication capability |

## Recipe research context

```yaml
research_context:
  artifact_id: result-figure
  evidence_envelope_ref: ../epistemic/evidence/run.evidence.json
  claim_audit_ref: ../epistemic/claim-audits/run.claim-audit.json
  provenance_ref: ../epistemic/provenance/run.prov.json
  data_artifact_ref: ./data/result.csv
  claim_refs: [claim_1, claim_2]
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_1]
      relation: illustrates
    - visual_ref: series:treatment
      claim_refs: [claim_2]
      relation: supports
      evidence_ref: ../epistemic/claim-audits/run.claim-audit.json
```

Allowed declared relation labels

```text
supports
illustrates
contextualizes
compares
derived-from
```

```text
visual binding != verified entailment
supports label != evidence sufficiency
claim reference != claim truth
```

Bindings are never inferred from titles, legends, colors, data values, or pixels

## Figure Claim Audit

`core/claim_binding_audit.py` emits findings under `sci-render-kit/figure-claim-audit`

It checks malformed/duplicate bindings, claim-index mismatch, `supports` relations lacking declared evidence context, process-disclosure inconsistency, unresolved local-looking references, and visual-ref multiplicity

It does not inspect pixels, query literature, verify citations, determine entailment, or judge scientific truth

## Assertion basis

Figure-side evidence records how values entered the record

```text
figure bytes            -> runtime-observed-local-bytes
recipe/profile identity -> runtime-observed local bytes + canonical serialization
claim refs/bindings      -> recipe-declared
process disclosure       -> recipe-declared
uncertainty semantics    -> recipe-declared
upstream refs            -> recipe-declared-with-optional-local-resolution
local ref resolution     -> runtime-observed-local-filesystem
```

```text
assertion basis != correctness
recipe-declared supports != verified support
```

The process path records `automatic_ai_detection_used: false`

The renderer does not infer AI authorship/use from captions, prose, pixels, or metadata

## Dimensional communication coverage

`claim_communication_coverage(recipe)` reports separate dimensions including

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

Derived ratios

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

Example

```text
supports_evidence_context_ratio = 1.0
```

means every declared `supports` binding has some declared evidence/audit/provenance context

It does not mean the support relation is correct, evidence is sufficient, the figure proves the claim, or truth probability is 1.0

```json
{"aggregate_score": null}
```

No composite communication-quality score is manufactured

## Two runtime evidence planes

```text
runtime_validation
  profile: sci-render-kit/runtime-quality

communication_audit
  profile: sci-render-kit/figure-claim-audit
  coverage: {...}
```

Visual/accessibility/artifact/publisher predicates stay separate from claim/process/reference communication audit

## Figure Evidence

After successful canonical rendering, `core/figure_evidence.py` writes `<figure>.evidence.json` under `sci-render-kit/figure-evidence`

It can index figure/recipe/profile identity, backend/sidecars, upstream evidence/audit/provenance/data refs, claim bindings, assertion basis, communication coverage, process disclosure, uncertainty semantics, runtime validation, and R1 replay-addressable status

Scientific validity is never inherited from upstream references

## Communication Transfer

`core/communication_transfer.py` creates a bounded downstream view over an existing `sci-render-kit/figure-evidence` sidecar

The source JSON must carry the expected figure-evidence profile; wrong-profile input fails explicitly

The transfer can preserve

```text
claim refs / bindings
upstream evidence / claim-audit / provenance context
uncertainty semantics
process disclosure
communication audit
runtime validation
```

Destination and purpose are caller-declared when supplied and are not inferred from pixels, captions, filenames, or prose

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

```text
communication transfer != entailment
upstream reference != inherited validity
publisher target != acceptance
accessibility metadata != WCAG certification
```

## Process disclosure

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools: [declared-provider-or-tool]
  human_review: partial
  disclosure_ref: methods.md
```

The evidence record identifies this as `recipe-declared` and records `automatic_ai_detection_used: false`

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
provider/tool label != output validity
```

## Uncertainty semantics

A displayed uncertainty object should declare its kind/semantics

```yaml
uncertainty:
  kind: confidence-interval
  level: 0.95
  semantics: "95% interval produced by the declared analysis method"
  source_ref: analysis.json
```

Bounds alone do not establish a confidence interval, credible interval, or valid uncertainty model

The renderer preserves declared semantics; it does not validate upstream statistics

## Accessibility semantics

WCAG 2.2 is used with scoped semantics

- SC 1.1.1 — text-alternative support
- SC 1.4.1 — do not use color as the sole required information channel
- SC 1.4.3 — text contrast support where applicable
- SC 1.4.11 — required graphical objects/boundaries need sufficient contrast against adjacent colors

`adjacency_check=true` is a stricter project all-pairs palette safeguard, not a universal WCAG requirement

CVD simulation is an extra robustness check, not WCAG certification

## Publisher-target profiles

Publisher presets are machine-readable project configuration targets

```text
profile alignment != publisher certification
profile alignment != acceptance
profile alignment != complete submission compliance
```

The repository is not an official Nature/Science/Cell/IEEE validator

## Backends and real runtime versions

Internal profile IDs are unversioned, but factual runtime versions remain evidence

- Matplotlib provenance records Matplotlib, NumPy, and Python versions
- ggplot2 manifest records installed ggplot2 and R versions
- Observable HTML pins `@observablehq/plot` 0.6.17 and records its view-time dependency

## Reproducibility

- **R0 Traceable** — artifact/source identity located
- **R1 Replay-addressable** — recipe/data/profile/backend identities locate intended replay
- **R2 Environment-bounded** — relevant execution environment/dependencies captured
- **R3 Reproduced** — separate rerun + declared comparison

Sidecars/hashes/transfers/maintenance baselines do not self-award R3

## Daily / weekly / monthly maintenance

Maintenance is defined in [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)

Current document authority is defined in [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)

The closed August baseline is [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Current closed stage

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

The scanner is read-only and does not render figures, inspect pixels, run tests, validate statistics, certify WCAG, predict publisher acceptance, call GitHub, or establish scientific validity

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` remain historical snapshots rather than current contracts

## Stage-close research calibration

The 2026-08-24 → 2026-08-31 architecture is informed by work on

- re-openable autonomous-science provenance
- transparent AI use/human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claims/review
- end-to-end scientific-agent consistency
- claim-level auditability distinguishing coverage from soundness
- Praxist-style solution/evidence lineage
- ReproAgent-style persistent contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments/recovery
- process-level evaluation beyond final scores
- living research-software maintenance and metadata

Borrowed: portable claim/artifact relations, assertion provenance, dimensional communication coverage, explicit transfer constraints, and phase-aware maintenance

Not claimed: entailment verification, evidence sufficiency, provenance soundness, automatic AI detection, scientific validity, WCAG certification, publisher acceptance, or independent reproduction

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

No direct Python imports are required and no scientific validity is inherited through reference/transfer

## Scientific-integrity boundaries

```text
Render success != scientific validity
Assertion basis != correctness
Communication coverage != entailment
Coverage ratio != probability
Visual binding != verified entailment
Supports label != evidence sufficiency
Communication transfer != entailment
Uncertainty label != statistical validity
Accessibility support != whole-publication WCAG certification
Publisher alignment != acceptance
Provenance != truth
Human review != peer review
Maintenance clean != scientific validity
Calendar-month close != reproduction
Metadata != reproduction
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection, and merge gates remain outside this research architecture

Local/manual checks are optional maintenance aids; test execution is not the completion criterion for this stage-close reconciliation

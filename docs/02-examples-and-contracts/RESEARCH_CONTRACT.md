# Research Contract — sci-render-kit

**Status:** active architecture contract  
**Calibrated:** 2026-08-31  
**Closed stage:** 2026-08-24 through 2026-08-31

`sci-render-kit` is the scientific-communication plane of the research toolchain. It compiles a declared recipe into a backend-bounded figure plus inspectable evidence and optional downstream communication-transfer records. It does **not** decide whether the underlying scientific conclusion is true

## Canonical flow

```text
recipe + data + research_context + claim_bindings + uncertainty + process_disclosure
  -> P0 schema
  -> P1 runtime findings + claim communication audit
       ├─ assertion basis
       └─ dimensional communication coverage
  -> backend capability resolution
  -> render
  -> render-manifest / provenance / accessibility sidecars
  -> P2 artifact-integrity findings
  -> P3 publisher-target findings
  -> figure-evidence
  -> optional communication-transfer
       └─ explicit non-inheritance constraints

repository state
  -> daily / weekly / monthly maintenance
       ├─ current-document authority
       ├─ communication-stack reconciliation
       ├─ calendar/stage status
       └─ optional canonical SHA-256 baseline
```

P0–P3 are runtime phases, not GitHub merge gates

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

This does not remove real external/runtime versions such as WCAG 2.2, CFF 1.2.0, Observable Plot 0.6.17, or actual backend/library versions

## Document-authority contract

`DOCUMENT_STATUS.md` classifies current authoritative documents/machine contracts, historical snapshots, examples, and external/citation metadata

Historical Day-N consolidation files remain time-scoped evidence and are not current figure/publisher/accessibility contracts

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## Scientific-integrity boundary

A successful render, audit, transfer, or maintenance scan does not prove scientific truth, causal validity, statistical validity, correct preprocessing/uncertainty estimation, claim entailment, source credibility, evidence sufficiency, authorship, peer review, publisher acceptance, accessibility conformance, or independent reproduction

## Runtime validation semantics

`sci-render-kit/runtime-quality` contains visual/accessibility/artifact/publisher-target predicates with `error / warning / info` severities

```text
runtime validation != scientific validity
runtime validation != publisher acceptance
```

## Claim-to-visual communication

Recipes may declare whole-figure claim refs and visual-level bindings with relation labels

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are communication declarations, never inferred from pixels/titles/legends/data values

```text
claim reference != claim truth
visual binding != verified entailment
supports label != evidence sufficiency
```

## Assertion-basis contract

Recorded values remain distinct from how they entered figure evidence

| Surface | Basis |
|---|---|
| figure bytes | runtime-observed local bytes |
| recipe/profile identities | runtime-observed local bytes + canonical serialization |
| claim refs/bindings | recipe-declared |
| process disclosure | recipe-declared |
| uncertainty semantics | recipe-declared |
| upstream refs | recipe-declared with optional local resolution |
| local reference resolution | runtime-observed local filesystem |
| communication-transfer destination/purpose | caller-declared or not-declared |

```text
assertion basis != correctness
recipe-declared support != scientific verification
```

The process-disclosure path records `automatic_ai_detection_used: false`; the renderer does not infer AI authorship/use from prose, metadata, or pixels

## Communication-coverage contract

`core/claim_binding_audit.py` computes dimensional coverage over declared communication metadata

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

No aggregate quality score is computed

```json
{"aggregate_score": null}
```

```text
communication coverage != entailment
coverage ratio != probability
reference context != evidence sufficiency
coverage != provenance soundness
```

## Communication-transfer contract

`sci-render-kit/communication-transfer` is a bounded downstream view over an existing figure-evidence sidecar

The source JSON must carry the expected `sci-render-kit/figure-evidence` profile

It may carry

```text
claim refs / bindings
upstream research context
uncertainty semantics
process disclosure
communication audit
runtime validation
```

It must explicitly preserve non-inheritance constraints

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

Destination and purpose are caller-declared when supplied

The transfer does not infer destination, publication status, or review authority from filenames, captions, pixels, or metadata

```text
communication transfer != entailment
upstream reference != inherited validity
transfer != publisher acceptance
```

The machine-readable companion contract is `metadata/communication_transfer.contract.yaml`

## Process disclosure

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Process metadata is recipe-declared

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
process disclosure != publisher compliance
```

Unknown tool/model versions remain unknown

## Uncertainty semantics

Supported declared kinds include standard error/deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges, and heuristic bounds

Lower/upper bounds alone do not establish a valid confidence/credible interval or probability model

The renderer preserves declared semantics and does not independently validate the statistical procedure

## Artifact identity and evidence

- `sci-render-kit/render-manifest` preserves recipe/data/profile/output/backend context
- `sci-render-kit/provenance` on the Matplotlib path records artifact identity and actual runtime/library versions where available
- `sci-render-kit/a11y` records declared accessibility support with `conformance_claim: false`
- `sci-render-kit/figure-evidence` indexes figure/recipe/profile identity, sidecars, upstream research refs, claim communication, assertion basis, communication coverage, process disclosure, uncertainty, runtime validation, and local reproducibility semantics
- `sci-render-kit/communication-transfer` carries a bounded subset of context to downstream workflows without inherited authority
- `sci-render-kit/maintenance-report` records local repository-maintenance structure without rendering or scientific validation

Figure evidence and communication transfer are project-owned handoff records, not external standards or scientific proof objects

## Reproducibility levels

- **R0 — Traceable**: figure/source association locatable
- **R1 — Replay-addressable**: recipe/data/profile/output identities recorded
- **R2 — Environment-bounded**: important backend/runtime/dependency assumptions recorded
- **R3 — Reproduced**: a separate rerun executed and compared under a declared criterion

No sidecar/hash/binding/coverage/transfer/maintenance record self-awards R3

## Accessibility boundary

Selected WCAG 2.2 concerns are supported without claiming whole-document conformance

- SC 1.1.1 — text alternatives
- SC 1.4.1 — color not sole information channel
- SC 1.4.3 — text contrast where applicable
- SC 1.4.11 — required graphical objects/boundaries against adjacent colors

`adjacency_check` is a stricter project all-pairs safeguard, not a universal WCAG palette rule

CVD simulation is an extra robustness check, not a WCAG test requirement

## Publisher-target boundary

Publisher profiles are project presets, not official validators

```text
P3/profile match != publisher certification
P3/profile match != acceptance
communication transfer != acceptance
```

## Backend capability truth

Declared outputs

- Matplotlib: PNG/SVG/PDF
- ggplot2: PNG/SVG/PDF where runtime exists
- Observable Plot: HTML with pinned 0.6.17 view-time dependency

Backend source presence does not prove runtime availability or semantic parity

## Maintenance contract

`MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `DOCUMENT_STATUS.md`, and `STAGE_2026_08_MAINTENANCE.md` define current repository maintenance/document governance

The scanner is read-only and reports date-derived calendar status plus configured stage status

For 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

Daily maintenance corrects demonstrated recipe/evidence/backend/document drift

Weekly maintenance reconciles the complete current communication/document stack, machine contracts, upstream profile names, uncertainty/WCAG/publisher boundaries, and historical inventory

Monthly or explicit phase-close maintenance records canonical baselines and reviews current/experimental/not-integrated/document status without automatic deletion

```text
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
history inventory != deprecation decision
```

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓
auto-doc-engine/artifact-lineage
        ↓
epistemic-pipeline/claim-verification
        ↓
epistemic-pipeline/claim-transfer
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
        ↓
sci-render-kit/figure-evidence
        ↓ optional downstream handoff
sci-render-kit/communication-transfer
```

References/transfers are optional handoff relationships, not direct runtime coupling or inherited scientific validity

## RO-Crate interoperability

RO-Crate 1.3 is a useful external packaging target, but this repository does not claim its sidecars are RO-Crates

## Stage-close external calibration

The closed 2026-08-24 → 2026-08-31 design is informed by

- re-openable autonomous-science provenance
- transparent AI use/human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claims/review
- end-to-end scientific-agent consistency
- claim-level auditability
- Praxist-style solution/evidence lineages
- ReproAgent-style persistent implementation/reference contracts
- long-horizon research phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level evaluation beyond final scores
- living research-software maintenance and metadata

Borrowed: explicit claim/artifact relations, assertion provenance, dimensional coverage, persistent interpretive constraints, and phase-aware review

Not claimed: entailment verification, evidence sufficiency, provenance soundness, automatic AI detection, scientific validity, WCAG certification, peer review, publisher acceptance, or independent reproduction

## Experimental modules

Experimental filenames must be interpreted by actual mechanics, not metaphor

Importability does not promote them into canonical capability

## Shared hard boundaries

```text
Render success != scientific truth
Runtime validation != scientific validity
Assertion basis != correctness
Communication coverage != entailment
Coverage ratio != probability
Visual-to-claim binding != verified entailment
Communication transfer != entailment
Upstream reference != inherited validity
AI disclosure != authorship adjudication
Human review != peer review
Publisher alignment != acceptance
Provenance != truth
Checksum != reproduction
Interval bounds != confidence interval
Accessibility sidecar != whole-publication WCAG conformance
Maintenance clean != scientific validity
Calendar-month close != reproduction
```

## Governance boundary

Local/manual checks may be used when useful

GitHub Actions, CI, CodeQL, dependency bots, branch protection, and merge gates remain outside repository architecture

Test execution is not the completion criterion for this stage-close reconciliation

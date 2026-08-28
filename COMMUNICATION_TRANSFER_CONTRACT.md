# Scientific Communication Transfer Contract — sci-render-kit

**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-08-29  
**Implementation:** `core/communication_transfer.py`

## Purpose

`sci-render-kit/communication-transfer` summarizes an existing `sci-render-kit/figure-evidence` sidecar for downstream publication, archival, review or agent workflows.

The transfer exists so a figure does not travel downstream as only an image path or claim ID. It keeps the communication context that is easy to lose:

```text
claim refs
visual-to-claim bindings
upstream evidence / claim-audit / provenance refs
uncertainty semantics
process disclosure
communication-audit summary
runtime-validation summary
```

## Stable profile

```text
sci-render-kit/communication-transfer
```

## Source semantics

The source figure-evidence file is locally byte-identified with SHA-256. Destination and purpose are caller-declared when supplied.

No relationship is inferred from filenames, image pixels, captions, legends or prose.

## Transfer constraints

The handoff explicitly carries:

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

A downstream publication/review system therefore receives the communication metadata without silently inheriting authority the renderer never established.

## Transfer coverage

The record reports counts/presence for claim refs, bindings, upstream research context, process disclosure, uncertainty semantics, communication audit and runtime validation.

```text
aggregate_score: null
```

Coverage is descriptive only. It is not entailment, evidence sufficiency, statistical validity, scientific quality, WCAG conformance or publisher acceptance.

## CLI

```bash
python core/communication_transfer.py \
  output/figure.evidence.json \
  --destination manuscript-main-text \
  --purpose publication-handoff \
  --output output/figure.communication-transfer.json
```

## Relationship to figure evidence

```text
figure-evidence
        ↓ bounded copy / transfer constraints
communication-transfer
        ↓
publication / review / archive / agent workflow
```

The transfer does not replace the full figure evidence sidecar. It is a portable handoff view.

## Global calibration

- **Praxist** (arXiv:2608.25955, 26 Aug 2026) shows why scientific/engineering artifacts benefit from explicit inspectable lineage across generations.
- **ReproAgent** (arXiv:2608.24291, 25 Aug 2026) shows why persistent contracts are useful when requirements and reference evidence must survive long generation/repair trajectories.
- Current autonomous-science provenance and claim-auditability work reinforces keeping artifact/claim relations inspectable rather than relying on opaque conversational context.

These works are design calibration only. They do not certify this repository or make declared visual relations scientifically valid.

## Hard boundaries

```text
Communication transfer != Entailment
Claim binding != Claim truth
Upstream reference != Inherited validity
Uncertainty metadata != Statistical validation
Accessibility metadata != WCAG certification
Publisher target != Acceptance
Human review != Peer review
Provenance != Truth
```

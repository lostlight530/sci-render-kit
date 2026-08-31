# Scientific Communication Transfer Contract — sci-render-kit

**Status:** implemented project-owned handoff contract  
**Calibrated:** 2026-09-01  
**Implementation:** `core/communication_transfer.py`

## Purpose

`sci-render-kit/communication-transfer` summarizes an existing `sci-render-kit/figure-evidence` sidecar for downstream publication, archival, review or agent workflows.

The transfer exists so a figure does not travel downstream as only an image path or claim ID. It keeps communication context that is easy to lose:

```text
claim refs
visual-to-claim bindings
upstream evidence / claim-audit / provenance refs
uncertainty semantics
process disclosure
communication-audit summary
runtime-validation summary
reproducibility context
```

## Stable profile

```text
sci-render-kit/communication-transfer
```

Project-owned identifiers remain unversioned. Real external/runtime versions remain explicit only when genuinely observed or specified.

## Source semantics

The source figure-evidence file is locally byte-identified with SHA-256. Destination and purpose are caller-declared when supplied.

No relationship is inferred from filenames, image pixels, captions, legends or prose.

```text
source hash != semantic equivalence
caller-declared destination != publication acceptance
```

## Reproducibility-context preservation

As of 2026-09-01, the transfer copies the figure-evidence `reproducibility` object rather than dropping it at the communication boundary.

Current figure evidence uses local project semantics such as:

```text
R1 = replay-addressable render inputs/artifact identity
R3 = requires an actual separate rerun and declared comparison criterion
```

The transfer preserves that context but explicitly refuses stronger inheritance:

```text
independent_reproduction_inherited: false
independent_reproduction_claim: false
```

```text
reproducibility metadata copied != rerun executed
R1 context preserved != R3 achieved
source reproducibility label != downstream independent reproduction
```

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
independent_reproduction_inherited: false
```

A downstream publication/review system receives communication metadata without silently inheriting authority the renderer never established.

## Transfer coverage

The record reports counts/presence for claim refs, bindings, upstream research context, process disclosure, uncertainty semantics, communication audit, runtime validation, and reproducibility context.

```text
reproducibility_context_present: true | false
aggregate_score: null
```

Presence is descriptive only. It does not mean independent reproduction occurred.

## Assertion basis

```text
source figure-evidence identity
  -> runtime-observed-local-bytes

transferred figure context
  -> copied-from-local-figure-evidence-sidecar

reproducibility context
  -> copied-from-local-figure-evidence-sidecar

destination / purpose
  -> caller-declared | not_declared

basis_inferred
  -> false
```

```text
copied-from-sidecar != independently reverified
assertion basis != correctness
```

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

## Machine-readable contract

The machine companion is:

```text
metadata/communication_transfer.contract.yaml
```

The machine contract and this document must stay semantically aligned.

## Cross-repository context

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
        ↓
sci-render-kit/communication-transfer
```

The chain is a handoff path, not a chain of inherited scientific authority.

## Current maintenance authority

Current document authority is indexed in `DOCUMENT_STATUS.md`. The August scientific-communication phase closed on 2026-08-31; the 2026-09-01 repair hardens current handoff fidelity without reopening that stage.

## Global calibration

Current long-horizon and scientific-agent work reinforces keeping constraints and intermediate state visible across handoffs. The 2026-09-01 repair applies that principle narrowly to reproducibility semantics: a downstream consumer should not lose the difference between replay-addressable evidence and an actually reproduced result.

These works are design calibration only. They do not certify this repository or make declared visual relations scientifically valid.

## Hard boundaries

```text
Communication transfer != Entailment
Claim binding != Claim truth
Upstream reference != Inherited validity
Uncertainty metadata != Statistical validation
Reproducibility context != Independent reproduction
Accessibility metadata != WCAG certification
Publisher target != Acceptance
Human review != Peer review
Provenance != Truth
Calendar-month close != Reproduction
```

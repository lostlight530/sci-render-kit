# Figure Claim & Process Disclosure Contract — sci-render-kit

**Status:** implemented companion contract  
**Calibrated:** 2026-08-31  
**Primary record:** `sci-render-kit/figure-evidence`

## Purpose

A scientific figure may preserve which upstream claims it is intended to communicate, which visual object relates to which claim, which evidence/provenance refs were declared, how those declarations entered the record, and which communication dimensions are covered

The contract never upgrades those relationships into scientific truth

## Stable project identifiers

```text
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

Internal identifiers remain unversioned; real external/runtime versions remain factual evidence when known

## Figure-level claim references

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
```

```text
claim reference != claim truth
claim reference != evidence sufficiency
```

## Visual-to-claim bindings

```yaml
research_context:
  claim_bindings:
    - visual_ref: series:treated
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

Required

```text
visual_ref
claim_refs[]
relation
```

Allowed relations

```text
supports
illustrates
contextualizes
compares
derived-from
```

Bindings are **recipe-declared** communication semantics
They are never inferred from titles, legends, pixels, labels, prose or data values

```text
visual binding != verified entailment
supports label != evidence sufficiency
illustrates label != causal support
derived-from label != complete provenance proof
```

## Assertion basis

Figure-side evidence records how information entered the record

| Surface | Basis |
|---|---|
| claim refs / bindings | `recipe-declared` |
| process disclosure | `recipe-declared` |
| uncertainty | `recipe-declared` |
| upstream refs | recipe-declared + optional local resolution |
| figure bytes | runtime-observed local bytes |
| local ref resolution | runtime-observed local filesystem |
| communication-transfer destination / purpose | caller-declared or `not_declared` |

```text
assertion basis != correctness
recipe-declared support != scientific verification
```

## Runtime claim communication audit

`core/claim_binding_audit.py` emits `sci-render-kit/figure-claim-audit` findings for metadata consistency, including malformed/duplicate bindings, claim-index mismatches, support relations lacking declared evidence context, process-disclosure inconsistency and unresolved local-looking references

The audit does not inspect pixels, infer claims, dereference remote resources, verify citations or establish scientific validity

## Communication coverage

The audit exposes dimensional coverage

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

These are coverage ratios only

```text
binding coverage != entailment
supports evidence-context coverage != evidence sufficiency
coverage ratio != probability
coverage != provenance soundness
```

No aggregate communication-quality score is computed

```json
{"aggregate_score": null}
```

## Process disclosure

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools: [declared-tool-id]
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

Allowed values

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Figure evidence identifies the basis as `recipe-declared` and records

```json
{"automatic_ai_detection_used": false}
```

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
AI tool identity != output authenticity proof
human review != peer review
human review != truth
```

## Figure evidence

`core/figure_evidence.py` emits `sci-render-kit/figure-evidence` with separate surfaces

```text
claim_communication
  -> declared bindings + assertion basis

communication_audit
  -> findings + dimensional coverage

process_disclosure
  -> declared AI/human-review context + basis
```

It also preserves artifact identities, recipe/profile/backend context, upstream refs, uncertainty semantics, runtime findings and local reproducibility state

Scientific/statistical/causal/authorship/peer-review/publisher-acceptance claims remain false

## Communication transfer

`core/communication_transfer.py` can produce a bounded downstream view over an existing `sci-render-kit/figure-evidence` sidecar

It preserves claim communication, upstream research references, uncertainty semantics, process disclosure, communication audit and runtime validation while carrying explicit non-inheritance constraints

```text
communication transfer != entailment
upstream reference != inherited validity
uncertainty metadata != statistical validation
publisher target != acceptance
accessibility metadata != WCAG certification
```

See [COMMUNICATION_TRANSFER_CONTRACT.md](COMMUNICATION_TRANSFER_CONTRACT.md)

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
        ↓ optional bounded handoff
sci-render-kit/communication-transfer
```

A reference or transfer does not inherit truth

## Current document and maintenance authority

Current document authority is indexed in [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)
Daily / weekly / monthly repository maintenance is defined by [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)
The August 2026 research-maintenance phase is closed in [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

Historical `*_DAY_CONSOLIDATION.md` files remain snapshots of earlier repository states and are not current contracts

## Research direction boundary

Current scientific-agent work increasingly emphasizes portable claim/artifact/evidence records, auditability coverage, evidence-bounded claims, persistent handoff constraints and human oversight
The repository borrows those structural lessons only; it does not claim provenance soundness, entailment verification or scientific-review authority

## Core rule

> Preserve what the figure declares it communicates, the basis of those declarations, and the coverage of the communication record, without silently upgrading any of them into truth

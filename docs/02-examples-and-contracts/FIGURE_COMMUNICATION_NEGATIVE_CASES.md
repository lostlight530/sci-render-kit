# Figure-to-claim communication — source-derived negative cases

**Document class:** durable specialized research-method companion  
**Source baseline:** `main@df9c2424f661b2f0ef258f0064f4480dc8395913`, inspected 2026-11-15  
**Owners:** [Figure Claim](./FIGURE_CLAIM_CONTRACT.md), [Communication Transfer](./COMMUNICATION_TRANSFER_CONTRACT.md), [Assertion Basis and Coverage](./ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md)  
**Implementation:** `core/claim_binding_audit.py`, `core/figure_evidence.py`, `core/communication_transfer.py`

## Non-equivalent evidence planes

```text
recipe -> renderer -> figure bytes / runtime-quality diagnostics
recipe.research_context -> claim binding audit [declared metadata consistency]
figure + recipe + references -> figure-evidence sidecar
figure-evidence sidecar -> transfer [bounded copied context]
```

A `supports` relation is a caller-declared label rather than independently checked logical entailment, and the source code does not inspect pixels to verify the scientific proposition

## Negative-case matrix

| ID | Controlled variation | Code owner | Source-grounded interpretation |
| --- | --- | --- | --- |
| F-1 | Well-formed recipe references an unsupported claim | `audit_claim_communication` | Structural claim binding does not verify empirical evidence |
| F-2 | `evidence_envelope_ref` contains an arbitrary non-empty string | `claim_communication_coverage` | Upstream evidence presence is string-based, not verified retrieval |
| F-3 | Repeat identical `visual_ref`, relation, sorted claim refs and evidence ref | `seen_bindings` in `audit_claim_communication` | Duplicate metadata warning, not measured duplicate image content |
| F-4 | Declare uncertainty without its data-generation/statistical method | `figure_evidence.py` | Metadata retained, no statistical interval certification |
| F-5 | Transfer structurally valid sidecar containing false or unsupported assertions | `communication_transfer.py` | Copies bounded context, not truth, peer review, acceptance or accessibility certification |
| F-6 | Maximize declared binding and support-context ratios without verified sources | `claim_communication_coverage` | Coverage ratios may increase, `aggregate_score=None` |
| F-7 | Define or observe a successful render integration fixture | `tests/test_render_integration.py` | At most the fixture's actual byte/sidecar consistency, not a proof of scientific validity |

## Falsification design

Retain recipe and backend versions, figure digest, source-data identity, claimed proposition and source passage, declared uncertainty computation, exact audit result, produced evidence sidecar and any independent review

Distinguish separately `STRUCTURAL_BINDING`, `SOURCE_SUPPORT`, `STATISTICAL_VALIDITY`, `ACCESSIBILITY_CONFORMANCE`, and `PUBLISHER_ACCEPTANCE`; no positive state on one axis upgrades any other

A figure with attractive styling can be misleading even when it passes declared profile checks, while a source-backed scientific claim can be rendered inaccurately

**Evidence status:** inspected source and existing test definitions, new fixtures `NOT_EXECUTED`, external publication or scientific adjudication `NOT_PERFORMED`

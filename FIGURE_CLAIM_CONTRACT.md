# Figure Claim & Process Disclosure Contract — sci-render-kit

**Status:** implemented companion contract  
**Calibrated:** 2026-08-27  
**Primary record:** `sci-render-kit/figure-evidence`

## 1. Purpose

A scientific figure may need to preserve which upstream claims it is intended to communicate, which visual object relates to which claim, which upstream evidence/provenance references were declared, and what AI/human-review process metadata was declared.

This contract preserves those relationships without pretending the renderer can determine scientific truth.

## 2. Stable project identifiers

```text
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

These identifiers intentionally have no project-invented `@1/@2` suffixes. Compatibility is defined by documented fields and semantics, not decorative counters.

## 3. Figure-level claim references

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
```

These IDs are lineage/context pointers only.

```text
claim reference != claim truth
claim reference != evidence sufficiency
claim reference != statistical validity
```

## 4. Visual-to-claim bindings

```yaml
research_context:
  claim_bindings:
    - visual_ref: series:treated
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

Required fields:

```text
visual_ref
claim_refs[]
relation
```

Optional fields:

```text
evidence_ref
note
```

Allowed relation labels:

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are declared communication semantics, not automatically verified logical entailment. The renderer never infers missing bindings from titles, legends, pixels, labels, prose or data values.

```text
visual binding != verified entailment
supports label != evidence sufficiency
illustrates label != causal support
derived-from label != complete provenance proof
```

## 5. Runtime claim communication audit

`core/claim_binding_audit.py` emits `sci-render-kit/figure-claim-audit` findings for bounded metadata consistency, including duplicate bindings, unresolved local/opaque references, inconsistent process-disclosure fields and support relations that lack declared evidence context.

The audit:

- does not inspect figure pixels;
- does not infer claims from titles or legends;
- does not dereference remote resources;
- does not verify citations;
- does not establish scientific validity or truth.

## 6. Process disclosure

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools: [declared-tool-id]
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

Allowed values:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

Missing values stay `not_declared`. Tool/model/provider identifiers are retained as declarations and are not verified against a vendor registry.

```text
AI disclosure != authorship adjudication
AI tool identity != output authenticity proof
human review != peer review
human review != expert validation
human review != truth
```

## 7. Figure evidence

`core/figure_evidence.py` emits `sci-render-kit/figure-evidence`.

Communication surfaces include:

```text
claim_communication:
  profile: sci-render-kit/figure-claim-binding
  claim_refs: [...]
  bindings: [...]
  inferred_bindings: false

communication_audit:
  profile: sci-render-kit/figure-claim-audit

process_disclosure:
  profile: sci-render-kit/process-disclosure
```

The record also preserves artifact identities, recipe/profile/backend context, uncertainty semantics, runtime findings and local reproducibility state.

Explicit non-claims remain false for authorship, peer review, scientific validity, statistical validity, causal validity and publisher acceptance.

## 8. Cross-repository handoff

```text
auto-doc-engine
artifact-record + process-disclosure
        ↓ optional reference
epistemic-pipeline
claim-verification + evidence-envelope
        ↓ optional reference
sci-render-kit
figure-claim-binding + figure-claim-audit + figure-evidence
```

A Sci Render recipe may reference an Epistemic evidence envelope or claim-verification record and bind declared claim IDs to visual objects. Sci Render does not import Epistemic Pipeline and does not independently validate those upstream claims.

## 9. Research direction boundary

Current scientific-agent research increasingly emphasizes portable artifact/claim/evidence/provenance records and human oversight. That direction motivates this engineering layer; it does not certify this project's implementation, prove novelty, or establish scientific correctness.

## 10. Core rule

> Preserve what the figure declares it communicates and how it was produced, while refusing to silently upgrade those declarations into truth.

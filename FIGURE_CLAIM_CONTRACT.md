# Figure Claim & Process Disclosure Contract — sci-render-kit

**Calibration:** 2026-08-26  
**Status:** implemented companion contract for `sci-render-kit/figure-evidence@2`  
**Scope:** figure-to-claim bindings, upstream evidence references, AI-assistance disclosure, human-review declaration, and scientific-communication boundaries

## 1. Purpose

A scientific figure is not only an image. In an AI-assisted or agentic research workflow, a later auditor may need to know:

```text
Which upstream claim IDs is this figure related to?
Which panel/series/visual object is intended to communicate which claim?
Which upstream evidence/provenance object was referenced?
Was AI assistance declared for the figure-generation process?
Was human review declared?
```

`figure-evidence@2` adds those relationships without pretending that the renderer can determine scientific truth.

## 2. Figure-level claim references

A recipe may continue to declare broad figure-level claim references:

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
```

These IDs identify upstream claims associated with the figure as a whole.

A claim reference is a lineage/context pointer only:

```text
claim reference != claim truth
claim reference != evidence sufficiency
claim reference != statistical validity
```

## 3. Visual-to-claim bindings

For finer-grained communication auditing, the recipe may declare:

```yaml
research_context:
  claim_bindings:
    - visual_ref: series:treated
      claim_refs: [claim_2]
      relation: illustrates
      evidence_ref: evidence/run-042.evidence.json
```

Each binding requires:

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

Allowed relation labels are:

```text
supports
illustrates
contextualizes
compares
derived-from
```

These relation labels are **declared communication semantics**, not automatically verified logical entailment.

The renderer does not parse titles, legends, labels, visual similarity, or data values to infer missing bindings.

`figure-evidence@2` therefore records:

```text
inferred_bindings: false
```

### Hard boundary

```text
visual binding != verified entailment
supports label != evidence sufficiency
illustrates label != causal support
derived-from label != complete provenance proof
figure claim binding != scientific validation
```

## 4. Process disclosure

A recipe may declare:

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools:
    - provider/model or tool identifier declared by the author
  human_review: reviewed
  disclosure_ref: methods/figure-disclosure.md
```

### `ai_assistance`

Allowed values:

```text
none
used
not_declared
```

Absence is not interpreted as `none`.

### `ai_tools`

Human-readable identifiers for tools/models/providers declared by the recipe author or producing system.

The repository does not verify these names against a vendor registry and does not treat the label as proof that a particular output came from that system.

### `human_review`

Allowed values:

```text
reviewed
partial
not_reviewed
not_declared
```

`reviewed` describes declared human review of the figure-generation/communication process only.

```text
human review != peer review
human review != expert validation
human review != truth
```

### `disclosure_ref`

An optional local path or URI to a fuller methods/disclosure record. `figure_evidence.py` records it as a reference and does not dereference or certify it.

## 5. Figure Evidence v2

`core/figure_evidence.py` emits:

```text
sci-render-kit/figure-evidence@2
```

New communication audit surfaces:

```text
claim_communication:
  profile: sci-render-kit/figure-claim-binding@1
  claim_refs: [...]
  bindings: [...]
  inferred_bindings: false

process_disclosure:
  profile: sci-render-kit/process-disclosure@1
  ai_assistance: ...
  ai_tools: [...]
  human_review: ...
```

The profile retains all existing artifact, recipe, publisher-profile, uncertainty, runtime-finding and reproducibility evidence.

Additional explicit false claims include:

```text
authorship_claim: false
peer_review_claim: false
scientific_validity_claim: false
statistical_validity_claim: false
causal_validity_claim: false
publisher_acceptance_claim: false
```

## 6. Cross-repository handoff

The intended three-layer relationship is:

```text
auto-doc-engine
artifact identity + declared AI/human-review context
        ↓
epistemic-pipeline
claim-index@1 + evidence-envelope@2 + provider/review disclosure
        ↓
sci-render-kit
figure-claim-binding@1 + figure-evidence@2
```

A Sci Render recipe may reference an `epistemic-pipeline/evidence-envelope@2` and then bind one or more of its claim IDs to visual objects.

The renderer does not import Epistemic Pipeline and does not independently validate those upstream claims.

## 7. Why this exists now

Three 2026 research signals make the missing layer explicit:

1. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents** argues that autonomous scientific systems need portable claim/artifact relations in addition to model-call telemetry.
2. **EarthVerse** shows that scientific agents can achieve relatively strong local answer-unit performance while still failing strict end-to-end consistency across evidence, units, calculations and interpretation.
3. Nature Computational Science's August 2026 editorial position emphasizes transparency, accountability and human oversight for AI-assisted scientific publishing.

For scientific communication, the narrow engineering response is:

> preserve which claims a figure declares that it communicates, preserve process context, and never silently upgrade those declarations into scientific validity.

These sources motivate the design direction. They do not define or certify this project-owned profile.

## 8. References

- https://arxiv.org/abs/2608.18312
- https://arxiv.org/abs/2608.23525
- https://www.nature.com/articles/s43588-026-01043-4
- https://www.nature.com/articles/s43588-026-01035-4

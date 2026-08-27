# Frontier Alignment — sci-render-kit

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-27

`sci-render-kit` addresses a narrow but increasingly important research-engineering problem: how to preserve scientific communication semantics when figures are produced inside AI-assisted or agentic workflows.

## Current engineering thesis

The relevant artifact is not just an image. It is:

```text
figure
+ recipe identity
+ data/profile/backend context
+ accessibility context
+ uncertainty semantics
+ declared claim-to-visual relations
+ process disclosure
+ runtime findings
+ provenance / evidence references
```

This does not make the renderer a scientific verifier. It makes the communication artifact more inspectable.

## Current external direction

Recent scientific-agent work increasingly emphasizes artifact-centered provenance, claim/evidence structure, end-to-end consistency and human oversight rather than model-call logs alone. Those directions are compatible with this repository's evidence-oriented design.

They are **context, not certification**. No external paper or publisher establishes that this implementation is correct, novel, complete or scientifically valid.

## Distinct layer

Existing plotting libraries remain deeper and more mature at rendering itself. The repository's differentiating layer is the explicit handoff between:

```text
upstream research artifact / evidence
        ↓
declared scientific communication semantics
        ↓
rendered figure + evidence sidecars
```

That positioning should not be rewritten as “better than Matplotlib/ggplot2/Plotly” or as a global uniqueness claim.

## Stable project vocabulary

```text
runtime-quality
render-manifest
provenance
a11y
figure-claim-binding
figure-claim-audit
process-disclosure
figure-evidence
```

Project-owned identifiers intentionally carry no decorative release suffixes. Real standards and observed software/runtime versions remain provenance.

## Hard boundaries

```text
figure evidence ≠ scientific validity
claim binding ≠ entailment
publisher preset ≠ acceptance
accessibility support ≠ whole-document conformance
provenance ≠ truth
checksum ≠ reproduction
AI disclosure ≠ authorship adjudication
human review ≠ peer review
```

The repository should continue improving portability and explicit semantics without crossing these boundaries.

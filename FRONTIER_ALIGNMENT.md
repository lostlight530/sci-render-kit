# Frontier Alignment — sci-render-kit

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-28

`sci-render-kit` addresses a narrow research-engineering problem: preserving scientific communication semantics when figures are produced inside AI-assisted or agentic workflows.

## Current engineering thesis

The relevant artifact is not only an image. It is:

```text
figure
+ recipe/data/profile/backend identity
+ accessibility context
+ uncertainty semantics
+ declared claim-to-visual relations
+ assertion basis
+ dimensional communication coverage
+ process disclosure
+ runtime findings
+ provenance / upstream evidence refs
```

This does not make the renderer a scientific verifier; it makes the communication artifact more inspectable.

## Day-5: assertion provenance

A later auditor benefits from knowing whether a field was recipe-declared or runtime-observed.

```text
claim binding / process / uncertainty -> recipe-declared
figure bytes                         -> runtime-observed-local-bytes
upstream ref resolution              -> runtime-observed-local-filesystem
```

```text
assertion basis != correctness
```

The renderer also records `automatic_ai_detection_used: false` for process disclosure. It does not infer AI authorship/use from figure captions, prose, pixels or metadata.

## Day-5: communication coverage

Current claim-level auditability research separates coverage from stronger ideas such as provenance soundness. Sci Render adopts the part it can honestly compute at the communication layer:

```text
claim-index/binding coverage
binding evidence-context coverage
supports evidence-context coverage
process-disclosure field coverage
```

No aggregate quality score is computed.

```text
communication coverage != entailment
coverage ratio != probability
coverage != provenance soundness
reference context != evidence sufficiency
```

## Global signals used for calibration

### Re-openable provenance

Autonomous-science provenance work motivates durable, inspectable records that can be revisited and corrected.

Borrowed: figure artifacts should remain linked to inputs/context.

Not borrowed: provenance establishes scientific truth.

### Transparent AI use / human oversight

Scientific-publishing guidance supports explicit process disclosure and accountability.

Borrowed: preserve declared AI/human process context.

Not borrowed: disclosure equals authorship adjudication or publisher-policy compliance.

### Artifact-centered claim-aware observability

Current scientific-agent observability research motivates portable artifact/claim/evidence relations beyond raw model-call logs.

Borrowed: figure-to-claim communication should be explicit and independently inspectable.

### From Trajectories to Evidence

Completed execution is not automatically evidence.

Borrowed: a generated figure is not automatically scientific evidence merely because a render completed.

### Brain Researcher

Evidence-bounded claims/review outcomes motivate explicit support/qualification records.

Borrowed: declared support relations should carry inspectable context.

Not borrowed: scientific accepted/rejected verdicts.

### EarthVerse

Strong local task performance can coexist with much weaker strict end-to-end scientific consistency.

Borrowed: preserve cross-layer relationships rather than treating a successful visual as global correctness.

### Claim-level auditability

*From Fluent to Verifiable* distinguishes provenance coverage, soundness, contradiction transparency and audit effort.

Borrowed today: coverage as a separate measurable dimension.

Not implemented: provenance soundness or scientific entailment verification.

### AI detection versus disclosure

Recent Nature reporting on AI-detection tools reinforces that automatic detection and explicit disclosure are separate mechanisms.

Sci Render preserves explicit recipe declarations; it does not silently classify content to infer AI authorship/use.

## Distinct layer

Existing plotting libraries remain deeper/more mature at rendering itself. This repository's focus is the explicit handoff between:

```text
upstream research artifact / claim audit
        ↓
declared scientific communication semantics
        ↓
assertion basis + communication coverage
        ↓
rendered figure + evidence sidecars
```

That positioning is not “better than Matplotlib/ggplot2/Plotly” and is not a global uniqueness claim.

## Cross-repository position

```text
auto-doc-engine
  artifact identity / assertion basis / artifact coverage
        ↓
epistemic-pipeline
  claim/evidence observations / claim coverage / provenance
        ↓
sci-render-kit
  claim-aware communication / communication coverage / figure evidence
```

Together the repositories explore evidence-aware research infrastructure across artifact, epistemic process and scientific communication planes.

## Hard boundaries

```text
figure evidence != scientific validity
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
claim binding != entailment
supports label != evidence sufficiency
publisher preset != acceptance
accessibility support != whole-document conformance
provenance != truth
checksum != reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

> Day 5 makes the communication layer more auditable by preserving both the basis and coverage of declared relationships while refusing to manufacture scientific-verification semantics.

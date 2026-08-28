# Five-Day Consolidation — sci-render-kit

**Window:** 2026-08-24 → 2026-08-28  
**Repository role:** evidence-aware scientific communication plane  
**Status:** implementation and architecture consolidation snapshot

## Five-day trajectory

### Day 1 — truthful rendering contracts

The repository was tightened around declarative recipes, backend capability truth, uncertainty semantics, accessibility boundaries, publisher-profile evidence status and machine-readable artifact identity.

### Day 2 — scientific-communication frontier calibration

The repository was positioned as a communication layer rather than a scientific-reasoning authority. Provenance, accessibility and publisher-target alignment were kept distinct from scientific validity.

### Day 3 — claim-to-visual bindings and process disclosure

Figure evidence gained explicit whole-figure claim references, visual-to-claim bindings and AI/human process disclosure without inferring entailment or authorship.

### Day 4 — communication audit as a separate evidence plane

`figure-claim-audit` began checking internal consistency of declared claim/process/reference metadata. These findings remained separate from visual/accessibility/publisher runtime validation.

### Day 5 — assertion basis + communication coverage

Figure evidence now records how identities and declarations were obtained and exposes dimensional coverage over the communication contract.

```text
runtime-observed-local-bytes
recipe-declared
recipe-declared-with-optional-local-resolution
runtime-observed-local-filesystem
```

No aggregate research-quality score is produced.

## Current canonical path

```text
recipe
  ↓
P0 schema
  ↓
P1 visual/accessibility runtime rules
  + claim/process communication audit
  ↓
backend capability resolution
  ↓
render
  ↓
render manifest / provenance / accessibility sidecars
  ↓
P2 artifact integrity
  ↓
P3 publisher-target alignment
  ↓
figure-evidence
  ├─ artifact identity
  ├─ upstream research refs
  ├─ claim-to-visual bindings
  ├─ assertion basis
  ├─ communication coverage
  ├─ process disclosure
  ├─ uncertainty semantics
  └─ runtime findings
```

## Why Day 5 matters

A downstream reader needs to distinguish:

```text
this binding was declared by the recipe
```

from:

```text
this binding was inferred from the picture
```

The latter is not implemented and remains explicitly false.

Likewise, the system can report that all `supports` bindings carry some declared evidence context without pretending that all support relations are scientifically valid.

## Global calibration

The five-day design is informed by:

- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*;
- *From Trajectories to Evidence*;
- *Bringing analytic rigor to agentic AI for science: The Brain Researcher platform*;
- *EarthVerse*;
- *From Fluent to Verifiable: Claim-Level Auditability for Deep Research Agents*;
- Nature Computational Science commentary on provenance in autonomous science;
- Nature Computational Science guidance on transparent AI use and human oversight;
- Nature reporting on AI-text detection, which reinforces that detection and explicit disclosure are different mechanisms;
- WCAG 2.2 as the current accessibility success-criterion reference used by the project.

Borrowed design ideas:

- portable claim/artifact relations;
- dimensional audit coverage;
- explicit process context;
- evidence-bounded claims;
- separation between local task success and end-to-end scientific consistency.

Not claimed:

- claim entailment verification;
- evidence sufficiency;
- provenance soundness;
- automatic AI-content detection;
- whole-publication WCAG conformance;
- publisher acceptance;
- scientific validity;
- independent reproduction.

## Cross-repository Day-5 chain

```text
auto-doc-engine
  artifact-record
  assertion basis
  artifact audit coverage
        ↓
epistemic-pipeline
  claim-verification
  claim audit coverage
  evidence-envelope
        ↓
sci-render-kit
  figure-claim-audit
  communication coverage
  figure-evidence
```

## Hard boundaries

```text
Render success != scientific truth
Assertion basis != correctness
Communication coverage != entailment
Evidence context != evidence sufficiency
Binding relation != proof
AI disclosure != authorship adjudication
Human review != peer review
Accessibility support != WCAG certification
Publisher alignment != acceptance
Provenance != reproduction
```

## Maintenance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection and merge gates remain outside the repository's scientific architecture. Optional local checks are maintenance aids, not scientific validation.

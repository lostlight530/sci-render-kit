# Four-Day Consolidation — sci-render-kit

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** evidence-aware scientific communication plane  
**Status:** implementation and architecture consolidation snapshot

## 1. Four-day trajectory

### 24 Aug — rendering truth before visual polish

The repository was recalibrated around a strict engineering boundary:

```text
recipe declaration
  != backend capability
  != runtime rule success
  != scientific validity
```

The canonical path became explicit about:

- recipe schema and backend capability truth;
- visual/accessibility runtime findings;
- uncertainty as a typed semantic object rather than styling;
- `render-manifest@2` and Matplotlib `provenance@2`;
- figure-level accessibility sidecars with no whole-publication WCAG claim;
- sourced publisher-target presets with `acceptance_claim: false`;
- local R0–R3 reproducibility language.

### 25 Aug — scientific communication as evidence-bearing artifact

The repository was positioned not as a replacement plotting library but as the
contract around mature renderers: preserve research context, uncertainty,
artifact identity, accessibility and publisher-target evidence as the result
moves from analysis to communication.

### 26 Aug — explicit claim-to-visual bindings

The recipe and `figure-evidence@2` gained:

```text
whole-figure claim_refs[]
visual_ref -> claim_refs[]
relation
optional evidence_ref
AI/human process disclosure
```

The crucial boundary was explicit from the start:

```text
visual binding != verified entailment
```

### 27 Aug — communication relations are now audited at runtime

Previously a schema-valid recipe could still contain semantically awkward
handoff metadata, and the evidence normalizer could drop malformed bindings
without a dedicated audit record.

The unified CLI now executes:

```text
sci-render-kit/figure-claim-audit@1
```

before rendering. It checks only declared metadata and can surface:

- malformed binding records that bypass a direct helper call;
- duplicate visual/claim relations;
- binding claims missing from the whole-figure claim index;
- `supports` relations with no declared evidence context;
- AI process-disclosure inconsistencies;
- local-looking references that do not resolve locally and have no URI scheme;
- intentional visual refs that participate in multiple declared relations.

The final `figure-evidence@2` keeps this audit separate from
`runtime-quality@1`.

## 2. Why the two runtime evidence planes stay separate

Scientific communication has at least two different engineering questions.

### A. Can the declared figure be rendered under the selected contract?

Answered by:

```text
sci-render-kit/runtime-quality@1
```

Examples:

- schema/backend mismatch;
- missing accessibility cue;
- artifact sidecar missing;
- publisher-target size/DPI mismatch.

### B. Is the declared research communication metadata internally inspectable?

Answered by:

```text
sci-render-kit/figure-claim-audit@1
```

Examples:

- duplicate claim binding;
- `supports` with no evidence context;
- process disclosure mismatch;
- unresolved local-looking upstream reference.

Neither profile decides whether the underlying scientific claim is true.

## 3. Global signals borrowed, not overclaimed

### Responsible and transparent AI scientific publishing

The Nature Computational Science editorial *Responsible and transparent use of
AI in scientific publishing* (20 Aug 2026) emphasizes transparency,
accountability and human oversight as AI enters research and communication.

Borrowed principle:

> the production/review context of a figure should be explicitly recordable.

Not borrowed as a claim:

> a process-disclosure field establishes authorship, peer review or publisher
> compliance.

### Provenance grounds trust in autonomous science

The same issue's comment on provenance argues for complete, re-openable records
that can be audited and corrected.

Borrowed principle:

> a figure should remain connected to its recipe, data/context, upstream
> evidence and production sidecars.

Not borrowed as a claim:

> a fully traceable figure is a scientifically valid figure.

### Artifact-centered claim-aware observability

Yin et al. (arXiv:2608.18312) argue that agent observability needs explicit
artifact/claim relations and verification records, not just model-call logs.

Borrowed principle:

> visual artifacts should carry explicit claim relations and references to
> upstream claim verification where available.

The recipe now supports:

```text
research_context.claim_audit_ref
```

for a project such as `epistemic-pipeline/claim-verification@1`.

### EarthVerse

EarthVerse (arXiv:2608.23525) highlights a broader scientific-agent failure:
strong local execution does not guarantee an end-to-end consistent evidence and
interpretation chain.

Borrowed principle:

> the final figure must not erase or silently reinterpret uncertainty, claim
> scope, evidence references or process context inherited from upstream work.

## 4. Current Day-4 canonical architecture

```text
Recipe
  data / aesthetics / output
  accessibility
  uncertainty
  research_context
    artifact/evidence/provenance refs
    claim_audit_ref
    claim_refs
    claim_bindings
  process_disclosure
        ↓
P0 JSON Schema
        ↓
P1 runtime-quality rules
        +
figure-claim-audit@1
        ↓
Backend capability resolution
        ↓
Render
        ↓
Figure
+ render-manifest@2
+ provenance@2 (Matplotlib)
+ a11y@1 (when declared)
        ↓
P2 artifact integrity
        ↓
P3 publisher-target alignment
        ↓
figure-evidence@2
  runtime_validation
  communication_audit
  claim_communication
  upstream_research
  process_disclosure
  uncertainty
```

## 5. Claim communication semantics

A recipe may declare:

```yaml
research_context:
  claim_refs: [claim_1, claim_2]
  claim_audit_ref: claim-audits/run-042.claim-audit.json
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_1]
      relation: illustrates
    - visual_ref: series:treatment
      claim_refs: [claim_2]
      relation: supports
      evidence_ref: evidence/run-042.evidence.json
```

Allowed relation vocabulary remains:

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are **declared communication relations**.

They do not establish:

```text
logical entailment
evidence sufficiency
causal validity
statistical validity
scientific truth
```

## 6. Why `supports` gets a reference warning

The runtime audit does not decide whether evidence truly supports a claim.

It asks a weaker engineering question:

> If the recipe uses the stronger communication verb `supports`, is there at
> least some declared evidence/audit context that a later reviewer can follow?

Therefore a missing evidence reference is a **warning**, not a scientific
rejection.

## 7. Reference resolution boundary

The claim audit is deliberately offline:

- existing local files can be recognized as local references;
- URI-like references are retained as opaque and are not dereferenced;
- local-looking missing paths generate a warning.

This preserves auditability without turning figure rendering into a network
availability test.

## 8. Runtime manifest separation

After Day 4, the render manifest reports independent summaries:

```text
runtime_validation
  profile: sci-render-kit/runtime-quality@1

claim_communication_audit
  profile: sci-render-kit/figure-claim-audit@1

figure_evidence
  profile: sci-render-kit/figure-evidence@2
```

The full claim-audit findings remain in the figure evidence sidecar. This avoids
mixing a metadata relationship warning with a visual rendering failure.

## 9. Cross-repository Day-4 chain

```text
auto-doc-engine
artifact-record@1
        ↓
epistemic-pipeline
claim-verification@1
evidence-envelope@2
        ↓
sci-render-kit
claim_audit_ref
figure-claim-audit@1
figure-evidence@2
```

The renderer can reference upstream evidence without inheriting upstream truth.

## 10. Deliberate non-goals

- automatically deciding whether a visual proves a claim;
- using an LLM as a scientific figure oracle;
- inferring claim bindings from titles, legends or pixels;
- dereferencing every upstream URI during render;
- automatically converting missing evidence into scientific rejection;
- journal acceptance certification;
- whole-publication WCAG conformance claims;
- silently upgrading arbitrary bounds into confidence/credible intervals;
- replacing Matplotlib, ggplot2 or Observable Plot;
- GitHub Actions / CI / CodeQL / merge-gate architecture.

## 11. Primary references

Checked through 2026-08-27:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). https://doi.org/10.1038/s43588-026-01043-4
3. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
4. **EarthVerse: Benchmarking and Advancing AI Agents for Global Earth Science.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
5. WCAG 2.2 Understanding documents: https://www.w3.org/WAI/WCAG22/understanding/

## 12. Bottom line

The Day-4 shift is from:

> “this figure references claim X”

to:

> **“this figure declares how its visual objects relate to upstream claims, the
> runtime audits those declarations for consistency, and the final evidence
> artifact preserves that audit without pretending it verified scientific
> entailment.”**

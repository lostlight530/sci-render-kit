# Architecture — sci-render-kit

> Calibrated 2026-08-27. This document describes scientific-figure runtime and evidence semantics, not GitHub platform governance.

## 1. Thesis

A scientific figure is not only pixels. It is a bounded transformation from declared data/specification into a visual artifact plus evidence describing:

- what was rendered;
- which upstream claims it is declared to communicate;
- which uncertainty semantics were declared;
- which accessibility/publisher-target predicates were checked;
- which backend/runtime produced the artifact;
- which process context was declared;
- which communication-consistency findings were observed.

None of those facts alone establishes scientific truth.

## 2. Canonical path

```text
recipe YAML
  ↓
JSON Schema structure
  ↓
runtime visual/accessibility rules
  ↓
claim/process communication audit
  ↓
backend capability check
  ↓
Matplotlib / ggplot2 / Observable render
  ↓
post-render artifact/publisher-target checks
  ↓
render/provenance/accessibility sidecars
  ↓
figure evidence
```

## 3. Stable project identifiers

Project-owned identifiers are stable semantic names without decorative pseudo-versions:

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

Actual external/runtime versions remain evidence where meaningful: WCAG 2.2 references, Matplotlib/NumPy/Python/R/ggplot2 versions and the pinned Observable Plot dependency.

## 4. Recipe layer

`metadata/recipe.schema.yaml` defines the declarative surface for:

```text
chart type
data
aesthetics
accessibility
research_context
claim bindings
uncertainty
process disclosure
output
```

Schema success means the declared structure matches the schema. It does not mean data or claims are scientifically correct.

## 5. Runtime-quality plane

`sci-render-kit/runtime-quality` covers project predicates for:

- visual encoding;
- declared text/non-text contrast support;
- redundant non-color cues;
- output existence/format;
- expected sidecars;
- explicit publisher-target properties.

It is not a scientific-validity or publisher-acceptance engine.

## 6. Accessibility semantics

WCAG 2.2 is referenced with scoped semantics:

- SC 1.1.1: text-alternative support;
- SC 1.4.1: color should not be the sole visual means where another cue is required;
- SC 1.4.3: declared text contrast support;
- SC 1.4.11: non-text graphical boundaries/components required for understanding.

The project `adjacency_check` all-pairs color policy is intentionally stricter than universal WCAG scope. CVD simulation is an additional safeguard, not a WCAG certification test.

## 7. Claim communication layer

Recipes can declare:

```text
whole-figure claim refs
visual_ref -> claim_refs[]
relation
optional evidence_ref
upstream claim-audit/evidence/provenance refs
```

Supported relation labels are communication semantics, not logical proof:

```text
supports
illustrates
contextualizes
compares
derived-from
```

The renderer never infers these relations from image pixels, title text, legends or colors.

## 8. Figure Claim Audit

`core/claim_binding_audit.py` produces findings under `sci-render-kit/figure-claim-audit`.

It detects metadata-level issues such as duplicate bindings, missing figure-level claim indexing, `supports` without declared evidence context, disclosure inconsistencies and unresolved local-looking references.

This audit answers:

> Is the declared communication metadata internally inspectable and reasonably self-consistent?

It does not answer:

> Does the visual scientifically entail, prove or sufficiently support the claim?

## 9. Two evidence planes

The architecture deliberately separates:

```text
runtime_validation
  -> sci-render-kit/runtime-quality

communication_audit
  -> sci-render-kit/figure-claim-audit
```

Mixing these would cause a claim-reference warning to masquerade as plotting quality, or a rendering issue to masquerade as epistemic judgment.

## 10. Backend layer

### Matplotlib

Writes:

```text
sci-render-kit/render-manifest
sci-render-kit/provenance
```

and records real Matplotlib, NumPy and Python versions.

### ggplot2

Writes the stable render-manifest identifier and records actual ggplot2/R runtime versions where available.

### Observable Plot

Generates HTML and pins `@observablehq/plot` 0.6.17 at view time. The pinned dependency is a real runtime version, not an internal profile release. Offline reproduction requires vendoring/snapshotting that dependency separately.

## 11. Figure Evidence layer

`core/figure_evidence.py` writes `sci-render-kit/figure-evidence` after a successful canonical render.

The record indexes:

```text
figure identity
recipe identity
target profile identity
backend artifacts
upstream evidence envelope
upstream claim audit
upstream provenance/data refs
claim communication bindings
communication audit
process disclosure
uncertainty semantics
runtime validation
reproducibility declaration
```

It does not inherit scientific validity from upstream references.

## 12. Process disclosure

`sci-render-kit/process-disclosure` records declared AI assistance/tool identifiers/human review.

Unknown model/tool versions remain unknown rather than being inferred.

```text
human review != peer review
AI disclosure != authorship adjudication
```

## 13. Uncertainty layer

Uncertainty semantics are explicit because visual bounds are otherwise easy to mislabel.

The recipe can distinguish standard error/deviation, confidence/credible/bootstrap/quantile intervals, min-max range and heuristic bounds. The renderer does not independently validate the statistical method.

## 14. Publisher profiles

Publisher presets are project configuration targets. Runtime checks use only properties declared in those files.

```text
profile match != official publisher validation
profile match != acceptance
```

## 15. Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓
epistemic-pipeline/claim-verification
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
        ↓
sci-render-kit/figure-evidence
```

This chain is reference-based; repositories remain independently usable.

## 16. Reproducibility

R0–R3 remain local project terms. Backend manifests and figure evidence support traceability/replay addressing, but R3 requires a genuinely separate rerun and declared comparison criterion.

## 17. Global design calibration

Recent autonomous-science and scientific-agent work increasingly emphasizes re-openable provenance, claim/artifact observability, evidence-constrained claim qualification, process transparency and strict end-to-end consistency. The architecture borrows those design lessons while keeping communication metadata distinct from scientific verdicts.

No cited work certifies or validates this implementation.

## 18. Non-goals

The canonical architecture does not provide:

- scientific truth adjudication;
- pixel-based claim inference;
- entailment verification;
- automatic citation verification;
- statistical-method validation;
- whole-publication WCAG certification;
- official publisher compliance certification;
- peer review;
- automatic R3 reproduction.

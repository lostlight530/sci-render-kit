# sci-render-kit

> Declarative scientific-figure compilation with explicit uncertainty semantics, accessibility intent, publisher-target boundaries, claim-to-visual communication, assertion basis, dimensional communication coverage, runtime audit and portable figure evidence.

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Figure Claim Contract](FIGURE_CLAIM_CONTRACT.md) · [Assertion Basis & Communication Coverage](ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Five-Day Consolidation](FIVE_DAY_CONSOLIDATION.md) · [Examples](examples/README.md)

## Positioning

`sci-render-kit` does **not** decide whether a scientific conclusion is correct. It compiles a declarative recipe into a supported visual artifact while keeping communication semantics inspectable.

```text
recipe
  ↓ schema structure
visual/accessibility runtime checks
  ↓
claim/process communication audit
  ├─ assertion basis
  └─ dimensional communication coverage
  ↓
backend render
  ↓
artifact/publisher-target checks
  ↓
render manifest + provenance/accessibility sidecars
  ↓
figure-evidence
```

The repository separates renderability, runtime visual/accessibility predicates, declared communication coverage and scientific validity.

## Stable internal identifiers

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/a11y
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

Project identifiers are unversioned. Real external/runtime versions remain evidence when genuinely known: WCAG 2.2 references, Matplotlib/NumPy/Python/ggplot2/R versions, and pinned Observable Plot 0.6.17.

## Capability map

| Surface | Status | Boundary |
|---|---|---|
| `metadata/recipe.schema.yaml` | Implemented | recipe structure; schema success != scientific validity |
| `sci_render.py` | Implemented | unified schema/rule/backend/evidence path |
| `core/accessibility.py` | Implemented | text alternatives/redundant style intent; not whole-publication WCAG certification |
| `core/color_encoding.py`, `core/palettes.py`, `core/cvd_simulation.py` | Implemented | project safeguards, not universal perceptual guarantees |
| `core/uncertainty_legend.py` | Implemented | explicit uncertainty terminology; not statistical-validity inference |
| `core/claim_binding_audit.py` | Implemented | claim/process consistency + communication coverage; no pixel/entailment inference |
| `core/figure_evidence.py` | Implemented | portable identity/upstream/basis/audit evidence index |
| Matplotlib backend | Implemented | PNG/SVG/PDF + manifest/provenance evidence |
| ggplot2 backend | Environment-dependent implementation | PNG/SVG/PDF where runtime exists |
| Observable backend | Implemented | HTML; pinned view-time network dependency unless vendored |
| experimental modules | Experimental | not canonical scientific-communication capability |

## Recipe research context

```yaml
research_context:
  artifact_id: result-figure
  evidence_envelope_ref: ../epistemic/evidence/run.evidence.json
  claim_audit_ref: ../epistemic/claim-audits/run.claim-audit.json
  provenance_ref: ../epistemic/provenance/run.prov.json
  data_artifact_ref: ./data/result.csv
  claim_refs: [claim_1, claim_2]
  claim_bindings:
    - visual_ref: panel:A
      claim_refs: [claim_1]
      relation: illustrates
    - visual_ref: series:treatment
      claim_refs: [claim_2]
      relation: supports
      evidence_ref: ../epistemic/claim-audits/run.claim-audit.json
```

Allowed declared relation labels:

```text
supports
illustrates
contextualizes
compares
derived-from
```

```text
visual binding != verified entailment
supports label != evidence sufficiency
claim reference != claim truth
```

Bindings are never inferred from titles, legends, colors, data values or pixels.

## Figure Claim Audit

`core/claim_binding_audit.py` emits findings under:

```text
sci-render-kit/figure-claim-audit
```

It checks malformed/duplicate bindings, claim-index mismatch, `supports` relations lacking declared evidence context, process-disclosure inconsistency, unresolved local-looking references and visual-ref multiplicity.

It does not inspect pixels, query literature, verify citations, determine entailment or judge scientific truth.

## Assertion basis

Day 5 records how figure-side evidence entered the record:

```text
figure bytes            -> runtime-observed-local-bytes
recipe/profile identity -> runtime-observed local bytes + canonical serialization
claim refs/bindings      -> recipe-declared
process disclosure       -> recipe-declared
uncertainty semantics    -> recipe-declared
upstream refs            -> recipe-declared-with-optional-local-resolution
local ref resolution     -> runtime-observed-local-filesystem
```

```text
assertion basis != correctness
recipe-declared supports != verified support
```

The process path records `automatic_ai_detection_used: false`; the renderer does not infer AI authorship/use from captions, prose, pixels or metadata.

See [ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md](ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md).

## Dimensional communication coverage

`claim_communication_coverage(recipe)` reports separate dimensions including:

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

Derived ratios:

```text
indexed_claim_binding_ratio
binding_evidence_context_ratio
supports_evidence_context_ratio
```

Example:

```text
supports_evidence_context_ratio = 1.0
```

means every declared `supports` binding has some declared evidence/audit/provenance context.

It does **not** mean the support relation is correct, evidence is sufficient, the figure proves the claim, or truth probability is 1.0.

```json
{"aggregate_score": null}
```

No composite communication-quality score is manufactured.

## Two runtime evidence planes

```text
runtime_validation
  profile: sci-render-kit/runtime-quality

communication_audit
  profile: sci-render-kit/figure-claim-audit
  coverage: {...}
```

Visual/accessibility/artifact/publisher predicates stay separate from claim/process/reference communication audit.

## Figure Evidence

After successful canonical rendering, `core/figure_evidence.py` writes `<figure>.evidence.json` under:

```text
sci-render-kit/figure-evidence
```

It can index figure/recipe/profile identity, backend/sidecars, upstream evidence/audit/provenance/data refs, claim bindings, assertion basis, communication coverage, process disclosure, uncertainty semantics, runtime validation and R1 replay-addressable status.

Scientific validity is never inherited from upstream references.

## Process disclosure

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools: [declared-provider-or-tool]
  human_review: partial
  disclosure_ref: methods.md
```

The evidence record identifies this as `recipe-declared` and records `automatic_ai_detection_used: false`.

```text
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
provider/tool label != output validity
```

## Uncertainty semantics

A displayed uncertainty object should declare its kind/semantics, for example:

```yaml
uncertainty:
  kind: confidence-interval
  level: 0.95
  semantics: "95% interval produced by the declared analysis method"
  source_ref: analysis.json
```

Bounds alone do not establish a confidence interval, credible interval or valid uncertainty model. The renderer preserves declared semantics; it does not validate upstream statistics.

## Accessibility semantics

WCAG 2.2 is used with scoped semantics:

- SC 1.1.1 — text-alternative support;
- SC 1.4.1 — do not use color as the sole required information channel;
- SC 1.4.11 — required graphical objects/boundaries need sufficient contrast against adjacent colors;
- SC 1.4.3 — text contrast support where applicable.

`adjacency_check=true` is a stricter project all-pairs palette safeguard, **not** a universal WCAG requirement. CVD simulation is an extra robustness check, not WCAG certification.

## Publisher-target profiles

Publisher presets are machine-readable project configuration targets.

```text
profile alignment != publisher certification
profile alignment != acceptance
profile alignment != complete submission compliance
```

The repository is not an official Nature/Science/Cell/IEEE validator.

## Backends and real runtime versions

Internal profile IDs are unversioned, but factual runtime versions remain evidence:

- Matplotlib provenance records Matplotlib, NumPy and Python versions;
- ggplot2 manifest records installed ggplot2 and R versions;
- Observable HTML pins `@observablehq/plot` 0.6.17 and records its view-time dependency.

## Reproducibility

- **R0 Traceable** — artifact/source identity located.
- **R1 Replay-addressable** — recipe/data/profile/backend identities locate intended replay.
- **R2 Environment-bounded** — relevant execution environment/dependencies captured.
- **R3 Reproduced** — separate rerun + declared comparison.

Sidecars/hashes do not self-award R3.

## Five-day research calibration

The 2026-08-24 → 2026-08-28 architecture is informed by re-openable autonomous-science provenance, transparent AI use/human oversight, artifact-centered claim-aware observability, trajectory-to-evidence qualification, Brain Researcher evidence-bounded claims, EarthVerse strict end-to-end consistency gaps, claim-level auditability work distinguishing coverage from soundness, and current AI-detection reporting that reinforces the distinction between detection and disclosure.

Borrowed: portable claim/artifact relations, assertion provenance and dimensional communication coverage.

Not claimed: entailment verification, evidence sufficiency, provenance soundness, automatic AI detection, scientific validity, WCAG certification or publisher acceptance.

See [FIVE_DAY_CONSOLIDATION.md](FIVE_DAY_CONSOLIDATION.md).

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
epistemic-pipeline/claim-verification
  claim audit coverage + observation basis
        ↓
epistemic-pipeline/evidence-envelope
        ↓
sci-render-kit/figure-claim-audit
  communication coverage
        ↓
sci-render-kit/figure-evidence
```

No direct Python imports are required.

## Scientific-integrity boundaries

```text
Render success != scientific validity
Assertion basis != correctness
Communication coverage != entailment
Coverage ratio != probability
Visual binding != verified entailment
Supports label != evidence sufficiency
Uncertainty label != statistical validity
Accessibility support != whole-publication WCAG certification
Publisher alignment != acceptance
Provenance != truth
Human review != peer review
Metadata != reproduction
```

## Governance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch protection and merge gates remain outside this research architecture. Local checks are optional maintenance aids; test execution is not the completion criterion for this consolidation.

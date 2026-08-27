# sci-render-kit

> Declarative scientific-figure compilation with explicit uncertainty semantics, accessibility intent, publisher-target boundaries, claim-to-visual communication, runtime audit and portable figure evidence.

[Architecture](ARCHITECTURE.md) · [Research Contract](RESEARCH_CONTRACT.md) · [Figure Claim Contract](FIGURE_CLAIM_CONTRACT.md) · [Frontier Alignment](FRONTIER_ALIGNMENT.md) · [Four-Day Consolidation](FOUR_DAY_CONSOLIDATION.md) · [Examples](examples/README.md)

## Positioning

`sci-render-kit` does **not** decide whether a scientific conclusion is correct. It compiles a declarative recipe into a supported visual artifact while keeping communication semantics inspectable.

```text
recipe
  ↓ schema structure
visual/accessibility runtime checks
  ↓
claim/process communication audit
  ↓
backend render
  ↓
artifact/publisher-target checks
  ↓
render manifest + provenance/accessibility sidecars
  ↓
figure evidence
```

The repository separates “can this figure be rendered?”, “does it satisfy project visual/accessibility predicates?”, and “are its declared claim-to-visual relations internally inspectable?” from “is the science true?”.

## Stable internal identifiers

Project-owned identifiers are intentionally unversioned:

```text
sci-render-kit/runtime-quality
sci-render-kit/render-manifest
sci-render-kit/provenance
sci-render-kit/figure-claim-binding
sci-render-kit/figure-claim-audit
sci-render-kit/process-disclosure
sci-render-kit/figure-evidence
```

Decorative `@1/@2` or `/v1` suffixes are not used as pseudo-releases. Real external/runtime versions remain explicit when they are actual evidence—for example WCAG 2.2 references, Matplotlib/NumPy/Python versions recorded by a backend, or the pinned Observable Plot dependency.

## Capability map

| Surface | Status | Boundary |
|---|---|---|
| `metadata/recipe.schema.yaml` | Implemented | validates declared recipe structure; schema success is not scientific validity |
| `sci_render.py` | Implemented | unified schema/rule/backend/evidence path |
| `core/accessibility.py` | Implemented | text alternatives and redundant style intent; not whole-publication WCAG certification |
| `core/color_encoding.py`, `core/palettes.py`, `core/cvd_simulation.py` | Implemented | project visual safeguards, not universal perceptual guarantees |
| `core/uncertainty_legend.py` | Implemented | explicit uncertainty terminology; does not infer statistical validity |
| `core/claim_binding_audit.py` | Implemented | audits declared claim/process/reference consistency without reading pixels or deciding truth |
| `core/figure_evidence.py` | Implemented | portable evidence index for figure/recipe/backend/upstream refs/audits |
| Matplotlib backend | Implemented | PNG/SVG/PDF plus manifest/provenance evidence |
| ggplot2 backend | Implemented where dependencies exist | PNG/SVG/PDF; environment-dependent |
| Observable backend | Implemented | HTML; pinned view-time network dependency unless vendored |
| experimental metaphorical modules | Experimental | not part of canonical scientific-communication contract |

## Recipe research context

A recipe can explicitly reference upstream research artifacts:

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

Supported declared relation vocabulary:

```text
supports
illustrates
contextualizes
compares
derived-from
```

These are communication labels supplied by the recipe author/system.

```text
visual binding != verified entailment
supports label != evidence sufficiency
claim reference != claim truth
```

The renderer never infers claim bindings from figure titles, legends, color or pixels.

## Figure Claim Audit

`core/claim_binding_audit.py` emits runtime findings under:

```text
sci-render-kit/figure-claim-audit
```

It checks declared metadata such as:

- malformed or duplicate bindings;
- binding claims absent from the figure-level claim index;
- `supports` relations with no declared evidence/audit context;
- contradictory AI-assistance/tool disclosure;
- local-looking references that do not resolve;
- a visual object participating in multiple declared relations.

The audit does **not**:

- inspect figure pixels;
- query external literature;
- verify citations;
- determine entailment;
- judge statistical, causal or scientific truth.

A warning that `supports` lacks an evidence reference means only that the recipe lacks inspectable reference context. It is not a verdict that scientific support is insufficient.

## Two runtime evidence planes

The unified CLI deliberately keeps two summaries separate:

```text
runtime_validation
  profile: sci-render-kit/runtime-quality

communication_audit
  profile: sci-render-kit/figure-claim-audit
```

`runtime-quality` covers visual/accessibility/artifact/publisher-target predicates. `figure-claim-audit` covers claim/process/reference metadata consistency.

A claim warning is not relabelled as a plotting-quality failure, and a DPI/palette warning is not relabelled as a scientific claim problem.

## Figure Evidence

After a successful canonical render, `core/figure_evidence.py` writes `<figure>.evidence.json` under:

```text
sci-render-kit/figure-evidence
```

It can index:

```text
figure byte identity
recipe canonical/file identity
target-profile identity
backend identity
render/provenance/accessibility sidecars
upstream evidence envelope
upstream claim audit
upstream provenance/data artifact refs
whole-figure claim refs
visual-to-claim bindings
process disclosure
uncertainty semantics
runtime validation
communication audit
R1 replay-addressable status
```

Local referenced files can receive SHA-256 identity. Opaque references are retained without remote dereference.

Scientific validity is never inherited from an upstream reference.

## Process disclosure

Recipes may declare:

```yaml
process_disclosure:
  ai_assistance: used
  ai_tools:
    - declared provider/model/tool identifier
  human_review: partial
  disclosure_ref: methods.md
```

Vocabulary:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

```text
AI disclosure != authorship adjudication
human review != peer review
provider/tool label != output validity
```

Unknown tool/model versions must not be guessed.

## Uncertainty semantics

A recipe that displays uncertainty should declare what it is:

```yaml
uncertainty:
  kind: confidence-interval
  level: 0.95
  semantics: "95% interval produced by the declared analysis method"
  source_ref: analysis.json
```

Supported kinds include standard error/deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges, heuristic bounds, and not-applicable.

The existence of lower/upper bounds is not enough to call them a confidence interval. The renderer records declared semantics; it does not independently validate the statistical procedure.

## Accessibility semantics

The project uses WCAG 2.2 concepts carefully:

- **SC 1.4.1 Use of Color** — color should not be the sole visual means when information requires another cue;
- **SC 1.4.11 Non-text Contrast** — the 3:1 requirement is relevant to graphical boundaries/components required for understanding;
- **SC 1.4.3 Contrast (Minimum)** — text contrast support where declared;
- **SC 1.1.1 Non-text Content** — text-alternative support.

`adjacency_check=true` intentionally applies a stricter project all-pairs palette safeguard. It is **not** presented as a universal WCAG requirement.

CVD simulation is an additional project safeguard, not a WCAG-mandated certification test.

## Publisher-target profiles

Publisher/profile presets are configuration targets. Runtime checks can compare explicit properties such as preferred/required formats, declared raster DPI and dimensions when the profile contains those values.

```text
profile alignment != publisher certification
profile alignment != acceptance
profile alignment != complete submission compliance
```

The repository does not claim to be an official Nature/Science/Cell/IEEE validator.

## Backends and real runtime versions

Project profile IDs are unversioned, but runtime evidence records actual software versions where known:

- Matplotlib provenance records Matplotlib, NumPy and Python versions;
- ggplot2 manifest records installed ggplot2 and R runtime versions;
- Observable HTML pins `@observablehq/plot` 0.6.17 and records the view-time dependency.

These are factual execution/dependency identities, not internal release decoration.

## Reproducibility

Shared project terminology:

- **R0 Traceable** — artifact/source identity can be located.
- **R1 Replay-addressable** — recipe/data/profile/backend identities describe the intended replay.
- **R2 Environment-bounded** — relevant execution environment/dependencies are also captured.
- **R3 Reproduced** — a separate rerun occurred and was compared under a declared criterion.

A manifest, provenance sidecar, figure evidence record or matching hash alone does not establish R3.

## Cross-repository handoff

```text
auto-doc-engine
artifact-record
      ↓
epistemic-pipeline
claim-verification + evidence-envelope
      ↓
sci-render-kit
figure-claim-audit + figure-evidence
```

Preferred upstream identifiers:

```text
auto-doc-engine/artifact-record
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
```

No direct Python import between repositories is required.

## Current global research calibration

The four-day architecture was rechecked against recent 2026 work on re-openable provenance, transparent AI-assisted scientific publishing, artifact-centered claim-aware observability, evidence-constrained claim qualification, trajectory-to-evidence conversion and strict end-to-end scientific-agent evaluation. Those directions support making claim/artifact/process relations inspectable; they do not certify this repository.

## Scientific-integrity boundaries

- Render success is not scientific validity.
- A figure is not evidence merely because it exists.
- A visual binding is not verified entailment.
- A `supports` label is not evidence sufficiency.
- Uncertainty labels are not statistically valid unless the upstream method justifies them.
- Accessibility checks support design; they do not certify an entire publication.
- Publisher-target alignment is not publisher acceptance.
- Provenance is not truth.
- Human review is not peer review.
- Metadata is not reproduction.

## Governance boundary

No GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge gates are part of this research architecture. Existing local checks remain optional maintenance aids. No test suite is used as the completion criterion for the 2026-08-27 consolidation.

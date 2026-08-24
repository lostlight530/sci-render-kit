# Research Contract — 2026-08-24

Status: **active architecture contract** for figure-generation claims, runtime validation, uncertainty semantics, provenance, accessibility, publisher-target alignment, and cross-repository evidence handoff.

`sci-render-kit` is the scientific-communication plane of the three-repository research toolchain. It turns a declarative recipe into a backend-bounded figure plus machine-readable evidence. It does **not** decide whether the underlying scientific conclusion is true.

## 1. Canonical contract

```text
recipe + data + research_context + uncertainty
  -> P0 schema
  -> P1 runtime findings
  -> backend capability resolution
  -> render
  -> render manifest / provenance / accessibility sidecars
  -> P2 artifact-integrity findings
  -> P3 publisher-target findings
  -> figure-evidence@1
```

P0–P3 are repository runtime phases, not GitHub merge gates.

A successful render establishes only that the implemented predicates passed for the declared recipe, selected backend, selected profile, and current environment.

## 2. Scientific-integrity boundary

A successful figure must not be interpreted as proof of:

- statistical significance;
- causal validity;
- adequate sample size;
- correct preprocessing or missing-data treatment;
- correct uncertainty estimation;
- absence of omitted observations;
- journal acceptance;
- whole-publication accessibility;
- independent reproduction of the scientific result.

`scientific_validity_claim` is therefore `false` in the figure evidence profile.

## 3. Runtime validation semantics

The active catalog is:

```text
quality/rules.yaml
sci-render-kit/runtime-quality@1
```

Each finding has a severity:

- **error** — the current declared render/artifact contract cannot be satisfied; stop the run;
- **warning** — retain as project/publisher-alignment evidence but do not convert to failure;
- **info** — explanatory evidence.

A single boolean `quality_gate_status` is retired from the active architecture because it collapses materially different findings into one value.

Preferred figure-side field is now:

```text
runtime_validation_status
```

with structured findings retained in the figure evidence envelope.

## 4. Uncertainty contract

Uncertainty is a declared semantic object, not a visual synonym for “fuzziness”.

Supported `kind` values include:

```text
standard-error
standard-deviation
confidence-interval
credible-interval
min-max-range
quantile-interval
bootstrap-interval
heuristic-bound
```

Every declared uncertainty object must carry a human-readable `semantics` field. Optional `level` and `source_ref` can preserve coverage/analysis context.

Hard boundary:

> Lower/upper bounds alone do not establish a confidence interval, credible interval, probability, or uncertainty model.

The upstream analysis remains responsible for the statistical meaning of the values supplied to the renderer.

## 5. Artifact identity and evidence

### 5.1 Render manifest

All active backends emit project profile:

```text
sci-render-kit/render-manifest@2
```

The manifest records available recipe/data/profile/output identities and backend/runtime context. It is replay-addressable evidence, not independent reproduction.

### 5.2 Matplotlib provenance

The Matplotlib path emits:

```text
sci-render-kit/provenance@2
```

with recipe/data/profile/output SHA-256 identities and runtime versions. Embedded metadata is used only where the output format supports it.

A SHA-256 digest establishes identity of recorded bytes/canonical serialization. It does not establish semantic truth.

### 5.3 Accessibility sidecar

When accessibility is declared, the unified path emits:

```text
sci-render-kit/a11y@1
```

with `conformance_claim: false`.

### 5.4 Figure evidence

The unified CLI emits:

```text
sci-render-kit/figure-evidence@1
```

The figure evidence envelope references available artifacts by SHA-256 and carries:

- recipe/profile/backend/output identity;
- render manifest / provenance / accessibility references;
- `research_context`;
- uncertainty semantics;
- runtime findings;
- local reproducibility level;
- scientific-boundary flags.

It is a project-owned handoff profile, not a W3C/RO-Crate standard.

## 6. Reproducibility levels

These are local project terms, not an external standard:

- **R0 — Traceable**: figure and declared sources can be associated.
- **R1 — Replay-addressable**: stable recipe/data/profile/output identities and references are recorded.
- **R2 — Environment-bounded**: important runtime/backend/dependency assumptions are also recorded.
- **R3 — Reproduced**: a separate rerun has actually been executed and compared under a declared criterion.

Generating `.manifest.json`, `.prov.json`, `.a11y.json`, or `.evidence.json` does not self-award R3.

## 7. Accessibility contract

The repository supports selected WCAG 2.2 design boundaries without claiming whole-document conformance:

- **SC 1.1.1** — text-alternative support;
- **SC 1.4.1** — color is not the only required information channel when redundant encoding is required;
- **SC 1.4.11** — non-text graphical objects/boundaries required for understanding need appropriate contrast against adjacent colors.

`accessibility.adjacent_pairs` models explicitly declared graphical adjacency.

`aesthetics.adjacency_check` is an optional stricter project all-pairs safeguard. It must not be described as a universal WCAG palette requirement.

Machado 2009 CVD simulation is an additional project robustness signal, not a WCAG-mandated simulation test.

## 8. Publisher-target contract

Profiles are sourced machine-readable presets, not official submission validators.

Every external profile should expose:

```text
source_url
verified_date
source_status
verification_scope
publication.authority
publication.acceptance_claim
```

Current evidence state on 2026-08-24:

- **Nature** — main-figure sizing/font/editability and initial-submission raster guidance reverified against current Nature guidance;
- **Science / Cell / IEEE** — 2026-08-19 local snapshots retained and explicitly marked as not independently reverified on 2026-08-24;
- **presentation** — internal project preset with no external publisher authority.

A P3 match means only that the machine-readable preset did not report a mismatch. It does not mean journal acceptance or exhaustive compliance.

## 9. Backend capability truth

Current declared output sets:

- Matplotlib: PNG, SVG, PDF;
- ggplot2: PNG, SVG, PDF;
- Observable Plot: HTML.

Unsupported combinations fail before a successful render is reported.

Backend availability and semantic parity are separate questions. In particular:

- Matplotlib implements the current non-color redundant-series styling path;
- ggplot2 and Observable do not yet claim that same style-mapping capability;
- Observable HTML pins `@observablehq/plot@0.6.17/+esm` but still requires network access to the CDN when viewed;
- optional R/Node runtimes must not be counted as verified merely because source adapters exist.

## 10. Cross-repository handoff contract

Preferred upstream fields include:

```text
artifact_id
source_refs[]
content_or_data_sha256
evidence_envelope_ref
provenance_ref
claim_refs[]
uncertainty_semantics
validation_status
```

Preferred figure-side fields include:

```text
figure_id
recipe_sha256
input_data_sha256
profile_id
backend_id
output_sha256
manifest_ref
provenance_ref
accessibility_ref
figure_evidence_ref
runtime_validation_status
```

The repositories remain independently runnable. A reference from `sci-render-kit` to an upstream `epistemic-pipeline/evidence-envelope@1` is a handoff relationship, not direct runtime coupling.

## 11. RO-Crate interoperability

RO-Crate 1.3 remains a useful external packaging target. This repository does **not** currently claim that its render manifest, provenance sidecar, accessibility sidecar, or figure-evidence envelope is an RO-Crate.

A future exporter could package the figure, recipe, profile, source data, software environment and upstream evidence into a crate. Until an actual RO-Crate writer/profile/validation path exists here, status remains **proposed interoperability**.

## 12. Experimental modules

Experimental files are bounded by their implemented mechanics:

- `projection.py`: centered-SVD PCA and actual neighborhood-rank metrics; t-SNE not implemented;
- `uncertainty_legend.py`: typed uncertainty/interval metadata; no quantum-uncertainty claim;
- `superposition.py`: deterministic variant layering; no quantum-interference model;
- `time_crystal.py`: periodic waveform utility; no physical time-crystal simulation;
- `observer_dashboard.py`: caller-fed interaction telemetry; no automatic comprehension or causal inference.

Experimental status is not upgraded merely because a module imports successfully.

## 13. Shared hard boundaries

```text
Render success ≠ scientific truth
Runtime validation ≠ scientific validity
Publisher alignment ≠ acceptance
Provenance ≠ truth
Checksum ≠ reproduction
Interval bounds ≠ confidence interval
Accessibility sidecar ≠ whole-publication WCAG conformance
Experimental implementation ≠ canonical pipeline capability
```

## 14. Maintenance model

Local checks may be used manually when useful. The repository architecture does not require GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge gates.

Current maintenance work intentionally prioritizes truthful code/config/document contracts over platform governance.

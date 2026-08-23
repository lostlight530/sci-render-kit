# Architecture & Philosophy — sci-render-kit

## 1. Thesis: a scientific figure is a contract, not a screenshot

A research figure is simultaneously:

- a visual encoding of data,
- an artifact constrained by a publication profile,
- a reproducibility object with provenance,
- and non-text content that may need redundant cues and textual alternatives.

The architecture therefore separates **declaration, policy, rendering, and evidence**. A backend should not invent hidden policy, and a policy file should not claim support that no backend actually renders.

## 2. Pipeline

```text
[YAML Recipe]
    ↓ P0 schema
[Profile + Accessibility Contract]
    ↓ P1 policy gates
[Backend Capability Gate]
    ↓
[Backend Adapter]
    ↓
[Rendered Figure]
    + .manifest.json
    + .prov.json (Matplotlib)
    + .a11y.json (when accessibility is declared)
    ↓ P2 integrity
[Journal Profile Gate]
    ↓ P3 publication constraints
```

## 3. Declaration layer

### 3.1 Recipe

`metadata/recipe.schema.yaml` defines data, aesthetics, output, and accessibility intent. Accessibility fields are deliberately explicit:

- `alt_text`
- `long_description`
- `require_alt_text`
- `redundant_encoding`
- `series_styles`
- `adjacent_pairs`

The schema describes intent; it does not prove that every backend can realize every field.

### 3.2 Profile

Publication profiles encode measurable external constraints such as dimensions, fonts, DPI, and vector-format expectations. Their `source_url` and `verified_date` fields are snapshots, not promises that publishers will never update guidance.

## 4. Policy layer — `sci_render.py`

The unified CLI owns validation. Adapters remain rendering implementations rather than independent policy engines.

### 4.1 Accessibility scope

The 2026-08-23 calibration separates three WCAG-related concerns that were previously conflated with palette checks:

1. **SC 1.1.1 support — Text alternatives.** A recipe can require a short `alt_text`; a long description can carry richer trends/interpretation or point to the data table.
2. **SC 1.4.1 support — Use of Color.** When `redundant_encoding: required`, multiple visual series cannot rely on color alone. Matplotlib maps the same labels to distinct marker / line-style / hatch cues.
3. **SC 1.4.11 support — Non-text Contrast.** `adjacent_pairs` identifies graphical series that are actually adjacent and required for understanding; those declared boundaries are checked at ≥ 3:1.

The older `aesthetics.adjacency_check` remains available as an intentionally stricter **all-pairs project policy**. It must never be described as WCAG requiring every categorical color pair to contrast 3:1.

Machado CVD simulation stays a separate project safeguard. CVD resilience is valuable, but it is not itself a WCAG success criterion.

### 4.2 Backend capability truth

A schema field is not backend implementation evidence. Today:

- Matplotlib can render redundant line/marker/hatch cues.
- ggplot2 and Observable can participate in the backend-independent text-alternative sidecar, but their redundant-series-style mapping is **Not Integrated**.
- If a recipe requests `auto` or `required` redundant encoding on a backend without that capability, the CLI fails with `BACKEND_ACCESSIBILITY_MISMATCH` before dispatch.

This preserves the repository's central doctrine: **unsupported must be explicit, not silently downgraded.**

## 5. Matplotlib two-layer adapter

The mature renderer is retained byte-for-byte as `backends/matplotlib_base.py`. The public `backends/matplotlib_adapter.py` imports that implementation and adds accessibility policy behavior.

```text
matplotlib_adapter.py
    ├─ re-exports existing public renderer API
    ├─ patches render logic only during one accessibility-aware render
    ├─ maps labels -> marker / line_style / hatch
    ├─ embeds alt text in PNG/SVG/PDF metadata where supported
    └─ extends the existing manifest with accessibility linkage

matplotlib_base.py
    ├─ profile merge
    ├─ code generation
    ├─ Matplotlib execution
    ├─ reproducibility manifest
    └─ provenance sidecar + embedded provenance metadata
```

This is an adapter-policy split: new policy can evolve without rewriting the stable rendering core or breaking existing direct imports.

## 6. Evidence sidecars

### 6.1 `.manifest.json`

Records generator, profile, parameters, output checksum, and — when accessibility is declared — a pointer to the accessibility profile/sidecar.

### 6.2 `.prov.json`

Matplotlib provenance records recipe/input/output SHA-256 and environment metadata. It provides traceability evidence, not a mathematical guarantee that the experiment is perfectly reproducible on every future machine.

### 6.3 `.a11y.json`

`core/accessibility.py` emits `sci-render-kit/a11y@1` containing:

- text alternatives,
- redundant-encoding mode,
- actual series colors,
- actual non-color cues,
- declared adjacent pairs,
- explicit `conformance_claim: false`.

The sidecar makes the figure's accessibility intent inspectable and machine-readable. Association of that sidecar with a figure in a final website/PDF remains the responsibility of the publishing layer.

## 7. Quality gates

- **P0:** JSON Schema / recipe structure
- **P1:** aesthetics + accessibility semantics
- **P2:** output, manifest, provenance, accessibility evidence
- **P3:** publication-profile format / DPI / dimensions

Each gate has a different failure meaning. A P1 accessibility failure is not the same class of problem as a P3 journal-size mismatch.

## 8. Verification architecture

`make test` runs the legacy 26-test renderer/gate/provenance suite plus `tests/test_accessibility.py`. GitHub Actions executes the same deterministic Python contract with Python 3.12 and the Matplotlib/Pillow stack.

Node and R runtime tests remain optional because the core CI must not turn missing external ecosystems into false failures or false passes.

## 9. Hard rules

1. Declaration does not imply backend support.
2. Color cannot be the only required series cue when redundant encoding is required.
3. WCAG wording must preserve the actual success-criterion scope.
4. Project-strict policies must be labelled as project policies.
5. Matplotlib base rendering stays policy-light; validation belongs to the unified CLI.
6. Provenance, reproducibility, and accessibility are related evidence layers but not interchangeable claims.
7. No output sidecar justifies saying a paper is “100% reproducible” or “WCAG conformant”.
8. Experimental modules remain Experimental until wired into the canonical render path with tests.

## 10. Direction

The project is moving from “multi-backend chart generator” toward an **auditable scientific-figure compiler**:

```text
intent -> constraint -> encoding -> render -> evidence -> publication
```

Future work should extend backend parity and evidence quality before adding speculative visualization modules.

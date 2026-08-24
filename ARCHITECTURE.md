# Architecture — sci-render-kit

## 1. Thesis

A scientific figure is not only pixels. It is a bounded transformation from declared data/specification into a visual artifact plus evidence describing what was rendered, under which backend/profile/environment, and what the runtime checks actually established.

The canonical architecture separates:

1. **declaration** — recipe, research context, uncertainty semantics, accessibility intent;
2. **runtime validation** — explicit machine rules with severity;
3. **capability resolution** — what the selected backend can actually produce;
4. **rendering** — backend-specific implementation;
5. **artifact evidence** — manifest, provenance, accessibility and figure-evidence sidecars;
6. **publisher-target alignment** — sourced preset comparison, not acceptance certification.

## 2. Canonical flow

```text
[YAML Recipe]
  data / aesthetics / output
  research_context
  uncertainty
  accessibility
        ↓
[P0 JSON Schema]
        ↓
[P1 Runtime Findings]
 error / warning / info
        ↓
[Backend Capability Resolution]
        ↓
[Adapter]
        ↓
[Figure]
 + render-manifest@2
 + provenance@2       (Matplotlib)
 + a11y@1             (when declared)
        ↓
[P2 Artifact Integrity]
        ↓
[P3 Publisher-target Alignment]
        ↓
[figure-evidence@1]
```

P0–P3 are runtime phases. They are not GitHub merge gates.

## 3. Declaration plane

### 3.1 Recipe identity

`metadata/recipe.schema.yaml` is the canonical recipe contract. The recipe file has a byte-level SHA-256; its structured `data` object has a canonical JSON SHA-256 in backend evidence. These identities answer different questions and must not be conflated.

### 3.2 Research context

`research_context` can carry references such as an upstream artifact ID, evidence-envelope path, provenance path and claim IDs. These references are handoff metadata; the renderer does not independently validate the scientific truth of upstream claims.

### 3.3 Uncertainty semantics

An interval must state what it means. `uncertainty.kind` distinguishes standard error, standard deviation, confidence/credible/bootstrap/quantile intervals, min-max ranges and heuristic bounds.

A pair of lower/upper numbers is never automatically promoted to a confidence interval. Coverage/frequentist/Bayesian semantics remain the responsibility of the upstream analysis that produced the interval.

### 3.4 Accessibility intent

Recipe-level accessibility remains separate from publisher profiles:

- text alternative / long description;
- whether non-color redundant encoding is required;
- per-series marker/line/hatch overrides;
- actual adjacent graphical-series pairs.

The schema declares intent. Backend capability still determines what can be realized.

## 4. Runtime-quality plane

The active catalog is `quality/rules.yaml` with profile `sci-render-kit/runtime-quality@1`.

Each finding has:

```text
check_id
level
severity
message
details
```

Only `severity: error` stops the render. Warnings are retained as evidence.

This matters because these conditions are not equivalent:

- malformed recipe;
- unsupported backend/output pair;
- missing required accessibility cue;
- project CVD robustness warning;
- publisher-format preference mismatch.

One boolean “quality gate passed” cannot faithfully represent all of them.

## 5. Accessibility / WCAG scope

The runtime supports selected WCAG 2.2 design boundaries without claiming whole-publication conformance:

- **SC 1.1.1**: short text-alternative contract;
- **SC 1.4.1**: color cannot be the only required distinction when redundant encoding is required;
- **SC 1.4.11**: contrast for graphical objects/boundaries required for understanding, including explicitly declared adjacent series where applicable.

`aesthetics.adjacency_check` is an intentionally stricter project all-pairs rule. It is not a universal WCAG requirement.

Machado CVD simulation is another project safeguard, not a WCAG success criterion.

`core/accessibility.py` emits `sci-render-kit/a11y@1` with `conformance_claim: false`.

## 6. Publisher-profile plane

Profiles contain two categories of data:

- `publication`: machine-readable target-alignment fields used by P1/P3;
- `aesthetics`: actual defaults merged into rendering.

Every external profile exposes `source_url`, `verified_date`, `source_status` and `verification_scope`.

A profile can therefore say “reverified publisher guidance” or “historical local snapshot” instead of silently presenting every number as equally current.

`acceptance_claim: false` is the default scientific boundary.

## 7. Backend plane

### 7.1 Matplotlib

```text
matplotlib_adapter.py
  -> explicit accessibility render/metadata functions
  -> matplotlib_base.render(..., render_logic_fn=..., metadata_fn=...)
```

The adapter no longer mutates module-global base functions during a render. The base renderer remains the code-generation/provenance implementation and receives extension functions explicitly.

The output DPI is the merged profile/recipe DPI. The renderer no longer silently applies `max(dpi, 300)`.

Matplotlib evidence:

- `sci-render-kit/render-manifest@2`
- `sci-render-kit/provenance@2`
- embedded metadata where supported

### 7.2 ggplot2

The R adapter records the same `render-manifest@2` identity categories and the R/ggplot2 runtime when executed. It does not currently implement the Matplotlib redundant-series-style contract.

### 7.3 Observable Plot

The generated HTML pins `@observablehq/plot@0.6.17/+esm`. The manifest records that browser viewing still requires the CDN/network, so the artifact must not be described as offline environment-complete evidence.

## 8. Figure evidence plane

`core/figure_evidence.py` creates `sci-render-kit/figure-evidence@1` after successful artifact checks.

It references available artifacts with SHA-256 rather than duplicating payloads and records:

- recipe/profile/output identities;
- manifest/provenance/accessibility references;
- backend;
- upstream research context;
- uncertainty declaration;
- runtime findings;
- local reproducibility semantics;
- `scientific_validity_claim: false`.

This is the project-level bridge from research analysis evidence to scientific communication. It is intentionally separate from RO-Crate and W3C PROV semantics.

## 9. Reproducibility model

Local terminology:

- **R0 Traceable** — artifact association exists;
- **R1 Replay-addressable** — stable content identities and references are recorded;
- **R2 Environment-bounded** — sufficient runtime/dependency assumptions are also captured;
- **R3 Reproduced** — a separate rerun actually occurred and was compared under a declared criterion.

A single successful render cannot self-award R3.

## 10. Experimental plane

Experimental modules remain outside the dispatcher.

- `projection.py`: centered-SVD PCA and actual neighborhood-rank metrics; t-SNE is explicit Not Implemented rather than a fake approximation.
- `uncertainty_legend.py`: typed interval/heuristic-bound metadata; no Heisenberg analogy as statistical evidence.
- `superposition.py`: deterministic variant layering; no quantum interference model.
- `time_crystal.py`: deterministic periodic waveform utility; no time-crystal physics simulation.
- `observer_dashboard.py`: caller-fed interaction telemetry; no automatic comprehension/causal inference.

Historical filenames may remain for compatibility. Their documentation must describe implemented mechanics, not metaphorical physics.

## 11. Maintenance architecture

Optional local commands may inspect repository contracts:

```bash
make test
```

They are maintenance aids only. The architecture explicitly does **not** require GitHub Actions, CodeQL, dependency bots, branch-protection rules or merge gates.

Hard rules for future work:

1. Declaration does not imply backend support.
2. A warning is not automatically an error.
3. Publisher alignment is not publisher acceptance.
4. Provenance is not truth.
5. Interval semantics must be declared rather than guessed.
6. Color semantics are project conventions unless stronger evidence exists.
7. Whole-publication accessibility cannot be inferred from a figure sidecar.
8. No experimental module may return fabricated metrics or pretend to implement an algorithm it does not implement.
9. New evidence profiles must distinguish byte identity, structured identity and scientific meaning.
10. Public docs, schemas, runtime rules and backend behavior must describe the same capability boundary.

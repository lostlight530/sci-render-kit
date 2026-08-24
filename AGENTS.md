# Agent Guide — sci-render-kit

This is the operational contract for agents modifying the repository. Public claims must stay aligned across runtime code, schemas, profiles, evidence sidecars, README, Architecture, Research Contract and Manifest.

## 1. Canonical architecture

```text
metadata/recipe.schema.yaml
  -> sci_render.py
     P0 schema
     P1 runtime findings
     backend capability resolution
  -> backend adapter
  -> figure + sidecars
  -> P2 artifact findings
  -> P3 publisher-target findings
  -> core/figure_evidence.py
```

Active runtime catalog:

```text
quality/rules.yaml
sci-render-kit/runtime-quality@1
```

Do **not** reintroduce `quality/gates.yaml` or describe P0–P3 as GitHub merge gates.

## 2. Evidence profiles

Current project profiles:

- `sci-render-kit/render-manifest@2`
- `sci-render-kit/provenance@2` — Matplotlib path
- `sci-render-kit/a11y@1`
- `sci-render-kit/figure-evidence@1`

These profiles record bounded implementation evidence. None proves scientific truth, journal acceptance, independent reproduction, or whole-publication WCAG conformance.

## 3. Runtime finding semantics

Rules use `error / warning / info`.

- `error`: current declared render/artifact contract cannot be satisfied;
- `warning`: preserve as evidence without turning it into a hard failure;
- `info`: explanatory signal.

Do not convert project safeguards or publisher preferences into errors without an explicit architectural reason.

## 4. Hard rules

1. **Schema ≠ backend support.** Update capability matrices only after actual backend behavior exists.
2. **No hidden rendering overrides.** Do not silently raise DPI, change output format, or replace declared uncertainty semantics.
3. **Uncertainty must be typed.** Bounds alone are not a confidence interval. Preserve `kind`, `semantics`, optional `level`, and source reference.
4. **Use of Color.** If redundant encoding is required, supported multi-series figures need non-color cues.
5. **WCAG scope.** SC 1.4.11 is about required graphical objects/boundaries against adjacent colors, not every pair in a palette. All-pairs checking is a project policy only.
6. **CVD scope.** Machado simulation is a robustness safeguard, not a normative WCAG test.
7. **Color semantics.** `positive -> green` and similar mappings are project conventions, not universal cognitive laws.
8. **Publisher profiles are snapshots.** Preserve `source_status`, `verified_date`, `verification_scope`, and `acceptance_claim: false`.
9. **Matplotlib extension model.** Use explicit `render_logic_fn` / `metadata_fn` injection. Do not restore global monkeypatching of base renderer functions.
10. **Optional ecosystems stay optional.** Source code presence is not R/Node runtime verification.
11. **Figure evidence is handoff, not truth.** Upstream evidence-envelope/provenance references are not independently validated by the renderer.
12. **No fake algorithms.** Experimental modules must use `NotImplementedError` rather than return fabricated t-SNE/metric/physics outputs.
13. **Experimental stays Experimental.** Importability does not promote a module into the canonical dispatcher.
14. **No GitHub-native governance creep.** Do not add Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate language as repository architecture.

## 5. Where to change what

| Goal | Primary files | Required synchronization |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime/backend/docs/evidence semantics |
| runtime rule | `quality/rules.yaml`, `sci_render.py` | severity + public docs |
| uncertainty | recipe schema + consumer | semantics must remain explicit |
| accessibility | `core/accessibility.py`, `sci_render.py` | a11y sidecar + backend capability truth |
| Matplotlib render | `backends/matplotlib_base.py` | preserve explicit extension hooks |
| Matplotlib accessibility | `backends/matplotlib_adapter.py` | preserve public API/direct-run bootstrap |
| ggplot2 | `backends/ggplot2_adapter.R` | manifest/runtime boundary |
| Observable | `backends/observable_adapter.js` | pinned Plot version/network dependency |
| publisher profile | `profiles/*.yaml` | source evidence status + P3 semantics |
| color registry | `core/palettes.py`, `core/color_encoding.py` | avoid unsupported CVD/perceptual claims |
| figure evidence | `core/figure_evidence.py` | Research Contract + Manifest |
| public capability | README / Architecture / Manifest | update together |

## 6. Experimental semantics

Historical file names may be retained for compatibility, but their module-level descriptions must match implemented mechanics:

- `projection`: PCA + projection-quality metrics; t-SNE not implemented here;
- `uncertainty_legend`: typed bounds/interval metadata;
- `superposition`: deterministic variant layering;
- `time_crystal`: periodic waveform utility;
- `observer_dashboard`: caller-fed interaction telemetry.

Do not use physics metaphors as evidence of statistical or scientific capability.

## 7. Local maintenance

When useful:

```bash
python -m pip install pyyaml jsonschema matplotlib numpy pillow
make test
```

These are optional local maintenance checks. This 2026-08-24 refresh does not rely on them as completion evidence and does not make them a GitHub merge policy.

## 8. Consistency rule

When code behavior changes, update the nearest machine-readable contract first, then public docs. Never leave an old test, profile, example, or historical design document presenting retired behavior as current architecture.

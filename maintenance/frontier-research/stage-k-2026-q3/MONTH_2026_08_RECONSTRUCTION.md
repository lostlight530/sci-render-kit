# Frontier Research Stage K / 2026-Q3 — 2026-08 monthly research reconstruction
- Source period: 2026-08; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Patch fidelity, major export migration and runtime floors. Evidence-object count: 1; **not** a measure of field-wide activity.
## 2026-08-25 — Plotly major export migration (`K-O2`)
**Publisher source:** [plotly/plotly.py v7.0.0](https://github.com/plotly/plotly.py/releases/tag/v7.0.0) (`K-S2`).
**Observed release note:** Plotly.py 7.0 bundles plotly.js 4, removes legacy Mapbox traces and legacy Orca/Kaleido image export paths.
**Analysis:** Wrapper major, JS engine and export backend are independent compatibility gates for saved figure recipes.
**Alternative / caution:** No old/new renderer execution or publisher-target check.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.

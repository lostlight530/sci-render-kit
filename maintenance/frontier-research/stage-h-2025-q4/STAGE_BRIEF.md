# Frontier Research Stage Brief — Stage H / 2025-Q4

## Identity
- Repository: `lostlight530/sci-render-kit`
- Stage: `H / 2025-Q4`
- Window: `2025-10-01 through 2025-12-31`
- Record type: `RETROSPECTIVE`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-27`
- Status: `COMPLETE`

## Rationale
Stage G made package/runtime/platform, browser/export engine, and interaction semantics explicit parts of figure identity. Stage H follows Q4 as wrapper and dependency surfaces shift again: Matplotlib tightens a parser dependency floor, Plotly.py advances the bundled Plotly.js communication semantics, and Altair 6 moves the Python wrapper onto Vega-Lite 6 while also changing reproducibility-relevant execution properties.

## Selected objects
- Matplotlib 3.10.7 — 2025-10-08.
- Plotly.py 6.4.0 / 6.5.0 — 2025-11-04 / 2025-11-17, treated as one November same-lineage transition.
- Altair 6.0.0 — 2025-11-12.
- December: `NO_NEW_SELECTED_OBJECT` under this search-bounded reconstruction.

## Hard boundaries
```text
dependency floor != local environment replay
wrapper version != renderer version
renderer feature != scientific validity
template/hover behavior != accessibility certification
thread-safe claim != all integrations race-free
stable rerun spec != identical rendered pixels
NO_NEW_SELECTED_OBJECT != no ecosystem activity
```

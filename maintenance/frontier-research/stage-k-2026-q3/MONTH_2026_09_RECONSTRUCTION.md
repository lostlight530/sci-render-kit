# Frontier Research Stage K / 2026-Q3 — 2026-09 monthly research reconstruction
- Source period: 2026-09; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Patch fidelity, major export migration and runtime floors. Evidence-object count: 2; **not** a measure of field-wide activity.
## 2026-09-15 — Interpreter floor and interaction parameters (`K-O3`)
**Publisher source:** [vega/altair v6.3.0](https://github.com/vega/altair/releases/tag/v6.3.0) (`K-S3`).
**Observed release note:** Altair 6.3.0 drops Python 3.10 support and expands parameter expressions while tightening invalid argument errors.
**Analysis:** Dependency floors and stricter grammar validation affect whether the same declared recipe can execute.
**Alternative / caution:** No environment compatibility matrix or interaction replay ran.

## 2026-09-11 — Backend-specific figure fixes (`K-O4`)
**Publisher source:** [matplotlib/matplotlib v3.11.2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2) (`K-S4`).
**Observed release note:** Matplotlib 3.11.2 reports PDF hexbin clipping, Cairo glyph, WebAgg/Qt HiDPI and GIF skew fixes.
**Analysis:** One plotting recipe may differ across backend export targets even on the same scientific dataset.
**Alternative / caution:** Only specified failure modes are evidenced; no backend experiment.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.

# Versioned Evidence Chart — Stage K / 2026-Q3

- Repository: `lostlight530/sci-render-kit`
- Source window: `2026-07-01 through 2026-09-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1) | Fixes font glyph embedding and layout in PDF/PostScript | Export format/font backend matter even for constant plot data | No local PDF before/after test | `NOT_RUN` |
| O2 / [S2](https://github.com/plotly/plotly.py/releases/tag/v7.0.0) | Drops Orca and Kaleido below v1, removes engine argument and upgrades plotly.js to v4 | Major change separates old/new export, JS, MathJax and map behavior | Cannot infer historical plots were scientifically wrong | `NOT_RUN` |
| O3 / [S3](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2) | Fixes PDF hexbin clipping, Cairo glyphs and WebAgg HiDPI | PDF and interactive output have different fidelity gates | No physical rendering test | `NOT_RUN` |
| O4 / [S4](https://github.com/vega/altair/releases/tag/v6.3.0) | Drops Python 3.10 support and adjusts expression/parameter support | Interpreter floor affects reproducible spec generation | No local Python compatibility matrix | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.

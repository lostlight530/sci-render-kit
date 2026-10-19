# Monthly Historical Reconstruction — 2026-01 / Stage I / 2026-Q1

- Repository: `lostlight530/sci-render-kit`
- Source window: `2026-01-01 through 2026-03-31`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
- Selection: `SELECTED_OBJECTS`
- This is a curated source-bounded month record, not an exhaustive claim about the month.

### O1 — plotly/plotly.py v6.5.1
- Published: 2026-01-07; [primary publisher tag](https://github.com/plotly/plotly.py/releases/tag/v6.5.1); source S1.
- Publisher-reported change: Fixes template trace colors and bumps Plotly.js 3.3.0 to 3.3.1.
- Repository-lens inference: Template and bundled JS identities affect visuals.
- Alternative/boundary: Not tested with local chart samples.
- [Research Part](I1_TEMPLATE_JS.md).

### O2 — vega/vega-lite v6.4.2
- Published: 2026-01-14; [primary publisher tag](https://github.com/vega/vega-lite/releases/tag/v6.4.2); source S2.
- Publisher-reported change: Fixes tooltip formatters, nearest-hit data and legend merging.
- Repository-lens inference: Interaction semantics are grammar-version dependent.
- Alternative/boundary: No browser or accessibility replay.
- [Research Part](I2_TOOLTIP_LEGEND.md).

## Source and time boundary
Public upstream release note establishes its own versioned publication, not observed deployment or independent correctness. Release time differs from retrospective analysis performed 2026-10-19. No local runtime, benchmark, output or current defect was checked.

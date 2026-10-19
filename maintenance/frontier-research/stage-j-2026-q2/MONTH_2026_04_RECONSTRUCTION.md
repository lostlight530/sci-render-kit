# Monthly Historical Reconstruction — 2026-04 / Stage J / 2026-Q2

- Repository: `lostlight530/sci-render-kit`
- Source window: `2026-04-01 through 2026-06-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
- Selection: `SELECTED_OBJECTS`
- This is a curated source-bounded month record, not an exhaustive claim about the month.

### O1 — vega/altair v6.1.0
- Published: 2026-04-21; [primary publisher tag](https://github.com/vega/altair/releases/tag/v6.1.0); source S1.
- Publisher-reported change: Updates Vega-Lite target to 6.4.1 with tooltip, stack and cursor behavior.
- Repository-lens inference: Python wrapper and grammar engine revision are distinct.
- Alternative/boundary: No generated spec rerun.
- [Research Part](J1_GRAMMAR_INTERACTION.md).

### O2 — matplotlib/matplotlib v3.10.9
- Published: 2026-04-23; [primary publisher tag](https://github.com/matplotlib/matplotlib/releases/tag/v3.10.9); source S2.
- Publisher-reported change: Hardens cycler validation and LaTeX/PostScript shell-escape handling.
- Repository-lens inference: Renderer security context differs from picture correctness.
- Alternative/boundary: Upstream security fix is not this repo security audit.
- [Research Part](J2_RENDER_HARDENING.md).

## Source and time boundary
Public upstream release note establishes its own versioned publication, not observed deployment or independent correctness. Release time differs from retrospective analysis performed 2026-10-19. No local runtime, benchmark, output or current defect was checked.

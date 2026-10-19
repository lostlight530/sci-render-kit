# Monthly Historical Reconstruction — 2026-09 / Stage K / 2026-Q3

- Repository: `lostlight530/sci-render-kit`
- Source window: `2026-07-01 through 2026-09-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
- Selection: `SELECTED_OBJECTS`
- This is a curated source-bounded month record, not an exhaustive claim about the month.

### O3 — matplotlib/matplotlib v3.11.2
- Published: 2026-09-11; [primary publisher tag](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2); source S3.
- Publisher-reported change: Fixes PDF hexbin clipping, Cairo glyphs and WebAgg HiDPI.
- Repository-lens inference: PDF and interactive output have different fidelity gates.
- Alternative/boundary: No physical rendering test.
- [Research Part](K3_PDF_CLIP_GLYPH.md).

### O4 — vega/altair v6.3.0
- Published: 2026-09-15; [primary publisher tag](https://github.com/vega/altair/releases/tag/v6.3.0); source S4.
- Publisher-reported change: Drops Python 3.10 support and adjusts expression/parameter support.
- Repository-lens inference: Interpreter floor affects reproducible spec generation.
- Alternative/boundary: No local Python compatibility matrix.
- [Research Part](K4_PYTHON_FLOOR.md).

## Source and time boundary
Public upstream release note establishes its own versioned publication, not observed deployment or independent correctness. Release time differs from retrospective analysis performed 2026-10-19. No local runtime, benchmark, output or current defect was checked.

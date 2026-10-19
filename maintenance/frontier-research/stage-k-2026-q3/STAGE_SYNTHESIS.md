# Frontier Research Stage K / 2026-Q3 — quarterly research synthesis
## Identity
- `lostlight530/sci-render-kit`; study window 2026-07-01–2026-09-30; reconstructed/synthesized 2026-10-19; `SOURCE_BOUNDED / COMPLETE`.
- `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; not contemporaneous execution, systematic review, or independently verified result.
## Question revisited
**Patch fidelity, major export migration and runtime floors:** what evidentiary boundary changed in this selected three-month history?
## Month and Part inputs
- [2026-07](MONTH_2026_07_RECONSTRUCTION.md)
- [2026-08](MONTH_2026_08_RECONSTRUCTION.md)
- [2026-09](MONTH_2026_09_RECONSTRUCTION.md)
- [Part K1: Layout and glyph fixes](K1_LAYOUT_AND_GLYPH_FIXES.md) — [matplotlib/matplotlib v3.11.1](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1), 2026-07-18
- [Part K2: Plotly major export migration](K2_PLOTLY_MAJOR_EXPORT_MIGRATION.md) — [plotly/plotly.py v7.0.0](https://github.com/plotly/plotly.py/releases/tag/v7.0.0), 2026-08-25
- [Part K3: Interpreter floor and interaction parameters](K3_INTERPRETER_FLOOR_AND_INTERACTION_PARAMETERS.md) — [vega/altair v6.3.0](https://github.com/vega/altair/releases/tag/v6.3.0), 2026-09-15
- [Part K4: Backend-specific figure fixes](K4_BACKEND_SPECIFIC_FIGURE_FIXES.md) — [matplotlib/matplotlib v3.11.2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2), 2026-09-11
## Source selection, method and appraisal
Executed 2026-10-19: publisher release-index enumeration and exact tag reads; chose 4 release objects in Patch fidelity, major export migration and runtime floors. These are publisher-origin product/specification/version statements. `SOURCE_BOUNDED` is the only coverage claim. Comparison uses research-question, versioned mechanism, time and evidence authority, not benchmark scores or number of announcements. Same-origin releases are related but not independent corroboration.
## Substantive quarter narrative
### 1. Layout and glyph fixes (2026-07-18)
**Evidence:** Matplotlib 3.11.1 reports tight-layout, 3D aspect and PDF font glyph fixes. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1).
**Meaning:** Patch releases can change visible publication artifacts without changing data inputs.
**Counter-reading:** No PDF, 3D or layout pixel diff was executed.

### 2. Plotly major export migration (2026-08-25)
**Evidence:** Plotly.py 7.0 bundles plotly.js 4, removes legacy Mapbox traces and legacy Orca/Kaleido image export paths. [Source](https://github.com/plotly/plotly.py/releases/tag/v7.0.0).
**Meaning:** Wrapper major, JS engine and export backend are independent compatibility gates for saved figure recipes.
**Counter-reading:** No old/new renderer execution or publisher-target check.

### 3. Interpreter floor and interaction parameters (2026-09-15)
**Evidence:** Altair 6.3.0 drops Python 3.10 support and expands parameter expressions while tightening invalid argument errors. [Source](https://github.com/vega/altair/releases/tag/v6.3.0).
**Meaning:** Dependency floors and stricter grammar validation affect whether the same declared recipe can execute.
**Counter-reading:** No environment compatibility matrix or interaction replay ran.

### 4. Backend-specific figure fixes (2026-09-11)
**Evidence:** Matplotlib 3.11.2 reports PDF hexbin clipping, Cairo glyph, WebAgg/Qt HiDPI and GIF skew fixes. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2).
**Meaning:** One plotting recipe may differ across backend export targets even on the same scientific dataset.
**Counter-reading:** Only specified failure modes are evidenced; no backend experiment.

## Cross-Part interpretation
The common research movement is **patch fidelity, major export migration and runtime floors**: selected release records reveal multiple distinct states—declared interface, effective runtime/configuration, action or rendering behavior, verification output and wider research interpretation. These states must not be collapsed. Different version families and software domains are not statistically comparable; there is no controlled common outcome metric.
## What persisted, failed to be shown and remains unknown
- Hard boundaries: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
- Publisher release statement != current target repo capability; a fix is not evidence that this repo had the associated defect.
- No local native experiment, exact-version reproduction, formal citation chaining, implementation-conformance audit, independent counterevidence study or peer review.
- Historical event/publication dates were not backdated from 2026-10-19; source-family selection bias and missing independent validation persist.
## Review and current repository boundary
[Producer Research Review](RESEARCH_REVIEW.md); `SAME_PRODUCER_REVIEW`. Local implementation drift = `NOT_AUDITED`; active-contract drift = `NOT_AUDITED`; runtime change = `NO`; contract change = `NO`.
## Conclusion
`FRONTIER_STAGE_COMPLETE` only within the declared retrospective `SOURCE_BOUNDED` research scope. This is a knowledge artifact and [bounded handoff](STAGE_HANDOFF.md), not a certificate of scientific correctness, performance or project implementation.

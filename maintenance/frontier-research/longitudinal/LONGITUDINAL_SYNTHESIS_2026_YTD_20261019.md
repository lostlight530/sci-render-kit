# Longitudinal Frontier Synthesis — 2026 YTD / cutoff 2026-10-19
- `lostlight530/sci-render-kit`; 2026-01-01 through 2026-10-19; `SOURCE_BOUNDED / YTD_OPEN_YEAR`; retrospective research performed 2026-10-19.
- Completed documentary Stages [I](../stage-i-2026-q1/STAGE_SYNTHESIS.md), [J](../stage-j-2026-q2/STAGE_SYNTHESIS.md), [K](../stage-k-2026-q3/STAGE_SYNTHESIS.md); [Q4 Stage L](../stage-l-2026-q4/STAGE_BRIEF.md) `IN_PROGRESS`.
## Research question
How did selected 2026 versioned changes alter the evidence identity required for figure evidence, scientific claim binding, wrapper/JS renderer revisions, accessibility, export and backend identity, relative to 2025 Stage H? This is neither a full-year close nor a source-exhaustive historical field review.
## Monthly / quarterly sources and turning points
- [2026-01](../stage-i-2026-q1/MONTH_2026_01_RECONSTRUCTION.md)
- [2026-02](../stage-i-2026-q1/MONTH_2026_02_RECONSTRUCTION.md)
- [2026-03](../stage-i-2026-q1/MONTH_2026_03_RECONSTRUCTION.md)
- [2026-04](../stage-j-2026-q2/MONTH_2026_04_RECONSTRUCTION.md)
- [2026-05](../stage-j-2026-q2/MONTH_2026_05_RECONSTRUCTION.md)
- [2026-06](../stage-j-2026-q2/MONTH_2026_06_RECONSTRUCTION.md)
- [2026-07](../stage-k-2026-q3/MONTH_2026_07_RECONSTRUCTION.md)
- [2026-08](../stage-k-2026-q3/MONTH_2026_08_RECONSTRUCTION.md)
- [2026-09](../stage-k-2026-q3/MONTH_2026_09_RECONSTRUCTION.md)
- [2026-10](../stage-l-2026-q4/MONTH_2026_10_RECONSTRUCTION.md)
### 2026-Q1: Theme and interaction changes across patch releases
- 2026-01-07: [plotly/plotly.py v6.5.1](https://github.com/plotly/plotly.py/releases/tag/v6.5.1) — Plotly.py fixes ignored template trace-color sequences and bundles plotly.js 3.3.1. **Interpretation:** Colors and legend state can encode categories; wrapper and JS identity condition presentation semantics.
- 2026-03-02: [plotly/plotly.py v6.6.0](https://github.com/plotly/plotly.py/releases/tag/v6.6.0) — Plotly.py bundles plotly.js 3.4.0, supporting legend-title toggles and multi-axis shape behaviors. **Interpretation:** Similar static plots may expose different interaction trajectories under new JS revisions.

### 2026-Q2: Grammar, prerelease and modern text shaping
- 2026-04-21: [vega/altair v6.1.0](https://github.com/vega/altair/releases/tag/v6.1.0) — Altair updates Vega-Lite 6.4.1 and fixes hash collisions between structurally identical specs using different data. **Interpretation:** Declarative spec and bound data identity must be retained separately; tooltip/cursor grammar can vary with runtime.
- 2026-05-13: [matplotlib/matplotlib v3.11.0rc2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2) — Matplotlib explicitly labels 3.11.0rc2 as a release candidate addressing downstream and deprecation issues. **Interpretation:** Release candidate availability is not stable release availability; its status and dates require separate treatment.
- 2026-06-12: [matplotlib/matplotlib v3.11.0](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0) — Matplotlib 3.11.0 reports font/text processing changes using libraqm, HarfBuzz, SheenBidi and FreeType. **Interpretation:** Font shaping and bidi layout can change human-readable figure meaning, separate from plotting data.

### 2026-Q3: Patch fidelity, major export migration and runtime floors
- 2026-07-18: [matplotlib/matplotlib v3.11.1](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1) — Matplotlib 3.11.1 reports tight-layout, 3D aspect and PDF font glyph fixes. **Interpretation:** Patch releases can change visible publication artifacts without changing data inputs.
- 2026-08-25: [plotly/plotly.py v7.0.0](https://github.com/plotly/plotly.py/releases/tag/v7.0.0) — Plotly.py 7.0 bundles plotly.js 4, removes legacy Mapbox traces and legacy Orca/Kaleido image export paths. **Interpretation:** Wrapper major, JS engine and export backend are independent compatibility gates for saved figure recipes.
- 2026-09-15: [vega/altair v6.3.0](https://github.com/vega/altair/releases/tag/v6.3.0) — Altair 6.3.0 drops Python 3.10 support and expands parameter expressions while tightening invalid argument errors. **Interpretation:** Dependency floors and stricter grammar validation affect whether the same declared recipe can execute.
- 2026-09-11: [matplotlib/matplotlib v3.11.2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2) — Matplotlib 3.11.2 reports PDF hexbin clipping, Cairo glyph, WebAgg/Qt HiDPI and GIF skew fixes. **Interpretation:** One plotting recipe may differ across backend export targets even on the same scientific dataset.

### 2026-Q4 — OPEN through 2026-10-19
No selected October release object from the checked Matplotlib/Plotly/Altair publisher feeds; this is not a global absence claim.
## Cross-Stage interpretation
Source events illustrate successive questions about how a result is produced and interpreted, but their change logs are not independent scientific trials. The *unit* is a versioned release/contract and its evidence, not an invented improvement metric. A source-listed capability, actual local execution, correctness review and cross-repository authority are separate. Major and patch revisions can be compared as identity mechanisms, not aggregated into a causal monotonic performance trend.
## Counter-reading and constraints
Object selection privileges releases close to this repository's lens, so broader community practices may follow a different path. No formal systematic search, field-wide effect estimate, independent adoption measure, local runtime execution, controlled reproduction or scientific adjudication was performed. `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
Stage L open October record does not certify October complete, Q4 close, or December annual close. 2025 historical syntheses are left unchanged. Any subsequent conflict belongs in a dated correction.
## Current-state governance
The A2-owned `LONGITUDINAL_INDEX.md` retains its older source-time router statements until a separate whole-month relation reconciliation. The new research timepoint is documented in the [reconciliation record](../corrections/RECONCILIATION_2026-10-19_STAGE_I_K_RESEARCH_INTRODUCTION.md). No runtime/contract change authorized; current target-repo drift `NOT_AUDITED`.

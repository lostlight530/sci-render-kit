# 2026-Q1 / 03 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-03-01 through 2026-03-31`
- Stage owner: `I / 2026-Q1`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-03-02 — Renderer/export patch and side effects
- **Primary source:** https://github.com/plotly/plotly.py/releases/tag/v6.6.0 (`plotly/plotly.py@v6.6.0`, `S3`)
- **Publisher-described observation:** Plotly.py 6.6.0 fixes a global warning-format side effect and a spurious write_image engine deprecation warning, and updates its underlying JS.
- **Analytic implication:** A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe.
- **Alternative / qualification:** Diagnostic change alone does not prove pixel or semantic output changed for every figure.
- **Research owner:** `I3` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O3 / S3 (plotly.py v6.6.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.

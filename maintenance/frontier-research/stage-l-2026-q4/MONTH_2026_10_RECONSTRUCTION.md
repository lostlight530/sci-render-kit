# 2026-Q4 / 10 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-10-01 through 2026-10-19`
- Stage owner: `L / 2026-Q4`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_OPEN — as of 2026-10-19`

## Selected events and evidence
### 2026-10-05 — Resize observer and responsive layout
- **Primary source:** https://github.com/plotly/plotly.js/releases/tag/v4.1.2 (`plotly/plotly.js@v4.1.2`, `S13`)
- **Publisher-described observation:** Plotly.js 4.1.2 changes responsive resizing to ResizeObserver instead of window resize events and documents image-export config in schema.
- **Analytic implication:** Viewport and host resize events are observable parts of interactive-figure reproducibility; host layout can modify what a recipient sees.
- **Alternative / qualification:** Responsiveness is not accessibility validation, scientific claim validation or guaranteed behavior in all host environments.
- **Research owner:** `L1` in this Stage; one originating source family, no independent validation.

### 2026-10-08 — Image-mark alignment correction
- **Primary source:** https://github.com/vega/vega-lite/releases/tag/v6.5.0 (`vega/vega-lite@v6.5.0`, `S14`)
- **Publisher-described observation:** Vega-Lite 6.5.0 fixes image-mark center alignment when a secondary channel is undefined.
- **Analytic implication:** Compiler revision changes spatial interpretation of a declarative spec even without changed data.
- **Alternative / qualification:** A scoped alignment fix is not an independent cross-version equivalence test.
- **Research owner:** `L2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O13 / S13 (plotly.js v4.1.2), O14 / S14 (vega-lite v6.5.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.

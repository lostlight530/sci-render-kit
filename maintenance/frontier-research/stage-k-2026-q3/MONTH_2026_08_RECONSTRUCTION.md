# 2026-Q3 / 08 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-08-01 through 2026-08-31`
- Stage owner: `K / 2026-Q3`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-08-25 — JS 4.0, exporter and map migration
- **Primary source:** https://github.com/plotly/plotly.py/releases/tag/v7.0.0 (`plotly/plotly.py@v7.0.0`, `S10`)
- **Publisher-described observation:** Plotly.py 7.0.0 bundles Plotly.js 4.0.0, removes deprecated Mapbox traces and legacy Orca/Kaleido export support, and changes certain color/MathJax behaviors.
- **Analytic implication:** A major wrapper/JS migration changes export backend, chart vocabulary and interpretation of colors/math; figure compatibility must be versioned.
- **Alternative / qualification:** A major release does not imply loss of validity of all earlier figures or successful local migration.
- **Research owner:** `K2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O10 / S10 (plotly.py v7.0.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.

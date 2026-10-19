# 2026-Q3 / 09 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-09-01 through 2026-09-30`
- Stage owner: `K / 2026-Q3`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-09-15 — Python runtime floor and parameterized datum
- **Primary source:** https://github.com/vega/altair/releases/tag/v6.3.0 (`vega/altair@v6.3.0`, `S11`)
- **Publisher-described observation:** Altair 6.3.0 drops support for Python 3.10 and supports using signals/parameters through alt.datum expressions.
- **Analytic implication:** Runtime-floor identity and parameterized grammar expression state are both necessary for replaying an interactive figure.
- **Alternative / qualification:** A documented minimum runtime is not evidence that any particular deployed environment was upgraded.
- **Research owner:** `K3` in this Stage; one originating source family, no independent validation.

### 2026-09-11 — PDF hexbin clipping and export corrections
- **Primary source:** https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2 (`matplotlib/matplotlib@v3.11.2`, `S12`)
- **Publisher-described observation:** Matplotlib 3.11.2 fixes hexbin clipping in PDF output and several other backend/text/HiDPI issues.
- **Analytic implication:** Export format and backend version can change visible evidence even when the plotting command appears identical.
- **Alternative / qualification:** A release note does not establish an issue in every hexbin image or equivalence of browser and PDF render paths.
- **Research owner:** `K4` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O11 / S11 (altair v6.3.0), O12 / S12 (matplotlib v3.11.2) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.

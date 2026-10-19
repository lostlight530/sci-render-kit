# Versioned Evidence Chart — Stage J / 2026-Q2

- Repository: `lostlight530/sci-render-kit`
- Source window: `2026-04-01 through 2026-06-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
The chart compares different primary-release events, not a quantitative time-series. Observed source text and research inference stay in separate columns.

| Object/source | Publisher statement | Interpretation | Strongest scope limit | Execution/reproduction |
|---|---|---|---|---|
| O1 / [S1](https://github.com/vega/altair/releases/tag/v6.1.0) | Updates Vega-Lite target to 6.4.1 with tooltip, stack and cursor behavior | Python wrapper and grammar engine revision are distinct | No generated spec rerun | `NOT_RUN` |
| O2 / [S2](https://github.com/matplotlib/matplotlib/releases/tag/v3.10.9) | Hardens cycler validation and LaTeX/PostScript shell-escape handling | Renderer security context differs from picture correctness | Upstream security fix is not this repo security audit | `NOT_RUN` |
| O3 / [S3](https://github.com/vega/altair/releases/tag/v6.2.0) | Updates Olli integration and fixes concat-chart parameter propagation | Assistive output and interactive parameter state are versioned | Olli integration != WCAG certification | `NOT_RUN` |
| O4 / [S4](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0) | Overhauls text/font processing using libraqm, HarfBuzz, SheenBidi and FreeType | Font shaping and language/direction affect visual identity | Not all font features supported; no local multilingual rerun | `NOT_RUN` |

## Counterevidence, negative space, review
All included sources are publisher release artifacts; no independent technical reproduction or independent contradiction search was performed. These versions do not share a common task, result variable or evaluator. Same-producer extraction and review; field-wide change or current repo behavior cannot be inferred from source counts.

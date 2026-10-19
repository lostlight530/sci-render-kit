# 2026-Q2 / 04 — monthly research reconstruction

## Time and method identity
- Repository: `lostlight530/sci-render-kit`; research month: `2026-04-01 through 2026-04-30`
- Stage owner: `J / 2026-Q2`; retrospective/research date: `2026-10-19`
- Coverage: `SOURCE_BOUNDED` to explicitly selected official release records (not exhaustive field coverage)
- State: `MONTH_RECONSTRUCTED`

## Selected events and evidence
### 2026-04-23 — Security hardening in rendering input paths
- **Primary source:** https://github.com/matplotlib/matplotlib/releases/tag/v3.10.9 (`matplotlib/matplotlib@v3.10.9`, `S4`)
- **Publisher-described observation:** Matplotlib 3.10.9 release notes describe security-hardening changes in cycler validation, LaTeX and PostScript shell invocation.
- **Analytic implication:** Figure production can cross executable or template boundaries; dependency/execution sandbox state belongs beside image provenance.
- **Alternative / qualification:** A release advisory does not establish that an actual target repository was exploitable.
- **Research owner:** `J1` in this Stage; one originating source family, no independent validation.

### 2026-04-21 — Declarative grammar target update
- **Primary source:** https://github.com/vega/altair/releases/tag/v6.1.0 (`vega/altair@v6.1.0`, `S5`)
- **Publisher-described observation:** Altair 6.1.0 updates Vega-Lite to 6.4.1 and reports tooltip behavior and related feature adjustments.
- **Analytic implication:** Python wrapper version and grammar/compiler target are distinct identifiers for generated visualization specs.
- **Alternative / qualification:** Library-side grammar support does not certify output equivalence, accessibility or local notebook behavior.
- **Research owner:** `J2` in this Stage; one originating source family, no independent validation.


## Month-to-quarter relation
Selected release objects O4 / S4 (matplotlib v3.10.9), O5 / S5 (altair v6.1.0) feed the Stage's separate Research Parts and source/chart registers. Monthly chronology records facts and bounded implications, not a substitute for Stage-level synthesis.

## Stable boundary / month decision
`APPEND_RELATION — SOURCE_BOUNDED_SELECTED_RELEASE`. render success != scientific validity; claim binding != entailment; uncertainty metadata != statistical validation; accessibility support != WCAG certification; checksum != independent reproduction.
No `sci-render-kit` runtime, experimental benchmark, scientific result or contract state was independently verified in this month reconstruction.

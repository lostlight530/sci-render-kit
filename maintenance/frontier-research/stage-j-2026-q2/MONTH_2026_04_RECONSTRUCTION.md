# Frontier Research Stage J / 2026-Q2 — 2026-04 monthly research reconstruction
- Source period: 2026-04; retrospective reconstruction/record 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Grammar, prerelease and modern text shaping. Evidence-object count: 1; **not** a measure of field-wide activity.
## 2026-04-21 — Vega-Lite target and data-spec hashes (`J-O1`)
**Publisher source:** [vega/altair v6.1.0](https://github.com/vega/altair/releases/tag/v6.1.0) (`J-S1`).
**Observed release note:** Altair updates Vega-Lite 6.4.1 and fixes hash collisions between structurally identical specs using different data.
**Analysis:** Declarative spec and bound data identity must be retained separately; tooltip/cursor grammar can vary with runtime.
**Alternative / caution:** No generated-spec equality or parameter test was executed.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.

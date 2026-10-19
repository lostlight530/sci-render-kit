# Frontier Research Stage J / 2026-Q2 — quarterly research synthesis
## Identity
- `lostlight530/sci-render-kit`; study window 2026-04-01–2026-06-30; reconstructed/synthesized 2026-10-19; `SOURCE_BOUNDED / COMPLETE`.
- `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; not contemporaneous execution, systematic review, or independently verified result.
## Question revisited
**Grammar, prerelease and modern text shaping:** what evidentiary boundary changed in this selected three-month history?
## Month and Part inputs
- [2026-04](MONTH_2026_04_RECONSTRUCTION.md)
- [2026-05](MONTH_2026_05_RECONSTRUCTION.md)
- [2026-06](MONTH_2026_06_RECONSTRUCTION.md)
- [Part J1: Vega-Lite target and data-spec hashes](J1_VEGA_LITE_TARGET_AND_DATA_SPEC_HASHES.md) — [vega/altair v6.1.0](https://github.com/vega/altair/releases/tag/v6.1.0), 2026-04-21
- [Part J2: Matplotlib pre-GA compatibility](J2_MATPLOTLIB_PRE_GA_COMPATIBILITY.md) — [matplotlib/matplotlib v3.11.0rc2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2), 2026-05-13
- [Part J3: Text/font shaping overhaul](J3_TEXT_FONT_SHAPING_OVERHAUL.md) — [matplotlib/matplotlib v3.11.0](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0), 2026-06-12
## Source selection, method and appraisal
Executed 2026-10-19: publisher release-index enumeration and exact tag reads; chose 3 release objects in Grammar, prerelease and modern text shaping. These are publisher-origin product/specification/version statements. `SOURCE_BOUNDED` is the only coverage claim. Comparison uses research-question, versioned mechanism, time and evidence authority, not benchmark scores or number of announcements. Same-origin releases are related but not independent corroboration.
## Substantive quarter narrative
### 1. Vega-Lite target and data-spec hashes (2026-04-21)
**Evidence:** Altair updates Vega-Lite 6.4.1 and fixes hash collisions between structurally identical specs using different data. [Source](https://github.com/vega/altair/releases/tag/v6.1.0).
**Meaning:** Declarative spec and bound data identity must be retained separately; tooltip/cursor grammar can vary with runtime.
**Counter-reading:** No generated-spec equality or parameter test was executed.

### 2. Matplotlib pre-GA compatibility (2026-05-13)
**Evidence:** Matplotlib explicitly labels 3.11.0rc2 as a release candidate addressing downstream and deprecation issues. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2).
**Meaning:** Release candidate availability is not stable release availability; its status and dates require separate treatment.
**Counter-reading:** No RC install or downstream matrix execution; not a GA claim.

### 3. Text/font shaping overhaul (2026-06-12)
**Evidence:** Matplotlib 3.11.0 reports font/text processing changes using libraqm, HarfBuzz, SheenBidi and FreeType. [Source](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0).
**Meaning:** Font shaping and bidi layout can change human-readable figure meaning, separate from plotting data.
**Counter-reading:** Release admits some font library features remain unsupported; no RTL output audit.

## Cross-Part interpretation
The common research movement is **grammar, prerelease and modern text shaping**: selected release records reveal multiple distinct states—declared interface, effective runtime/configuration, action or rendering behavior, verification output and wider research interpretation. These states must not be collapsed. Different version families and software domains are not statistically comparable; there is no controlled common outcome metric.
## What persisted, failed to be shown and remains unknown
- Hard boundaries: `render success != scientific validity; accessibility support != WCAG certification; checksum != reproduction; profile != publisher acceptance`.
- Publisher release statement != current target repo capability; a fix is not evidence that this repo had the associated defect.
- No local native experiment, exact-version reproduction, formal citation chaining, implementation-conformance audit, independent counterevidence study or peer review.
- Historical event/publication dates were not backdated from 2026-10-19; source-family selection bias and missing independent validation persist.
## Review and current repository boundary
[Producer Research Review](RESEARCH_REVIEW.md); `SAME_PRODUCER_REVIEW`. Local implementation drift = `NOT_AUDITED`; active-contract drift = `NOT_AUDITED`; runtime change = `NO`; contract change = `NO`.
## Conclusion
`FRONTIER_STAGE_COMPLETE` only within the declared retrospective `SOURCE_BOUNDED` research scope. This is a knowledge artifact and [bounded handoff](STAGE_HANDOFF.md), not a certificate of scientific correctness, performance or project implementation.

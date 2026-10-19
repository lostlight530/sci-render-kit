# Frontier Research Stage J / 2026-Q2 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| J-O1 / v6.1.0 | Altair updates Vega-Lite 6.4.1 and fixes hash collisions between structurally identical specs using different data. | Declarative spec and bound data identity must be retained separately; tooltip/cursor grammar can vary with runtime. | No generated-spec equality or parameter test was executed. |
| J-O2 / v3.11.0rc2 | Matplotlib explicitly labels 3.11.0rc2 as a release candidate addressing downstream and deprecation issues. | Release candidate availability is not stable release availability; its status and dates require separate treatment. | No RC install or downstream matrix execution; not a GA claim. |
| J-O3 / v3.11.0 | Matplotlib 3.11.0 reports font/text processing changes using libraqm, HarfBuzz, SheenBidi and FreeType. | Font shaping and bidi layout can change human-readable figure meaning, separate from plotting data. | Release admits some font library features remain unsupported; no RTL output audit. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.

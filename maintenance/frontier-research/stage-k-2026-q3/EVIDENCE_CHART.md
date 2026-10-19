# Evidence Chart — K/2026-Q3

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | bundled plotly.js update to 3.7.0 and marginal type validation | Validation failure paths and JS renderer version are separate communication evidence from scientific-data input; unsupported configurations should be recorded, not silently redrawn. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | Plotly.js 4.0, removed Mapbox/Orca/legacy Kaleido and Figure Factory APIs | Major upgrades can remove exporters and traces, change MathJax/color parsing and transform chart output identity; compatibility requires explicit migration rather than an assumed equivalent figure. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | Python 3.10 dropped; parameterized datum expressions and stricter errors | Environment support floor and spec-expression generation jointly affect reproducible chart execution; a stricter TypeError is a different failure state from silently ignored arguments. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F4 | O4 / S4 | PDF hexbin clipping and WebAgg/HiDPI rendering bug fixes | Static PDF export and interactive WebAgg/HiDPI output occupy different rendering surfaces, both version-sensitive. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.

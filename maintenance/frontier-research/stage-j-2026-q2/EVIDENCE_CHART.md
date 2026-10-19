# Evidence Chart — J/2026-Q2

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | Vega-Lite 6.4.1 target with tooltip newline, stacking and pointer changes | Updating a declarative wrapper can change tooltip rendering, color/stack relationships and interaction cues even when a source chart expression is unchanged. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | atomic dataset-cache writes | Cache writing is a separate file/dataset state in visualization provenance; atomicity reduces certain interrupted-write risks but does not certify dataset identity or chart semantics. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | text/font processing overhaul using shaping and bidi libraries | Text glyph shaping and bidirectional language layout influence what a figure communicates, and depend on font/renderer/library state as well as labels and data. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.

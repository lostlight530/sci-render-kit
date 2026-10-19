# Evidence Chart — I/2026-Q1

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | Plotly Express template trace-specific color sequences corrected | Template-dependent trace styling is part of the rendered communication contract; a corrected mapping can change what viewers perceive while the data remain identical. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | bundled plotly.js 3.4.0 with legend-title interaction changes and export warning correction | Interaction semantics and image-export diagnostics can change together in a patch/minor wrapper line; distinguish Python wrapper and JS renderer revision. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.

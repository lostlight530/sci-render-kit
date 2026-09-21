# Frontier Research Part B1 — Versioned Visual Semantics

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

What do Q2 plotting-library releases show about version-dependent visual decoding and execution semantics

## Objects and sources

- O1 ggplot2 3.5.1
- O2 Vega-Lite 5.18/5.19
- O3 Matplotlib 3.9
- S1 https://ggplot2.tidyverse.org/news/index.html
- S2 https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
- S3 https://matplotlib.org/3.10.5/users/prev_whats_new/whats_new_3.9.0.html

## Observations

ggplot2 3.5.1, released 2024-04-23, explicitly focused on regressions from 3.5.0 and included fixes affecting discrete scales, secondary-axis warnings, patterns/gradients, resolution behavior, and ordering in binned/colour-step guides

Vega-Lite 5.18.0 on 2024-04-09 added an explicit density-resolution option and changed its default behavior; 5.18.1 on 2024-05-07 fixed non-linear stacked bars, null placement, and transform-name collision; 5.19.0 on 2024-06-14 expanded options/examples for representing invalid data such as nulls and NaNs

Matplotlib 3.9.0 on 2024-05-15 added or changed legend support, layout/zorder behavior, mathtext spacing, exact 3D-axis limits, and introduced BackendRegistry as a single source of truth for available backends

## Analysis

The data may stay fixed while the viewer-facing artifact changes because library version, guide logic, invalid-data policy, backend selection, or layout semantics changed

Therefore:

    same data/spec
    != same rendered communication state

BackendRegistry is especially useful as evidence that execution backend identity is part of the render context rather than incidental environment detail

## Counterevidence

Release notes establish project-described changes, not the scientific materiality of every change

No cross-version rerender was performed

## Conclusion

SUPPORTED_OBSERVATION

Q2 strengthens the need to bind figure evidence to versioned rendering and visual-semantics context

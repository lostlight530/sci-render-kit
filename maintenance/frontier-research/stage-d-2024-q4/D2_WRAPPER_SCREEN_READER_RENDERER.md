# D2 — Wrapper-Level Screen-Reader Renderer

## Question
What changes when a visualization wrapper exposes an explicit renderer optimized for screen readers?

## Object and source
- O4: Vega-Altair 5.5.0, released 2024-11-24.
- S4: https://github.com/vega/altair/releases

## Observations
Altair 5.5.0 introduced a new renderer optimized for screen readers and also changed its theme system. This is wrapper-level communication behavior: the high-level Python object can now be routed through a different representation path.

## Analysis
The feature strengthens Stage C's wrapper-version lesson:

```text
chart specification
+ Altair revision
+ renderer selection
+ renderer implementation
+ assistive-technology context
= communication state
```

The mere presence of a screen-reader-oriented renderer is capability evidence. It is not evidence that every chart is semantically equivalent across visual and non-visual renderers, nor that every screen reader/user workflow is validated.

## Counterevidence / limits
- No Altair 5.5 screen-reader run was executed locally.
- No cross-renderer semantic-equivalence study was performed.
- No universal accessibility or WCAG-conformance claim follows.

## Conclusion
`SUPPORTED_CAPABILITY_BOUNDARY`.

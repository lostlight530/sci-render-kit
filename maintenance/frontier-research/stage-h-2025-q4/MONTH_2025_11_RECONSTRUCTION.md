# November 2025 Reconstruction — Stage H

## Selected events
- Plotly.py 6.4.0 — 2025-11-04
- Altair 6.0.0 — 2025-11-12
- Plotly.py 6.5.0 — 2025-11-17

## Narrative
November concentrates the wrapper/engine boundary. Plotly.py changes the bundled Plotly.js and interaction/input semantics while Altair moves to Vega-Lite 6.1.0 and changes wrapper/runtime properties.

The common lesson is not that these libraries converge. It is that a Python plotting package is often a compiler/wrapper around another semantic layer whose revision must remain visible.

## Boundary
Same-month releases from separate projects are independent project facts but do not form a formal interoperability claim.

## Decision
`APPEND_RELATION — WRAPPER_ENGINE_IDENTITY_STRENGTHENED`

# F3 — Delivery Integrity and Accessibility Metadata

## Evidence
Plotly.py 6.2.0 was released in June 2025 and added Subresource Integrity hash support for CDN script tags when `include_plotlyjs='cdn'`, along with Plotly.js path configuration and image-export deprecation signaling.

Vega-Lite 6.2.0 is dated 2025-06-27 and includes a fix to propagate temporal fields to time expressions and disables ARIA on the generated Voronoi layer used by nearest selections.

Sources:
- https://github.com/plotly/plotly.py/releases/tag/v6.2.0
- https://github.com/vega/vega-lite/blob/main/CHANGELOG.md

## Analysis
Stage E made runtime/package identity explicit. Stage F adds delivery-integrity and accessibility-tree behavior.

```text
CDN resource referenced
+ SRI hash
-> browser integrity check capability

SRI check
!= publisher/scientific trust

ARIA behavior changed
!= WCAG certification
```

Communication provenance may include how code is delivered and what accessibility metadata is emitted, while remaining distinct from scientific entailment.

## Outcome
`SUPPORTED_OBSERVATION`

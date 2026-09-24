# E1 — Plotly.py 6.0 Serialization, Wrapper and Renderer Identity

## Research question
When a visualization wrapper changes its JS major version, serialization path, widget integration and map backend direction at once, which identities belong to communication provenance?

## Evidence
Plotly.py v6.0.0 was released 2025-01-28. Its official release notes include:
- Plotly.js update from 2.34.2 to 3.0.0;
- removal of deprecated trace/attribute surfaces;
- Mapbox-based trace deprecation in favor of MapLibre migration;
- base64 encoding of typed arrays in Plotly JSON;
- `FigureWidget` migration to `anywidget`;
- native ES6 import for loading plotly.js;
- a LaTeX rendering fix for modern Jupyter environments.

Source: https://github.com/plotly/plotly.py/releases/tag/v6.0.0

## Analysis
A scientific figure is not identified only by data plus a nominal plotting call. Wrapper version, JS engine version, serialization path, widget host and backend family can alter communication behavior.

~~~text
same data
+ same high-level plotting intent
+ different wrapper/runtime/serialization stack
!= same communication state
~~~

Typed-array encoding and loader changes are provenance-relevant even when visual output appears similar. Map backend migration is a platform identity change, not merely styling.

## Limits
No local Plotly render, Jupyter replay, MapLibre migration test or pixel/semantic comparison was executed.

## Outcome
`SUPPORTED_OBSERVATION`
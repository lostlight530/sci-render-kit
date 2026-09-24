# Evidence Chart — Stage E / 2025-Q1

| Finding | Object | Communication/provenance axis | Boundary |
|---|---|---|---|
| wrapper/JS major and serialization path affect figure identity | Plotly.py 6.0 | wrapper + JS runtime + JSON encoding | feature/release != local render |
| map backend migration changes platform context | Plotly.py 6.0 | Mapbox → MapLibre direction | migration != semantic equivalence |
| patch release can alter concrete render behavior | Matplotlib 3.10.1 | renderer revision | bugfix != all prior artifacts invalid |
| declarative spec requires compiler/runtime major identity | Vega-Lite 6.0 | grammar + compiler + Vega runtime | spec text != derivative identity |
| package/module environment is part of deployment provenance | Plotly/Vega-Lite | ES6/ESM/widget integration | deployability != scientific validity |
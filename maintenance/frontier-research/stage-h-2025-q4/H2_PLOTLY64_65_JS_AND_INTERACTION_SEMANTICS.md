# H2 — Plotly.py 6.4/6.5: Bundled JS and Interaction Semantics

## Source identity
- Plotly.py 6.4.0 — released 2025-11-04
- Plotly.py 6.5.0 — released 2025-11-17
- Primary source: https://github.com/plotly/plotly.py/releases

## Frontier observation
Plotly.py 6.4.0 updates Plotly.js from 3.1.1 to 3.2.0 and adds interaction/display semantics such as fallback template attributes and extended SI formatting. 6.5.0 advances Plotly.js again to 3.3.0, adds hover-template support for financial traces, and fixes a datetime conversion issue.

This reinforces an identity chain already visible in Stage G:

```text
Python wrapper revision
!= bundled Plotly.js revision
!= trace/template semantics
!= input conversion behavior
!= browser/export artifact
```

## Boundary
- wrapper upgrade != semantic parity
- hover/display change != accessibility certification
- bug fix != prior artifacts invalid
- bundled JS version != browser runtime proof

## Repository interpretation
No Plotly 6.4/6.5 browser or static-export replay was executed.

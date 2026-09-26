# G2 — Plotly.py 6.3: Export Engine and Browser Identity

## Question
What changes when a scientific-visualization wrapper makes browser acquisition and its underlying JavaScript renderer revision more explicit parts of the export/runtime workflow?

## Object
- Research object: Plotly.py 6.3.0
- Release date: 2025-08-12
- Source family: Plotly.py project/PyPI release
- Authority: project release/changelog state
- Accessed: 2026-09-26

## Primary sources
- https://pypi.org/project/plotly/6.3.0/
- https://github.com/plotly/plotly.py/releases

## Observed release state
Plotly.py 6.3.0 updates the bundled/targeted Plotly.js line from 3.0.1 to 3.1.0 and exposes `plotly.io.get_chrome()`, making Chrome acquisition for image-export workflows an explicit user-facing surface. The release also includes export/runtime-related fixes.

## Interpretation
A Python figure specification is not identical to the browser/render engine that materializes it.

```text
Python wrapper
-> figure specification
-> Plotly.js revision
-> browser/Chrome runtime
-> export engine
-> image/interactive artifact
```

Once browser acquisition is part of the supported workflow, browser/runtime identity becomes harder to treat as invisible infrastructure.

This also sharpens a boundary:

```text
browser available
!= browser version/environment reproduced

export succeeded
!= scientific claim validated
```

## Negative space
No Plotly 6.3 installation, Chrome acquisition, Kaleido/image export, or browser rendering was executed locally.

## Finding
`G2_FINDING`: Q3 2025 makes export/runtime provenance more explicit: wrapper revision, JavaScript renderer revision, and browser identity can all affect the communication artifact and should not be collapsed into one "Plotly version" label.

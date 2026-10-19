# Evidence and comparison chart — Stage L / 2026-Q4

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-L1 | O13 | Plotly.js 4.1.2 changes responsive resizing to ResizeObserver instead of window resize events and documents image-export config in schema. | Viewport and host resize events are observable parts of interactive-figure reproducibility; host layout can modify what a recipient sees. | S13: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-10-05 |
| F-L2 | O14 | Vega-Lite 6.5.0 fixes image-mark center alignment when a secondary channel is undefined. | Compiler revision changes spatial interpretation of a declarative spec even without changed data. | S14: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-10-08 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `sci-render-kit` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.

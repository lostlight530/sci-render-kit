# Evidence and comparison chart — Stage I / 2026-Q1

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-I1 | O1 | Vega-Lite 6.4.2 fixes tooltip custom formatter behavior and legend merging with explicit scale/range/domain. | A stable high-level spec may acquire different tooltip/legend behavior under a patch-level compiler revision. | S1: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-01-14 |
| F-I2 | O2 | Plotly.js 3.4.0 adds clickable legend titles to toggle groups, multi-axis shape references and dashed marker lines. | Interactive figure semantics depend on the JS engine revision and user action, not just a static image. | S2: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-02-20 |
| F-I3 | O3 | Plotly.py 6.6.0 fixes a global warning-format side effect and a spurious write_image engine deprecation warning, and updates its underlying JS. | A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe. | S3: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-03-02 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `sci-render-kit` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.

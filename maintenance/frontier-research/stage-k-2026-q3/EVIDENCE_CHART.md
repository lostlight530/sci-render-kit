# Evidence and comparison chart — Stage K / 2026-Q3

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-K1 | O9 | Matplotlib 3.11.1 addresses 3D axis inversion/clipped labels, layout sharing, font glyphs and other patch-level defects. | Plot correctness questions include coordinate orientation and label visibility as renderer outcomes, not only artistic appearance. | S9: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-07-18 |
| F-K2 | O10 | Plotly.py 7.0.0 bundles Plotly.js 4.0.0, removes deprecated Mapbox traces and legacy Orca/Kaleido export support, and changes certain color/MathJax behaviors. | A major wrapper/JS migration changes export backend, chart vocabulary and interpretation of colors/math; figure compatibility must be versioned. | S10: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-08-25 |
| F-K3 | O11 | Altair 6.3.0 drops support for Python 3.10 and supports using signals/parameters through alt.datum expressions. | Runtime-floor identity and parameterized grammar expression state are both necessary for replaying an interactive figure. | S11: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-09-15 |
| F-K4 | O12 | Matplotlib 3.11.2 fixes hexbin clipping in PDF output and several other backend/text/HiDPI issues. | Export format and backend version can change visible evidence even when the plotting command appears identical. | S12: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-09-11 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `sci-render-kit` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.

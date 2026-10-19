# Evidence and comparison chart — Stage J / 2026-Q2

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-J1 | O4 | Matplotlib 3.10.9 release notes describe security-hardening changes in cycler validation, LaTeX and PostScript shell invocation. | Figure production can cross executable or template boundaries; dependency/execution sandbox state belongs beside image provenance. | S4: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-04-23 |
| F-J2 | O5 | Altair 6.1.0 updates Vega-Lite to 6.4.1 and reports tooltip behavior and related feature adjustments. | Python wrapper version and grammar/compiler target are distinct identifiers for generated visualization specs. | S5: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-04-21 |
| F-J3 | O6 | Plotly.js 3.5.1 fixes cases where axis.minallowed values inadvertently reversed an axis. | An axis-boundary renderer bug can materially invert visual presentation without a change in source data. | S6: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-05-01 |
| F-J4 | O7 | Matplotlib 3.11.0 overhauls text/font processing using libraqm, HarfBuzz, SheenBidi and updated FreeType for broader international script behavior. | Font shaping, bidirectionality and native dependency revisions become part of plot provenance, particularly for labels and uncertainty annotation. | S7: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-06-12 |
| F-J5 | O8 | Altair 6.2.2 fixes layered concat view-name collisions and includes layered concat views in selection parameters. | Generated spec identity includes selection/view naming; rerun or composition can change interactive semantics without data edits. | S8: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-06-23 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `sci-render-kit` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.

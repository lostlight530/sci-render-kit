# Longitudinal Frontier Research — 2026 year-to-date (through 2026-10-19)

## Identity and research question
- Repository `lostlight530/sci-render-kit`; event windows Jan 1–Oct 19, 2026; synthesis/reconstruction date 2026-10-19
- Status: `IN_PROGRESS / YEAR_OPEN`; not calendar-year complete
- Coverage: `SOURCE_BOUNDED` to selected official upstream release notes, not comprehensive source search, independent replay or local experiment.
- Eligible closed Stages: I, J, K. Stage L / Q4 is **OPEN**, with October month evidence and no future months.
- Question: How do selected 2026 releases change the meaning and identity of scientific communication, versioned figure/rendering state, accessibility, reproducibility, uncertainty display and publisher transfer without turning release claims into repository runtime or scientific truth?

## Month-to-quarter-to-YTD input and evidence
| Quarter Stage | Monthly window | Selected research objects | Review status |
|---|---|---|---|
| [I / 2026-Q1](../stage-i-2026-q1/STAGE_SYNTHESIS.md) | 2026-01, 2026-02, 2026-03 | vega-lite v6.4.2; plotly.js v3.4.0; plotly.py v6.6.0 | SOURCE_BOUNDED / same-producer review |
| [J / 2026-Q2](../stage-j-2026-q2/STAGE_SYNTHESIS.md) | 2026-04, 2026-05, 2026-06 | matplotlib v3.10.9; altair v6.1.0; plotly.js v3.5.1; matplotlib v3.11.0; altair v6.2.2 | SOURCE_BOUNDED / same-producer review |
| [K / 2026-Q3](../stage-k-2026-q3/STAGE_SYNTHESIS.md) | 2026-07, 2026-08, 2026-09 | matplotlib v3.11.1; plotly.py v7.0.0; altair v6.3.0; matplotlib v3.11.2 | SOURCE_BOUNDED / same-producer review |
| [L / 2026-Q4](../stage-l-2026-q4/STAGE_BRIEF.md) | October 1–19 **only** | plotly.js v4.1.2; vega-lite v6.5.0 | `OPEN / PARTIAL_REVIEW_ONLY`; NOT annual/quarter close |

Each month's primary evidence is in its Stage's `MONTH_2026_MM_RECONSTRUCTION.md`; every selected event is linked to a versioned upstream release record, an independent Research Part, and the Stage object/chart registry. A month with `NO_SELECTED_OBJECT_IN_DECLARED_SOURCE_SET` is a legitimate limitation, not grounds to fabricate a monthly breakthrough.

## Timeline and turning points
### 2026-Q1
- 2026-01-14 / vega-lite v6.4.2: Vega-Lite 6.4.2 fixes tooltip custom formatter behavior and legend merging with explicit scale/range/domain. Research inference: A stable high-level spec may acquire different tooltip/legend behavior under a patch-level compiler revision.
- 2026-02-20 / plotly.js v3.4.0: Plotly.js 3.4.0 adds clickable legend titles to toggle groups, multi-axis shape references and dashed marker lines. Research inference: Interactive figure semantics depend on the JS engine revision and user action, not just a static image.
- 2026-03-02 / plotly.py v6.6.0: Plotly.py 6.6.0 fixes a global warning-format side effect and a spurious write_image engine deprecation warning, and updates its underlying JS. Research inference: A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe.


### 2026-Q2
- 2026-04-23 / matplotlib v3.10.9: Matplotlib 3.10.9 release notes describe security-hardening changes in cycler validation, LaTeX and PostScript shell invocation. Research inference: Figure production can cross executable or template boundaries; dependency/execution sandbox state belongs beside image provenance.
- 2026-04-21 / altair v6.1.0: Altair 6.1.0 updates Vega-Lite to 6.4.1 and reports tooltip behavior and related feature adjustments. Research inference: Python wrapper version and grammar/compiler target are distinct identifiers for generated visualization specs.
- 2026-05-01 / plotly.js v3.5.1: Plotly.js 3.5.1 fixes cases where axis.minallowed values inadvertently reversed an axis. Research inference: An axis-boundary renderer bug can materially invert visual presentation without a change in source data.
- 2026-06-12 / matplotlib v3.11.0: Matplotlib 3.11.0 overhauls text/font processing using libraqm, HarfBuzz, SheenBidi and updated FreeType for broader international script behavior. Research inference: Font shaping, bidirectionality and native dependency revisions become part of plot provenance, particularly for labels and uncertainty annotation.
- 2026-06-23 / altair v6.2.2: Altair 6.2.2 fixes layered concat view-name collisions and includes layered concat views in selection parameters. Research inference: Generated spec identity includes selection/view naming; rerun or composition can change interactive semantics without data edits.


### 2026-Q3
- 2026-07-18 / matplotlib v3.11.1: Matplotlib 3.11.1 addresses 3D axis inversion/clipped labels, layout sharing, font glyphs and other patch-level defects. Research inference: Plot correctness questions include coordinate orientation and label visibility as renderer outcomes, not only artistic appearance.
- 2026-08-25 / plotly.py v7.0.0: Plotly.py 7.0.0 bundles Plotly.js 4.0.0, removes deprecated Mapbox traces and legacy Orca/Kaleido export support, and changes certain color/MathJax behaviors. Research inference: A major wrapper/JS migration changes export backend, chart vocabulary and interpretation of colors/math; figure compatibility must be versioned.
- 2026-09-15 / altair v6.3.0: Altair 6.3.0 drops support for Python 3.10 and supports using signals/parameters through alt.datum expressions. Research inference: Runtime-floor identity and parameterized grammar expression state are both necessary for replaying an interactive figure.
- 2026-09-11 / matplotlib v3.11.2: Matplotlib 3.11.2 fixes hexbin clipping in PDF output and several other backend/text/HiDPI issues. Research inference: Export format and backend version can change visible evidence even when the plotting command appears identical.

### 2026-Q4 OPEN, as of October 19
- 2026-10-05 / plotly.js v4.1.2: Plotly.js 4.1.2 changes responsive resizing to ResizeObserver instead of window resize events and documents image-export config in schema. Research interpretation: Viewport and host resize events are observable parts of interactive-figure reproducibility; host layout can modify what a recipient sees.
- 2026-10-08 / vega-lite v6.5.0: Vega-Lite 6.5.0 fixes image-mark center alignment when a secondary channel is undefined. Research interpretation: Compiler revision changes spatial interpretation of a declarative spec even without changed data.
These events are **candidate ongoing Stage L findings**, not a completed-quarter synthesis.

## Cross-Stage synthesis, conflict and comparability
Stage H / 2025-Q4 distinguished dependency floors, Python wrapper, grammar/JS renderer and generated spec identity; a successful render remained non-validating.
The 2026 selected releases collectively emphasize versioned state and the need to preserve source/implementation boundary. Their heterogeneity is material: upstream project releases are not independent experimental replications of one hypothesis; they do not share one population, metric or quality score. A field-wide improvement curve is `NOT_COMPARABLE`. Counterargument: the apparent progression may be selection bias toward changes that match this repository's lens.

## Longitudinal comparison table
| Dimension | 2025 Stage H inheritance | 2026 closed Stages | Open Stage L | Validation |
|---|---|---|---|---|
| Source authority | selected project standards/releases | official versioned release records | published October releases only | not independently reproduced |
| Temporal model | retrospective quarter | retrospective Jan–Sep Stage | as-of October observation | dates recorded, no backprojection |
| Repository implication | bounded non-normative research | potential questions; no direct drift audit | open research/watch only | runtime and contract not tested |
| Research maturity | Stage H complete | I–K source-bounded document studies complete | October only; no closed stage | review same producer, not independent |

## Current boundary and correction route
The previously merged 2025 annual and A–H longitudinal documents retain their cutoffs. The old index statement `Stage I NOT_EVIDENCED` was a true **earlier-index observation** before this proposed new Stage I record; it must not be silently erased. This dated result supplies new evidence of native Stage I–K **documentation creation**, not retroactive evidence of executions, benchmark studies, runtime fixes or independently validated science. No archive member, old Stage or old snapshot is rewritten.

## Year status and future work
`2026_YEAR_OPEN / NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE`.
Do not create November/December events before they occur; do not issue a 2026 annual complete file before quarter/year close. Needed next: source-family triangulation, exact revision-based replay where appropriate, independent review, current repo audits under native governance and later dated correction notes.

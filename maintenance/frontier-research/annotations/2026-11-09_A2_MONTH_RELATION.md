# Independent A2 — sci-render-kit — 2026-11-09 Stage L month relations

## Identity and fresh-main gate
- Repository: `lostlight530/sci-render-kit`; task: `independent-maintenance/A2`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 23:20:01 +08:00.
- A1-before-A2 order: satisfied. A1 [PR #229](https://github.com/lostlight530/sci-render-kit/pull/229) is merged.
- Fresh main after A1 merge: `b503ef21e0f1e95acbb0e334181bed7116b44278`.
- Exact merged A1 blob: `469fe5c7d5f304020597beed460ba8a902eee7ad`.
- Prior A2 Nov08: `maintenance/frontier-research/annotations/2026-11-08_A2_MONTH_RELATION.md` @ `636d0d10b38794156ddb5d23a013a94d72b9432d`.

## Current Stage-L and maintenance inputs
| Object | Exact blob | Role |
|---|---|---|
| `maintenance/2026-11-08-d7-operational-continuity.md` | `1af8d2977ef18392a11a633b35ba9fcbc95bc1e3` | D7 continuity record |
| `maintenance/frontier-research/LONGITUDINAL_INDEX.md` | `d06bc9611faa6c103d97cb69fc966825084a25d4` | pre-A2 current pointer |
| `stage-l-2026-q4/STAGE_BRIEF.md` | `96129b7b7b3ce4a9f6c7bfe5784a7fb1935bd43f` | Stage L boundary |
| `stage-l-2026-q4/L1_PLOTLYJS_V412.md` | `eb7b941a5d7327f2fa4543f21082102ba93bcf41` | selected Plotly.js 4.1.2 |
| `stage-l-2026-q4/L2_VEGALITE_V650.md` | `e0e5bdf11779395531d7b1338bc2cdef6323b5b8` | selected Vega-Lite 6.5.0 |

## Month-relation judgments
1. Stage L remains a 2026-Q4 research object, IN_PROGRESS, with selected source cut 2026-10-19.
2. Plotly.js 4.1.2 and Vega-Lite 6.5.0 remain the selected source objects; later upstream releases are candidates, not silent baseline replacements.
3. No new Stage-L renderer source observation, browser run, DOM measurement or screenshot evaluation is recorded for Nov09.
4. The Nov08 D7 report and Nov08 A1/A2 files are present; D7 is a separate periodic-audit owner and not a renderer experiment.
5. The current LONGITUDINAL_INDEX still points through Nov07 even though the Nov08 A2 relation is merged. This is a stale navigation pointer, not missing Nov08 content.
6. This A2 advances the current relation pointer to Nov09 and preserves Nov08 A2 as the prior dated relation.
7. Plotly.js and the Plotly Python wrapper have separate package and runtime identities; a matching version label does not establish export parity.
8. Vega-Lite grammar and compiled Vega specification are distinct representations; a chart's visual similarity does not prove semantic equivalence.
9. A sidecar hash authenticates bytes, not chart semantics, axis correctness, accessibility or scientific source truth.
10. Browser SVG, Canvas and PNG export can differ with fonts, locale, device scale and browser engine.
11. Responsive resize is a runtime property and requires an actual DOM resize sequence; a static screenshot cannot establish it.
12. No browser render, screenshot comparison, DOM/accessibility audit, package runtime or independent renderer conformance was executed by this A2.
13. The index pointer update changes navigation only; Stage Brief, source selection, MANIFEST calendar state and prior D7 report remain unchanged.
14. November remains OPEN; Nov10–30 are NOT_DUE.

## Current calendar and ownership matrix
| Owner | Current state | A2 decision |
|---|---|---|
| November 2026 | OPEN | continue |
| Stage L 2026-Q4 | IN_PROGRESS; selected source cut 2026-10-19 | preserve |
| D7 Nov08 | separate periodic audit | preserve |
| A1 Nov09 | merged | consume as upstream |
| A2 Nov09 | this relation | advance index pointer |
| Nov10–30 | NOT_DUE | no future-state inference |

- This A2 is a relation checkpoint, not a Stage-L renderer execution.
- No native source, renderer implementation, browser environment or Stage calendar state is changed.
- Result: `A2_MONTH_RELATION_DELIVERED / NOVEMBER_OPEN / STAGE_L_IN_PROGRESS / INDEX_ADVANCED_TO_NOV09`.

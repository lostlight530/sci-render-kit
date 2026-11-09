# Independent A1 — sci-render-kit — 2026-11-09 Stage L source custody

## Identity and scope
- Repository: `lostlight530/sci-render-kit`; task: `independent-maintenance/A1`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 23:10:21 +08:00.
- A1 scope: Nov01–08 inclusive; Nov09 is reserved for A2.
- Exact pre-write main: `7aeb282384834ca0bd5f6e8adc07f1ed06fea6ad`.
- Prior A1 Nov01–07: `maintenance/frontier-research/annotations/2026-11-08_A1_STAGE_SOURCE_CONTENT.md` @ `c35c1f6cecba7620a9875ff2b86950ec27a4441e`.
- Prior A2 Nov08: `maintenance/frontier-research/annotations/2026-11-08_A2_MONTH_RELATION.md` @ `636d0d10b38794156ddb5d23a013a94d72b9432d`.
- D7 Nov08: `maintenance/2026-11-08-d7-operational-continuity.md` @ `1af8d2977ef18392a11a633b35ba9fcbc95bc1e3`.
- Current index: `maintenance/frontier-research/LONGITUDINAL_INDEX.md` @ `d06bc9611faa6c103d97cb69fc966825084a25d4`.
- The 2026-09-25 SOP defines month-to-date coverage and merge-first A1→A2 sequencing, not a universal 100-lines-per-PR threshold.

## Exact Stage and D7 source custody
| Object | Blob SHA | Role |
|---|---|---|
| `stage-l-2026-q4/STAGE_BRIEF.md` | `96129b7b7b3ce4a9f6c7bfe5784a7fb1935bd43f` | Stage L scope and selected-source boundary |
| `stage-l-2026-q4/L1_PLOTLYJS_V412.md` | `eb7b941a5d7327f2fa4543f21082102ba93bcf41` | selected Plotly.js 4.1.2 object |
| `stage-l-2026-q4/L2_VEGALITE_V650.md` | `e0e5bdf11779395531d7b1338bc2cdef6323b5b8` | selected Vega-Lite 6.5.0 object |
| `LONGITUDINAL_INDEX.md` | `d06bc9611faa6c103d97cb69fc966825084a25d4` | current routing/index |
| `2026-11-08-d7-operational-continuity.md` | `1af8d2977ef18392a11a633b35ba9fcbc95bc1e3` | D7 operational continuity |

## Nov08-specific findings and decisions
1. Stage L selected Plotly.js 4.1.2 and Vega-Lite 6.5.0 under the October19 source cutoff; later release candidates do not automatically replace the frozen selection.
2. Plotly.js and the Plotly Python wrapper have separate package, runtime and export version identities.
3. Vega-Lite declarative grammar and compiled Vega rendering specification are distinct intermediate representations.
4. Similar-looking Plotly and Vega-Lite charts do not prove axis transformations, scale semantics or data lineage agree.
5. A Plotly alignment patch in one rendering path does not establish parity across browser SVG, Canvas and PNG exports.
6. Pixel identity depends on fonts, locale, device scale and browser engine, not only the figure specification hash.
7. A sidecar hash authenticates bytes, not chart semantics, accessibility, axis correctness or scientific source truth.
8. Responsive container resize is a runtime property and needs an actual DOM resize sequence; a static screenshot cannot prove it.
9. The D7 report records six Nov02–07 A1/A2 pairs; those are maintenance entries, not six native Stage-L renderer experiments.
10. D7 records no native screenshot/DOM/accessibility evaluation and no independent 100-line semantic certification; no such result is inferred here.
11. Nov08 A1/A2 files are present on main, but the LONGITUDINAL_INDEX still points current relation through Nov07; this is a current routing gap after the Nov08 A2 merge.
12. The Nov08 D7 pointer correction from Nov06 to Nov07 remains a valid historical event; the Nov08 A2 is a later dated relation and must not be backdated.
13. Stage L remains IN_PROGRESS and November remains OPEN; neither is closed by a pointer update.
14. No local browser render, screenshot comparison, DOM/accessibility audit, publisher runtime or independent renderer conformance was executed by this A1.

## Month-to-date coverage and decision matrix
| Window | Evidence owner | Decision |
|---|---|---|
| Nov01 | Prior A1 / month-start baseline | INHERIT_PRIOR_A1 |
| Nov02–07 | Prior A1 source review | INHERIT_PRIOR_A1 |
| Nov08 | D7, index, Stage Brief, selected Plotly/Vega-Lite sources | REVIEWED; APPEND_RELATION / CURRENT_POINTER_DRIFT |
| Nov09 | Excluded from A1 | A2_INPUT_ONLY |
| Nov10–30 | Future dates | NOT_DUE |

- November remains OPEN; Stage L 2026-Q4 remains IN_PROGRESS.
- The current relation pointer requires a forward update only after this A1 merges and A2 is freshly produced.
- No Stage source, renderer implementation, MANIFEST calendar snapshot or prior research artifact is changed.
- Result: `A1_COVERAGE_COMPLETE_WITH_NOV08_D7_AND_INDEX_RECONCILIATION_IDENTIFIED`.

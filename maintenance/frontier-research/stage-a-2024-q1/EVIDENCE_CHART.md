# Evidence Chart — Stage A / 2024-Q1

## 0. Identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Charting date:** `2026-09-21`
- **Method:** single-producer structured extraction
- **Coverage:** `SEARCH_BOUNDED`

## 1. Questions served

RQ1 uncertainty/guides; RQ2 accessibility/alternate representations; RQ3 renderer/version/communication transfer.

## 2. Variables

| Variable | Meaning |
|---|---|
| representation | raster/SVG/CSV/text/interactive/static/etc. |
| visual_semantics | axes/legends/scales/marks/uncertainty encoding |
| renderer_state | library/backend/version/execution path |
| accessibility_modality | screen reader/tactile/text/data/etc. |
| validation_type | software test/user study/statistical validation/none |
| claim_binding | relation between scientific claim and figure |
| transfer_state | source -> rendered -> alternate representation |
| authority_limit | what cannot be inferred |

## 3. Object chart

| Object | Communication problem | Mechanism | Evidence | Validation state | Main limit |
|---|---|---|---|---|---|
| O1 statisticians study | inferential nuance/dichotomy | visualization in statistical reasoning | interview study | qualitative research | no universal chart prescription |
| O2 uncertainty networks | hidden uncertainty in graph relations | uncertainty-aware visualization | research paper | domain research | representation != calibration |
| O3 Chart4Blind | raster chart accessibility | SVG/CSV/alt text conversion | code + paper + user study | reported usability/accessibility study | limited chart type/workflow; no independent certification |
| O4 ggplot2 3.5 | visual decoding through scales/guides | guide-system architecture | official release | software/project evidence | no user comprehension test for every config |
| O5 Matplotlib | backend execution failures | backend bugfixes | official releases | project testing implied; not rerun | execution != scientific correctness |
| O6 Plotly | interactive/visual/serialization changes | JS/Python version updates | official releases | not rerun | version may change communication surface |
| O7 Vega-Lite | interactive tooltip/mark behavior | grammar/compiler fixes | changelog | not rerun | tooltip fix != scientific validation |
| O8 Altair | multiple renderer/large-data paths | browser/Jupyter/VegaFusion renderers | release | not rerun | same spec != identical interaction/runtime |

## 4. Finding chart

| ID | Observation | Objects | Sources | Evidence class | Boundary |
|---|---|---|---|---|---|
| F1 | visualization participates in inferential reasoning | O1 | S1 | interview research | not universal prescription |
| F2 | uncertainty can be a property requiring explicit visual communication | O2 | S2 | visualization research | display != calibrated uncertainty |
| F3 | Chart4Blind public code exists in Jan before Mar paper | O3 | S3,S4 | repository history | later paper details not backdated |
| F4 | Chart4Blind generates alternate SVG/CSV/alt-text representations | O3 | S5,S6 | paper/system report | alternate representations not assumed equivalent |
| F5 | ggplot2 defines axes/legends as guides translating visual scales back to data qualities | O4 | S7-S9 | release semantics | correct guide != valid science |
| F6 | Matplotlib backend bugs can block/harm execution | O5 | S10,S11 | software release evidence | render fix != result validation |
| F7 | Plotly 5.19 changes tick/layout/serialization behavior | O6 | S12 | release evidence | no semantic-equivalence test |
| F8 | Plotly 5.20 changes gradients/legend presentation | O6 | S13 | release evidence | visual feature != evidentiary authority |
| F9 | Vega-Lite 5.17 includes interactive tooltip/mark fixes | O7 | S14 | release evidence | interactive surface is versioned |
| F10 | Altair 5.3 exposes browser/Jupyter/VegaFusion paths | O8 | S15 | release evidence | same spec can traverse different execution paths |
| F11 | communication transfer needs provenance across representation and renderer | O3-O8 | synthesis | analytic | not external standard |

## 5. Comparative dimensions

| Object | Static/interactive | Alternate representations | Uncertainty relevance | Renderer/version relevance | Accessibility evidence |
|---|---|---|---|---|---|
| O1 | figure-oriented | not primary | high | low | not primary |
| O2 | network figures | not primary | high | not primary | not primary |
| O3 | source raster + alternate formats | high | possible but not core | conversion-system state | high |
| O4 | static/general plotting | output formats downstream | encoding semantics | library version | indirect |
| O5 | backend-dependent | multiple backend outputs | indirect | high | not evaluated |
| O6 | interactive + static paths | browser/notebook/export | encoding-dependent | high | not certified |
| O7 | interactive grammar | spec-driven outputs | encoding-dependent | high | tooltip/accessibility not universally established |
| O8 | browser/Jupyter/other paths | multiple renderer paths | encoding-dependent | high | not certified |

## 6. Counterevidence / narrowing matrix

| Simplistic claim | Narrowing evidence | Resolution |
|---|---|---|
| rendered = communicated correctly | guide/backend/tooltip changes | rejected |
| figure bound to claim = figure entails claim | uncertainty/inferential studies | rejected |
| accessible export = universally accessible | Chart4Blind scope + no independent certification | rejected |
| same chart spec = same user experience | multiple renderers/interactivity | not established |
| uncertainty band/metadata = statistically valid uncertainty | visualization evidence does not validate model calibration | rejected |
| library update = scientific improvement | release evidence is engineering state | rejected |

## 7. Negative space

- no local render matrix;
- no figure checksum/reproduction experiment;
- no WCAG certification;
- no screen-reader/tactile re-evaluation;
- no cross-renderer semantic-diff;
- no statistical recalculation behind uncertainty figures;
- no publisher acceptance/production test.

## 8. Appraisal

The quarter combines peer-reviewed/research evidence about interpretation/accessibility with direct software release evidence about rendering state. Cross-family convergence is strong around the need to preserve representation context, but no source independently validates the entire communication chain.

## 9. Amendments

Research expanded from plotting-library releases to January uncertainty/interpretation papers and Chart4Blind code/paper because the deeper Stage question required human interpretation and accessibility evidence, not only software changelogs.

## 10. Limitations

No direct reproduction means all software behavior is project-reported/current-source-recovered. Research papers are bounded to their studied populations/domains.

## 11. Analytic note

The quarter's central pattern is a separation of **production correctness**, **decoding correctness**, **accessible representation**, and **scientific validity**. The same artifact can succeed on one plane and fail or remain unknown on another.

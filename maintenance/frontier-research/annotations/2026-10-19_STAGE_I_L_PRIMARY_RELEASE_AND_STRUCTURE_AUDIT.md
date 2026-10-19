# 2026 Stage I–L primary-release and structure audit — 2026-10-19

## Identity, data provenance and scope
- Repository: `lostlight530/sci-render-kit`, inspected main SHA: `951f74d8aaf94739e2305cbc23c7417a65fbc9f9`; prior annual merge reference: `81a459eac96961d929cac879c6e8af09bb963cf4`.
- Review performed 2026-10-19 through connected GitHub API by ChatGPT project-session researcher. This is a **same-producer documentary audit**, not scientific peer review, browser/render test, accessibility certification or independent reproduction.
- Input: native 2026 Stage I/J/K/L source-object registers, official `GET /repos/{owner}/{repo}/releases/tags/{tag}` records, repository Git recursive tree, and comparison to previous 2025 annual merge.
- Scope: the fourteen **selected** release identities (including the two October candidates), not the entire 2026 visualization ecosystem or unselected release candidates.

## Exact publisher release/tag verification
For every source-object row below, a real GitHub Release tag object was retrieved; its `published_at` UTC date matched the registry date. The publisher records were neither drafts nor prereleases at read time. These are **version and chronology checks**. GitHub existence and the release's own notes cannot establish actual rendering behavior on an arbitrary browser, platform or end-user environment.

| Stage | Upstream publisher release | Stage register event date | Check |
|---|---|---|---|
| I | [vega/vega-lite@v6.4.2](https://github.com/vega/vega-lite/releases/tag/v6.4.2) | 2026-01-14 | MATCH / published / not draft / not prerelease |
| I | [plotly/plotly.js@v3.4.0](https://github.com/plotly/plotly.js/releases/tag/v3.4.0) | 2026-02-20 | MATCH / published / not draft / not prerelease |
| I | [plotly/plotly.py@v6.6.0](https://github.com/plotly/plotly.py/releases/tag/v6.6.0) | 2026-03-02 | MATCH / published / not draft / not prerelease |
| J | [matplotlib/matplotlib@v3.10.9](https://github.com/matplotlib/matplotlib/releases/tag/v3.10.9) | 2026-04-23 | MATCH / published / not draft / not prerelease |
| J | [vega/altair@v6.1.0](https://github.com/vega/altair/releases/tag/v6.1.0) | 2026-04-21 | MATCH / published / not draft / not prerelease |
| J | [plotly/plotly.js@v3.5.1](https://github.com/plotly/plotly.js/releases/tag/v3.5.1) | 2026-05-01 | MATCH / published / not draft / not prerelease |
| J | [matplotlib/matplotlib@v3.11.0](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0) | 2026-06-12 | MATCH / published / not draft / not prerelease |
| J | [vega/altair@v6.2.2](https://github.com/vega/altair/releases/tag/v6.2.2) | 2026-06-23 | MATCH / published / not draft / not prerelease |
| K | [matplotlib/matplotlib@v3.11.1](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.1) | 2026-07-18 | MATCH / published / not draft / not prerelease |
| K | [plotly/plotly.py@v7.0.0](https://github.com/plotly/plotly.py/releases/tag/v7.0.0) | 2026-08-25 | MATCH / published / not draft / not prerelease |
| K | [vega/altair@v6.3.0](https://github.com/vega/altair/releases/tag/v6.3.0) | 2026-09-15 | MATCH / published / not draft / not prerelease |
| K | [matplotlib/matplotlib@v3.11.2](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.2) | 2026-09-11 | MATCH / published / not draft / not prerelease |
| L-OPEN | [plotly/plotly.js@v4.1.2](https://github.com/plotly/plotly.js/releases/tag/v4.1.2) | 2026-10-05 | MATCH / published / not draft / not prerelease |
| L-OPEN | [vega/vega-lite@v6.5.0](https://github.com/vega/vega-lite/releases/tag/v6.5.0) | 2026-10-08 | MATCH / published / not draft / not prerelease |

**Result:** `14/14 RELEASE_OBJECT_AND_PUBLISHED_DATE_MATCH / 0 MISMATCHES_IN_CHECKED_SET`.

A Matplotlib patch, Plotly.js renderer, Plotly.py Python wrapper, Vega-Lite compiler and Altair wrapper are not interchangeable software identities. Their release notes are origin-specific evidence, not independent inter-renderer validation. A stable code/text spec can render differently because of renderer revision, font or export environment; no pixel/semantic/accessibility equivalence trial was executed by this audit.

## Native source and time hierarchy
- Git recursive tree reported `truncated=false`; `39/39` essential contract and longitudinal routes were present: I/J/K each seven contractual files and three month reconstructions; L six source/brief/review/October files; two year-to-date longitudinal syntheses and the forward Stage-I absence reconciliation.
- Per-Stage file totals on current main: I=`13`, J=`15`, K=`14`, L=`8`, total `50` native 2026 Stage paths. Files are not independently reproduced experiments.
- Stage L remains `MONTH_OPEN / STAGE_NOT_COMPLETE`: no `STAGE_SYNTHESIS.md`, no 2026-11 or 2026-12 monthly reconstruction. The annual 2026 YTD remains `YEAR_OPEN`.
- Comparison with `81a459eac96961d929cac879c6e8af09bb963cf4` showed zero changed native Stage A–H paths. Earlier A2 `STAGE_I_NOT_EVIDENCED` observations remain dated and historically recoverable; new Stage I–L status is placed later in the canonical index, with forward reconciliation.

## Selection and consistency risks
- The selected objects cross upstream family boundaries (Vega, Plotly and Matplotlib). Each is authoritative about its own tagged release, **not an independent reproduction of another project's behavior**.
- The existing `annotations/PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md` and `annotations/expansion/` record additional wrapper/renderer release candidates. Their non-admission is preserved: `candidate != Stage finding`. Inclusion later requires a bounded methodological amendment, new evidence charting and review without rewriting original monthly snapshots.
- Official release metadata cannot answer whether `sci-render-kit` rendered, matched a publisher profile, communicated uncertainty correctly, or met WCAG requirements. All remain `NOT_TESTED` by this check.

## Findings / governance disposition
| Finding | Evidence checked | Disposition |
|---|---|---|
| S1 release identity | Fourteen exact publisher release tag endpoints | `MATCH_14_OF_14` |
| S2 routing completeness | Main tree paths; Stage I–L and YTD/forward correction | `39_OF_39_PRESENT` |
| S3 temporal closure | Open Stage L / YTD | `Q4_OPEN / YEAR_OPEN` |
| S4 historical integrity | Compare since 2025 annual merge | `ORIGINAL_A–H_STAGE_PATHS_UNCHANGED` |
| S5 scientific claim and renderer behavior | No local fixture, browser/export trial, accessibility testing or external independent reproduction | `UNKNOWN / NOT_TESTED` |
| S6 independent peer review | Same producer documentary verification | `INDEPENDENCE_NOT_ESTABLISHED` |

`DOCUMENTARY_RELEASE_AND_STRUCTURE_CHECK_COMPLETE / NO_CORRECTION_TRIGGER_IN_CHECKED_SCOPE / NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE`.

This audit neither revises the historical Stage research nor creates a competing stage or claims `FRONTIER_STAGE_COMPLETE` for Q4. Later substantive corrections must be dated and attached forward, never silently overwrite the original month/Stage objects.

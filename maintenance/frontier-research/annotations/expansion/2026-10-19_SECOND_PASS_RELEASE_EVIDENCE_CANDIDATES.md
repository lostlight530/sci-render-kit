# Second-pass 2026 release evidence — additive candidate register

## 0. Identity and temporal scope
- Repository: `lostlight530/sci-render-kit`; domain: **Figure output and release-status addendum**.
- Research instrument/time: ChatGPT assistant using connected GitHub public release-list and exact tagged-release reads, 2026-10-19.
- Kind: `ADDITIVE_CANDIDATE_REGISTER / SOURCE_BOUNDED / NOT_STAGE_ADMITTED`.
- Origin: a parallel native Stage I–L proposal was withheld after a newer authoritative main already acquired its own Stage I–L documents, month reconstructions, 2026 YTD, index and reconciliation. The superseded parallel PR is **not** merged.
- Related native reconciliation: [parallel selection register](../PARALLEL_SOURCE_SELECTION_RECONCILIATION_2026-10-19.md).
- Read authority: original Stage files and newest main remain controlling. Earlier absence inside a selected source family is **not** an assertion of global nonexistence.

## 1. Why these candidates and not a second Story/Stage
The present source selection is a **differential comparison** against native Stage I–K and the existing parallel candidate register. It targets additional versioned events that were not selected as main Stage findings, or that expose a distinct technical question not already owned by the main Stage's Part. This is not a replacement longitudinal index, a new research Stage, a reanalysis of all 2026 academic literature, or an attempted merge of the conflicting parallel branch.

## 2. Exact candidate evidence
| ID | Release date | Versioned upstream object | Release-described fact (not runtime evidence) |
|---|---|---|---|
| SP-1 | 2026-01-14 | [Plotly.py v6.5.2](https://github.com/plotly/plotly.py/releases/tag/v6.5.2) | Fixes array-valued pie legend/showlegend attributes |
| SP-2 | 2026-05-13 | [Matplotlib v3.11.0rc2 (PRERELEASE)](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2) | Second 3.11 release candidate fixes downstream package problems and missed deprecations |
| SP-3 | 2026-09-15 | [Plotly.py v7.1.0](https://github.com/plotly/plotly.py/releases/tag/v7.1.0) | Fixes unsigned-integer pandas columns being interpreted as categories in Plotly Express and improves mpl_to_plotly tick/background conversion |

### SP-1 — Plotly.py v6.5.2
**Source/event:** official upstream GitHub release [Plotly.py v6.5.2](https://github.com/plotly/plotly.py/releases/tag/v6.5.2), published 2026-01-14, consulted 2026-10-19.

**Direct publisher observation:** Fixes array-valued pie legend/showlegend attributes.

**Repository-lens interpretation:** Legends can encode the relation between figure marks and scientific categories; patch behavior can alter output semantics without changing data.

**Native Stage and selection distinction:** Main January selects Vega-Lite 6.4.2; older parallel candidate C1 already covers Plotly.py v6.5.1; this is a different patch object.

**Counter-reading:** A release note is publisher-origin evidence for a stated change and date; it cannot establish prevalence, downstream correctness, independent adoption, local execution or a target-repository defect. The candidate adds a source possibility, not an automatically admissible Stage result.

### SP-2 — Matplotlib v3.11.0rc2 (PRERELEASE)
**Source/event:** official upstream GitHub release [Matplotlib v3.11.0rc2 (PRERELEASE)](https://github.com/matplotlib/matplotlib/releases/tag/v3.11.0rc2), published 2026-05-13, consulted 2026-10-19.

**Direct publisher observation:** Second 3.11 release candidate fixes downstream package problems and missed deprecations.

**Repository-lens interpretation:** A release candidate has different maturity and time authority from the June 3.11.0 stable release; do not project GA capabilities into May.

**Native Stage and selection distinction:** Main May selected Plotly.js 3.5.1; June owns Matplotlib v3.11.0 GA; this candidate must remain explicitly RC.

**Counter-reading:** A release note is publisher-origin evidence for a stated change and date; it cannot establish prevalence, downstream correctness, independent adoption, local execution or a target-repository defect. The candidate adds a source possibility, not an automatically admissible Stage result.

### SP-3 — Plotly.py v7.1.0
**Source/event:** official upstream GitHub release [Plotly.py v7.1.0](https://github.com/plotly/plotly.py/releases/tag/v7.1.0), published 2026-09-15, consulted 2026-10-19.

**Direct publisher observation:** Fixes unsigned-integer pandas columns being interpreted as categories in Plotly Express and improves mpl_to_plotly tick/background conversion.

**Repository-lens interpretation:** Numerical type interpretation and cross-renderer conversion can change communicated chart structure without changing the dataset.

**Native Stage and selection distinction:** Main September selected Altair and Matplotlib changes; no Plotly 7.1 reproducibility experiment is recorded.

**Counter-reading:** A release note is publisher-origin evidence for a stated change and date; it cannot establish prevalence, downstream correctness, independent adoption, local execution or a target-repository defect. The candidate adds a source possibility, not an automatically admissible Stage result.


## 3. Executed method and review limitations
1. The upstream GitHub Releases index was inspected by date and selected exact `/repos/{owner}/{repo}/releases/tags/{tag}` release records were read on 2026-10-19. Inclusion: dated 2026 release pertinent to the repository lens, a distinct versioned source object from the main's selected objects.
2. Event date, release metadata access date and this annotation's authorship date are different clocks. Version tag and originating publisher are included so a future reviewer can reproduce the lookup.
3. The entries represent publisher release reports, not independent studies. Several releases from the same project count as **one source family**, not multiple independent corroborations.
4. This is `SOURCE_BOUNDED` targeted discovery, not systematic search. Other projects, source types, independent reproductions, unreleased branches and negative evidence have not been exhaustively reviewed.
5. Review independence: `SAME_PRODUCER_REVIEW`; no local runtime, renderer, CI, sandbox, artifact conversion, SDK test, security exploit, performance benchmark or scientific adjudication performed here.

## 4. Governance disposition
- `CANDIDATE / WATCH / NOT_STAGE_ADMITTED` for every entry. A qualified native Stage owner must assess amendment eligibility, source/object registration, revised chart, cross-Part implications and producer/independent review before admitting one to a Stage conclusion.
- Earlier Month `NO_SELECTED_OBJECT_IN_DECLARED_SOURCE_SET` results stay intact; any later expanded selection must be recorded as a **new timepoint or method amendment**, not silent history rewriting.
- No change to `LONGITUDINAL_INDEX.md`, original monthly/quarterly narratives, YTD, operational code, contracts, or evidence authority is justified by this register alone.
- `source != object != independent reproduction`; `selection != truth`; `external release != current-repository defect`; `review != execution`; `handoff != acceptance`.

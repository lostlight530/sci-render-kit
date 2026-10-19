# 2026-10-19 additional-source reconciliation — Plotly.py wrapper version evidence

## Research scope and native chronology
- Repository `lostlight530/sci-render-kit`; research written **2026-10-19** about 2026-Q1 and 2026-Q3.
- Type `ADDITIVE_SOURCE_SELECTION_EXPANSION / SOURCE_BOUNDED` from official upstream GitHub release tags. This is **not** a new Stage, retrospective change of research dates, independent render test or blanket assertion of new field-wide completeness.
- Current main includes native [Stage I](../../stage-i-2026-q1/STAGE_SYNTHESIS.md) and [Stage K](../../stage-k-2026-q3/STAGE_SYNTHESIS.md), plus an [open Stage L](../../stage-l-2026-q4/STAGE_BRIEF.md) with Plotly.js 4.1.2 and Vega-Lite 6.5.0 October evidence.
- The original 2026 Stages and object IDs preserve their own selected release records and interpretation. An additional origin-tagged object **must not be renumbered silently** into the existing register.

## New bounded release objects
| Extension object | Original month / Stage | Publisher release date and link | Bounded issuer observation | Figure-evidence implication |
|---|---|---|---|---|
| EX-I1 | [January 2026 / Stage I](../../stage-i-2026-q1/MONTH_2026_01_RECONSTRUCTION.md) | [plotly.py v6.5.1](https://github.com/plotly/plotly.py/releases/tag/v6.5.1), 2026-01-07 | Fixes Plotly Express template-specific color sequences; upgrades bundled plotly.js 3.3.0→3.3.1 | A Python wrapper patch can change a figure's template interpretation, even when the data and plot recipe are unchanged |
| EX-K1 | [September 2026 / Stage K](../../stage-k-2026-q3/MONTH_2026_09_RECONSTRUCTION.md) | [plotly.py v7.1.0](https://github.com/plotly/plotly.py/releases/tag/v7.1.0), 2026-09-15 | Adds marginal heatmap support and arbitrary conversion tick values; fixes unsigned-integer type interpretation and cross-library background transfer | Typed input, cross-library transformation and rendered orientation/background are separately versioned evidence surfaces |

## Comparison with native selected objects and conflicts
- Native [I release selections](../../stage-i-2026-q1/SOURCE_OBJECT_REGISTER.md) include Vega-Lite 6.4.2 (January), plotly.js 3.4.0 (February) and plotly.py 6.6.0 (March). EX-I1 is a **distinct wrapper version** from those objects and cannot be inferred solely from a JavaScript renderer release.
- Native [K source set](../../stage-k-2026-q3/SOURCE_OBJECT_REGISTER.md) includes Matplotlib 3.11.1, plotly.py 7.0.0, Altair 6.3.0 and Matplotlib 3.11.2. EX-K1 is a later **plotly.py 7.1.0** object, not a second independent confirmation of v7.0.0.
- Stage [L](../../stage-l-2026-q4/SOURCE_OBJECT_REGISTER.md) separately records versioned October Plotly.js/Vega-Lite source objects as **Q4 OPEN**. EX-I1/EX-K1 do not overwrite or close that Q4 story.

## Mechanism and source critique
```text
dataset + numeric dtype
 -> Python wrapper release + template
 -> generated plotly spec + JS bundle release
 -> browser/export backend and fonts
 -> visible / interactive figure
 -> separately checked scientific claim
```

Plotly release notes establish publisher-described changes, not a controlled cross-version pixel/interaction/accessibility comparison. Sources from plotly.py and plotly.js are related ecosystem families, not necessarily independent validation of one behavior. Matplotlib-to-Plotly conversions can change color, tick, geometry and orientation semantics, but a particular rendered plot difference would require reproducible inputs and tool-version pinning.

Competing account: the selected versions could represent ordinary defect fixes rather than uniform progress in scientific visual reliability. Release notes have selection bias; no systematic all-renderer archive search, independent browser replay or accessibility user study was performed.

## Decision and next native gate
- Disposition `SOURCE_BOUNDED_ADDITIONAL_EVIDENCE`; research on 2026-10-19, not contemporaneous January/September investigation.
- Existing I/K quarter syntheses remain correct within their original release selection. New objects are **HOLD_FOR_EXPLICIT_STAGE_SELECTION_AMENDMENT**, not quietly promoted into the original count or verification status.
- No tested local defect, scientific validity, WCAG certification, publisher acceptance or transfer of authority follows. `NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE`.


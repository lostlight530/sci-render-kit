# Source and Research-Object Register — Stage A / 2024-Q1

## 0. Register identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Specification:** `2026-09-19-first-batch`
- **Register date:** `2026-09-21`
- **Coverage:** `SEARCH_BOUNDED`

## 1. Identity rules

```text
figure != claim
rendered artifact != scientific validation
visual encoding != interpreted meaning
alternate representation != semantic equivalence
interactive surface != static surface
library version != backend execution
same chart spec != same communication outcome
```

## 2. Research-object register

| ID | Canonical object | Type | Q1 event/date | Identity basis | Notes |
|---|---|---|---|---|---|
| O1 | Visualization According to Statisticians | research paper | publication record 2024-01-01 | journal/university publication record | inferential visualization/uncertainty |
| O2 | Uncertainty in humanities network visualization | research paper | 2024-01-12 | Frontiers article | uncertainty communication |
| O3 | Chart4Blind | accessibility conversion system + paper | code 2024-01-07; paper 2024-03-11/18 | GitHub commit + arXiv/KIT record | raster -> SVG/CSV/alt text |
| O4 | ggplot2 | plotting-library release | 3.5.0, 2024-02-23 | official release/changelog | guide-system overhaul |
| O5 | Matplotlib | plotting-library release line | 3.8.3 2024-02-15; 3.7.5 2024-02-16 | GitHub releases | backend bugfixes |
| O6 | Plotly.py | interactive plotting release line | 5.19 2024-02-15; 5.20 2024-03-13 | GitHub releases | guide/layout/serialization/visual changes |
| O7 | Vega-Lite | visualization grammar release | 5.17.0, 2024-03-12 | changelog/release | tooltip + mark/stack fixes |
| O8 | Vega-Altair | declarative plotting release | 5.3.0, 2024-03-30 | GitHub release | renderer/execution paths |

## 3. Evidence-source register

| ID | Source | Family | Date | Authority | Limitations |
|---|---|---|---|---|---|
| S1 | https://pure.au.dk/portal/en/publications/visualization-according-to-statisticians-an-interview-study-on-th/ | paper authors/publisher | 2024-01 | paper record/findings | interview study scope |
| S2 | https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2023.1305137/full | paper authors/publisher | 2024-01-12 | peer-reviewed paper | domain-specific uncertainty context |
| S3 | https://github.com/moured/chart4blind_code/commit/8dc19c08c77096229b7839925a279fff8f1475a0 | Chart4Blind project | 2024-01-07 | code-availability anchor | not final-paper equivalence |
| S4 | https://github.com/moured/chart4blind_code | Chart4Blind project | mutable | implementation/readme | same family |
| S5 | https://arxiv.org/abs/2403.06693 | Chart4Blind authors | 2024-03-11 | paper method/results | same family as code |
| S6 | https://publikationen.bibliothek.kit.edu/1000183463 | KIT publication record | 2024-03-18 | proceedings/publication metadata | not independent replication |
| S7 | https://tidyverse.org/blog/2024/02/ggplot2-3-5-0/ | ggplot2/Tidyverse | 2024-02-23 | release semantics | producer source |
| S8 | https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-legends/ | ggplot2/Tidyverse | 2024-02-26 | legend semantics | same family |
| S9 | https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-axes/ | ggplot2/Tidyverse | 2024-02-28 | axis semantics | same family |
| S10 | https://github.com/matplotlib/matplotlib/releases/tag/v3.8.3 | Matplotlib | 2024-02-15 | release/fix record | project source |
| S11 | https://github.com/matplotlib/matplotlib/releases/tag/v3.7.5 | Matplotlib | 2024-02-16 | release/fix record | project source |
| S12 | https://github.com/plotly/plotly.py/releases/tag/v5.19.0 | Plotly | 2024-02-15 | release record | project source |
| S13 | https://github.com/plotly/plotly.py/releases/tag/v5.20.0 | Plotly | 2024-03-13 | release record | project source |
| S14 | https://github.com/vega/vega-lite/blob/main/CHANGELOG.md | Vega-Lite | records 5.17 on 2024-03-12 | release/changelog | mutable main changelog |
| S15 | https://github.com/vega/altair/releases/tag/v5.3.0 | Vega-Altair | 2024-03-30 | release record | project source |

## 4. Source-to-object mapping

| Object | Sources | Relation | Directness | Independence |
|---|---|---|---|---|
| O1 | S1 | reports study | direct | one paper family |
| O2 | S2 | reports study | direct | one paper family |
| O3 | S3-S6 | implements/reports/publishes | direct | same research family |
| O4 | S7-S9 | releases/explains guides | direct | same project family |
| O5 | S10,S11 | releases/fixes | direct | same project family |
| O6 | S12,S13 | releases/updates | direct | same project family |
| O7 | S14 | records release/fixes | direct | one project family |
| O8 | S15 | releases/updates renderer paths | direct | project family related to Vega ecosystem |

## 5. Source-family / independence map

| Family | Members | Common origin | Limitation |
|---|---|---|---|
| SF1 | S1 | visualization/inference study | single study |
| SF2 | S2 | uncertainty-network study | single study |
| SF3 | S3-S6 | Chart4Blind team/project | code + paper not independent replication |
| SF4 | S7-S9 | ggplot2/Tidyverse | release + explanatory posts same producer |
| SF5 | S10-S11 | Matplotlib | same project |
| SF6 | S12-S13 | Plotly | same project |
| SF7 | S14,S15 | Vega/Vega-Altair ecosystem | related project family; not independent for shared Vega-Lite semantics |

## 6. Revision / correction registry

| Object | Revision | Date | Research effect |
|---|---|---|---|
| O5 | backend bugfix releases | Feb 15-16 | execution state can change without scientific-method change |
| O6 | 5.19 -> 5.20 | Feb -> Mar | guide/visual/runtime semantics evolve |
| O7 | 5.17 fixes tooltip/mark behavior | 2024-03-12 | interactive communication state changes |
| O8 | 5.3 updates Vega-Lite + renderer paths | 2024-03-30 | spec/render pathway provenance becomes material |

## 7. Identity/conflict notes

- Chart4Blind January code is not treated as proof that every March paper feature/result existed in January.
- Vega-Lite current changelog is a mutable current page used to recover a dated 5.17 entry.
- Altair and Vega-Lite share ecosystem lineage; their evidence is not counted as fully independent when discussing shared renderer/spec behavior.

## 8. Limitations

No local rendering, assistive-technology test, statistical recalculation, cross-backend comparison, or semantic-equivalence experiment was executed.

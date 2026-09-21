# Source and Research-Object Register — Stage B / 2024-Q2

## Identity

- Repository: lostlight530/sci-render-kit
- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Registered: 2026-09-22

## Object register

| ID | Object | Type | Q2 state/date | Identity note |
|---|---|---|---|---|
| O1 | ggplot2 3.5.1 | plotting-library release | 2024-04-23 | regression/correction release |
| O2 | Vega-Lite 5.18/5.19 | visualization-grammar release line | 2024-04-09, 2024-05-07, 2024-06-14 | density, null and invalid-data semantics |
| O3 | Matplotlib 3.9 | plotting-library release | 2024-05-15 | backend/layout/guide/mathtext state |
| O4 | Umwelt | multimodal authoring research system | CHI 2024, May 11-16 | coequal visual/sonic/text modalities |
| O5 | MAIDR | multimodal accessible visualization system | CHI 2024 / May | sonification/text/braille/review |
| O6 | Customization is Key | accessible visualization customization model | CHI 2024 | presence/verbosity/order/duration |

## Source register

| ID | Source | Family | Date | Authority | Limit |
|---|---|---|---|---|---|
| S1 | https://ggplot2.tidyverse.org/news/index.html | ggplot2/Tidyverse | 2024-04-23 | release/fix semantics | producer source |
| S2 | https://github.com/vega/vega-lite/blob/main/CHANGELOG.md | Vega-Lite | Q2 entries | release/fix semantics | mutable current changelog |
| S3 | https://matplotlib.org/3.10.5/users/prev_whats_new/whats_new_3.9.0.html | Matplotlib | 2024-05-15 | release behavior | producer documentation |
| S4 | https://vis.csail.mit.edu/pubs/umwelt/ | Umwelt authors | CHI 2024 | method + reported study | one research family |
| S5 | https://www.microsoft.com/en-us/research/publication/maidr-making-statistical-visualizations-accessible-with-multimodal-data-representation/ | MAIDR authors/Microsoft Research | May 2024 | method + reported study | producer publication surface |
| S6 | https://vis.mit.edu/pubs/customization/ | Customization authors | CHI 2024 | method + reported study | one research family |

## Family map

- SF1 ggplot2: S1
- SF2 Vega-Lite: S2
- SF3 Matplotlib: S3
- SF4 Umwelt: S4
- SF5 MAIDR: S5
- SF6 Customization: S6

Distinct research/software families support cross-object convergence but do not establish identical mechanisms or independent reproduction of one another

## Identity rules

    library version != same communication state
    modality != authority
    accessible representation != semantic equivalence
    user configuration != source truth
    invalid-data display policy != data validity
    current changelog != frozen historical snapshot

## Limitations

No local renderer execution, screen-reader/tactile test, cross-modal semantic-equivalence study, WCAG certification, or exhaustive visualization survey

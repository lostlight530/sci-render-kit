# Evidence Chart — Stage B / 2024-Q2

## Identity

- Repository: lostlight530/sci-render-kit
- Coverage: SEARCH_BOUNDED
- Charted: 2026-09-22

## Variables

- source/data state
- library/release identity
- renderer/backend state
- visual decoding semantics
- invalid-data policy
- modality
- user configuration/query state
- accessibility evidence
- source family
- reproduction state

## Findings

| ID | Observation | Object | Evidence | Independence | Boundary |
|---|---|---|---|---|---|
| F1 | ggplot2 3.5.1 repairs guide/scale/resolution regressions | O1 | S1 | single family | fix != scientific validation |
| F2 | Vega-Lite changes density/null/invalid-data representation across Q2 versions | O2 | S2 | single family | representation policy != data truth |
| F3 | Matplotlib 3.9 makes backend identity and multiple layout/legend semantics more explicit | O3 | S3 | single family | backend success != scientific validity |
| F4 | Umwelt derives visual/sonic/text modes from shared abstract data state | O4 | S4 | independent research family | coequal modality != semantic equivalence |
| F5 | MAIDR combines text/sonification/braille/review and emphasizes user autonomy | O5 | S5 | independent research family | reported user benefit != universal accessibility |
| F6 | Customization exposes presence/verbosity/order/duration as user-controlled communication state | O6 | S6 | independent research family | preference/configuration != scientific authority |

## Cross-object analysis

Stage B turns communication provenance into a state graph

    data/model
    + representation policy
    + library/renderer version
    + modality
    + user configuration
    + invalid-data policy
    + query/interaction state
    + accessibility evidence

No one plane automatically inherits authority from another

## Counterevidence

Multimodality increases coordination and equivalence burden

Customization can add complexity

Explicit invalid-data representation can communicate missingness without validating why values are missing

## Amendment

NONE

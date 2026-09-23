# D1 — Multimodal Access and Interaction

## Question
What does Q4 research establish about accessible visualization interaction for blind and low-vision users?

## Objects and sources
- O1: MAIDR Meets AI, ASSETS '24, published 2024-10-27.
- O2: ChartA11y, ASSETS '24, October 2024.
- O3: screen-reader + sonification exploration prototype, AccessViz 2024.
- S1: https://doi.org/10.1145/3663548.3675660
- S2: https://doi.org/10.1145/3663548.3675611
- S3: https://doi.org/10.1109/AccessViz64636.2024.00009

## Observations
Q4 contains multiple approaches to non-visual chart access: multimodal LLM-supported interpretation with BLV users, touch/sonification interaction for blind smartphone users, and screen-reader/sonification exploration.

These are different systems, participant groups and interaction contracts. Their coexistence strengthens the case that "accessible representation" is not one modality.

## Analysis
```text
same underlying data
-> text / screen reader
-> sonification
-> touch / haptic interaction
-> LLM-mediated interpretation
```

Each path has its own transformation, user interaction, failure modes and validation population.

## Counterevidence / limits
- User studies are bounded by participant counts, devices, tasks and systems.
- LLM-mediated interpretation can introduce model-specific error.
- Different studies are not independent reproductions of one common implementation.

## Conclusion
`SUPPORTED_MULTIMODALITY_BOUNDARY`

```text
accessible in one interaction path
!= accessible in every path
!= semantic equivalence
!= scientific validity
```

# Frontier Research Stage Brief — Stage F / 2025-Q2

## Identity
- Repository: `lostlight530/sci-render-kit`
- Specification: `2026-09-19-first-batch`
- Stage: `F / 2025-Q2`
- Window: `2025-04-01 through 2025-06-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-25`
- Status: `COMPLETE`

## Rationale
Stage E established wrapper, serialization, compiler/runtime and package-host identity as scientific-communication provenance. Stage F studies what happens during migration and stabilization: wrapper compatibility may lag a grammar major, image-generation/notebook backends can be revised, and delivery integrity/accessibility metadata can change in later releases.

## Research questions
1. How should an unresolved wrapper migration be represented without inventing released capability?
2. What do Plotly.py 6.1 and Matplotlib 3.10.3 show about backend/runtime stabilization after a major transition?
3. What do Plotly.py 6.2 and Vega-Lite 6.2 add to delivery-integrity and accessibility-sensitive communication provenance?

## Hard boundaries
```text
migration issue != released capability
backend support != backend availability
render fix != scientific validity
SRI support != source trust
ARIA behavior != accessibility certification
release note != local replay
```

# Frontier Research Stage Brief — Stage G / 2025-Q3

## Identity
- Repository: `lostlight530/sci-render-kit`
- Specification: `2026-09-19-first-batch`
- Stage: `G / 2025-Q3`
- Window: `2025-07-01 through 2025-09-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-26`
- Status: `COMPLETE`

## Rationale
Stage F followed migration, backend stabilization, delivery integrity, and accessibility-sensitive output after a major renderer transition. Stage G follows the next quarter as scientific-communication identity becomes more explicitly tied to the **runtime platform**, the **export/browser engine**, and the **interactive representation semantics** users actually encounter.

The Stage does not ask which library is "best." It asks what additional state must be recorded before a rendered/interactive scientific figure can be interpreted reproducibly.

## Research questions
1. What does Matplotlib 3.10.5 show when supported runtime/platform targets change at the wheel/distribution layer?
2. What does Plotly.py 6.3 add when browser acquisition and the underlying Plotly.js revision become explicit export/runtime dependencies?
3. What do Vega-Lite 6.3/6.4 point releases show about interaction, tooltip, and visual semantics being version-sensitive?

## Hard boundaries
```text
wheel available != runtime tested
backend version != render correctness
browser acquisition != browser reproducibility
renderer update != scientific validity
tooltip/cursor behavior != accessibility certification
release note != local replay
same-project point release != independent corroboration
```

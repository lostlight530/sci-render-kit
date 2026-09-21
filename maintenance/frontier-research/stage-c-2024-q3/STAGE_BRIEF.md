# Frontier Research Stage Brief — Stage C / 2024-Q3

## Identity

- Repository: `lostlight530/sci-render-kit`
- Specification: `2026-09-19-first-batch`
- Stage: `C / 2024-Q3`
- Window: `2024-07-01 through 2024-09-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-22`
- Status: `COMPLETE`

## Rationale

Stage A separated scientific evidence, visual encoding, render execution and communication/accessibility

Stage B showed that communication is a family of versioned modalities and user-configurable states

Stage C asks how interactive/reactive state and user-population-specific validation change what a scientific communication artifact means and what evidence can be attached to it

## Hard boundaries

- `render success != scientific validity`
- `interaction state != source-data state`
- `representation-specific validation != global validation`
- `user-study result != universal accessibility`
- `wrapper/library version != inherited semantic equivalence`
- `low-vision usability evidence != blind-user evidence`
- `publication date != conference presentation date`

## Research questions

1. When does reactive/interactive parameter state become communication provenance
2. How do renderer/wrapper revisions change communication behavior even with unchanged data/specification
3. What does population-specific accessibility evidence validate, and what must remain scoped to user/device/task context

## Source plan

| Family | Q3 object | Use |
|---|---|---|
| Vega-Lite | 5.20.0/5.20.1/5.21.0 | reactive params, conditional opacity, responsive ticks |
| Altair | 5.4.0 | wrapper embeds Vega-Lite 5.20.1; version-coupled communication state |
| Matplotlib | 3.9.1/3.9.2 | interaction/backend fixes and versioned interactive behavior |
| GraphLite / IEEE TVCG | online publication 2024-09-20 | low-vision, smartphone, personalization/interaction validation |

## Parts

- C1 Reactive and Interactive Communication State
- C2 Renderer/Wrapper Version Binding
- C3 Population-Conditioned Accessibility Evidence

## Appraisal

Producer release sources establish project behavior/change state

User-study paper establishes bounded findings for its participants/tasks

No source establishes universal accessibility or scientific validity

## Amendments

`NONE`

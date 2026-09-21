# Frontier Research Stage Synthesis — Stage B / 2024-Q2

## Identity

- Repository: lostlight530/sci-render-kit
- Stage: B / 2024-Q2
- Window: 2024-04-01 through 2024-06-30
- Record type: RETROSPECTIVE
- Coverage: SEARCH_BOUNDED
- Synthesis date: 2026-09-22
- Status: COMPLETE

## Research questions revisited

| RQ | Outcome | Main evidence | Limit |
|---|---|---|---|
| versioned visual semantics | ANSWERED | ggplot2, Vega-Lite, Matplotlib | no local cross-version rerender |
| multimodal accessibility | ANSWERED/PARTIAL | Umwelt, MAIDR | bounded user studies; no independent rerun |
| user control + invalid-data policy | ANSWERED | Customization, Vega-Lite 5.19 | no universal optimal policy |

## Method actually executed

Stage B carried forward Stage A's four-plane model and questions about renderer provenance, alternate representations, and representation-specific validation

The object set was fixed before synthesis: three software families for versioned rendering semantics and three independent accessibility-research families for multimodality/user control

Official release documentation and primary research surfaces were used; same-origin evidence was grouped; month reconstructions and Parts preceded synthesis; no material amendment occurred

## April — visual semantics are visibly versioned

Vega-Lite 5.18 and ggplot2 3.5.1 expose version-specific defaults, guide ordering, scale behavior, density resolution, and regression repair

This is not merely maintenance noise

It demonstrates that the same source data and broadly similar specification can produce a different communication surface under a different library revision

    data unchanged
    != communication state unchanged

## May — the visual artifact stops being the privileged center

May combines Matplotlib 3.9 with three CHI accessibility objects

Matplotlib makes backend identity and several guide/layout/rendering details more explicit

Umwelt goes further conceptually by treating visualization, sonification, and text as coequal representations derived from a shared abstract model

MAIDR combines sonification/text with braille/review and emphasizes user autonomy

Customization makes presence, verbosity, ordering, and duration explicit user-configurable dimensions

The communication object is therefore no longer well represented as:

    figure.png + alt text

A stronger model is:

    shared scientific/data state
      -> representation family
      -> modality
      -> renderer/version
      -> user configuration
      -> interaction/query state

## June — invalid data become representation policy

Vega-Lite 5.19 adds more explicit options/examples for representing nulls and NaNs through marks and scales

This closes the quarter with a crucial distinction

    invalid/missing datum
    != absent observation
    != automatically valid observation

How invalid data are shown is a communication decision with epistemic consequences, not a repair of the data itself

## Cross-Part synthesis

Stage A separated four planes:

1 scientific/source evidence
2 visual encoding
3 render/execution
4 communication/accessibility

Stage B decomposes Plane 4 and strengthens Plane 3

A Stage B communication state can require:

    source/scientific context
    + encoding/specification
    + renderer/library/backend revision
    + representation modality
    + user configuration
    + query/interaction state
    + invalid-data policy
    + accessibility evidence

This is not a universal file schema

It is a non-collapse model for reasoning about what a viewer or assistive modality actually receives

## Previous-Stage delta

Relative to Stage A:

- STRENGTHENED: renderer/library version as evidence provenance
- NEW: coequal modality model rather than visual-first conversion
- NEW: user-controlled presence/verbosity/order/duration as communication state
- NEW: explicit invalid-data representation policy
- STRENGTHENED: accessibility as representation-specific evidence, not metadata checkbox
- PERSISTENT: render success != scientific validity
- PERSISTENT: accessible support != universal certification
- UNRESOLVED: semantic equivalence across modalities and user configurations

## Counterevidence and negative space

No Stage B evidence establishes:

- one universally best modality
- universal accessibility
- WCAG certification for these systems
- semantic equivalence between visual/sonic/text/braille states
- a universal optimal invalid-data policy
- scientific validity from successful rendering
- local reproduction in this repository

## Current repository assessment

The external research converges with current repository boundaries and suggests future research questions

It does not establish current implementation, contract, or documentation drift

    NO_CURRENT_REPOSITORY_DRIFT
    NO_RUNTIME_CHANGE
    NO_CONTRACT_CHANGE

## Limitations

Search-bounded, no local renderer execution, no assistive-technology rerun, bounded user-study evidence, mutable software changelogs, same-producer review

## Stage conclusion

FRONTIER_STAGE_COMPLETE

Q1's durable lesson was that a figure is not just pixels

Q2 goes further: a scientific communication object is not one canonical representation at all

It is a family of versioned, modality-specific, user-configurable communication states whose relations must be preserved without assuming semantic or scientific equivalence

The durable principle is:

    communication transfer
    != authority transfer

    representation change
    can change what evidence is perceptible
    without changing the underlying scientific object

## Carry-forward questions

- How should validation attach to a representation or modality rather than a figure globally
- Can one claim bind to multiple communication states without implying equal support
- How should interactive/query state be versioned for reproduction
- When does user customization become material provenance
- What evidence is required to compare accessibility across modalities

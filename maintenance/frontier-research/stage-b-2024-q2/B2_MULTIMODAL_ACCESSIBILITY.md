# Frontier Research Part B2 — Multimodal Accessibility as a Communication Graph

## Identity

- Stage: B / 2024-Q2
- Coverage: SEARCH_BOUNDED
- Status: COMPLETE

## Research question

How did Q2 accessibility research challenge the assumption that one visual artifact should remain the privileged source representation

## Objects and sources

- O4 Umwelt
- O5 MAIDR
- S4 https://vis.csail.mit.edu/pubs/umwelt/
- S5 https://www.microsoft.com/en-us/research/publication/maidr-making-statistical-visualizations-accessible-with-multimodal-data-representation/

## Umwelt observation

Umwelt, published at CHI 2024, treats visualization, sonification, and textual description as coequal representations derived from a shared abstract data model rather than treating nonvisual modes as secondary conversions from a privileged final chart

It maintains a shared query predicate across modalities so navigation/filtering state can be reified across representations

The paper reports a study with five blind/low-vision expert users

## MAIDR observation

MAIDR studies multimodal access to bar plots, heat maps, box plots, and scatter plots

Beyond sonification and text, it includes braille and review modalities and emphasizes user autonomy in combining modalities

The reported user study involved 11 blind participants

## Analysis

Stage A described alternate representations as edges derived from a figure

Stage B adds a stronger model:

    shared data/semantic state
        -> visual representation
        -> sonification
        -> text
        -> braille/review

where no single modality automatically owns scientific authority

The important property is not number of formats but preservation of relationships across modalities and user interaction state

## Counterevidence and limits

These studies do not establish universal accessibility, WCAG certification, or semantic equivalence across modalities

User-study findings are bounded to the reported participants/tasks

No system was rerun in this repository

## Conclusion

SUPPORTED_OBSERVATION

Accessible scientific communication can be modeled as a multimodal communication graph rather than a visual artifact plus after-the-fact accessibility metadata

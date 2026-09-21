# Frontier Research Part A1 — Uncertainty, Guides, and Figure-Evidence Semantics

## 0. Identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Part:** `A1`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> How did Q1 work make visual encodings, guides, and uncertainty expression more explicit, and what does this imply about figure evidence?

## 2. Research objects

- O1 — “Visualization According to Statisticians,” January 2024 publication.
- O2 — “Uncertainty in humanities network visualization,” published 2024-01-12.
- O4 — ggplot2 3.5.0 guide-system overhaul, 2024-02-23 plus axis/legend explanatory posts.

## 3. Source set

- S1: Aarhus publication record for “Visualization According to Statisticians”: https://pure.au.dk/portal/en/publications/visualization-according-to-statisticians-an-interview-study-on-th/
- S2: Frontiers, “Uncertainty in humanities network visualization”: https://www.frontiersin.org/journals/communication/articles/10.3389/fcomm.2023.1305137/full
- S3: ggplot2 3.5.0 release: https://tidyverse.org/blog/2024/02/ggplot2-3-5-0/
- S4: ggplot2 3.5.0 legends: https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-legends/
- S5: ggplot2 3.5.0 axes: https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-axes/

## 4. January: uncertainty and inferential interpretation are not decoration

The statisticians interview study reports that visualization is used throughout inferential work and that many statisticians reject simple dichotomous thinking. The authors connect visual displays of effect sizes and uncertainty to how inferential results are understood.

The key repository interpretation is that a figure is not merely a container for a conclusion. It is part of the evidence interface through which a viewer reconstructs scale, effect, variation, and uncertainty.

The humanities-network uncertainty paper similarly treats uncertainty as something that must be communicated in the visualization process rather than silently omitted.

This supports:

```text
uncertainty represented
!= uncertainty calibrated
uncertainty omitted
!= certainty
visual salience
!= epistemic strength
```

## 5. February: ggplot2 guide semantics expose the decoding layer

ggplot2 3.5.0 rewrote the guide system. The release documentation explicitly describes axes and legends as mechanisms that allow visual information to be translated back into data qualities/values.

This is unusually useful for figure-evidence reasoning because it exposes a normally invisible layer:

```text
data
 -> scales/encodings
 -> marks
 -> guides (axes/legends)
 -> viewer reconstruction of data meaning
```

If guides are incorrect, ambiguous, missing, or inconsistent with marks, the renderer may still produce a valid image while communication is defective.

### Legend awareness

The 3.5.0 legend changes made keys more aware of which discrete values/layers they represent. This is relevant to claim binding: a visible legend key is not generic decoration; it participates in binding visual attributes to semantic categories.

### Axes

The axis changes broaden control over repeated/faceted axes and labels. This shows that the same underlying data may be presented with different guide availability. Suppressing labels or changing axis placement can change what a reader can recover from the figure even when the plotted marks are unchanged.

## 6. Figure evidence as a structured relation

A useful conceptual model is:

```text
claim C
  bound-to figure F
figure F
  contains encodings E
  interpreted-through guides G
  may express uncertainty U
```

The existence of C-F binding does not prove that F entails C. A correct guide does not prove the underlying statistical model. An uncertainty band does not prove calibration.

## 7. Counterevidence / limitations

The selected studies do not imply that every figure requires explicit uncertainty. Different analytic tasks require different visual forms.

The ggplot2 release is software evidence, not a user-comprehension study. Its relevance is structural: it makes the decoding role of guides explicit.

## 8. Current repository relation

`DIRECTLY_RELEVANT / PARALLEL_CONVERGENCE`

The evidence supports keeping claim binding, uncertainty metadata, and visual-guide semantics distinct from scientific validation.

## 9. Part conclusion

`SUPPORTED_OBSERVATION`

Q1 evidence supports treating figure communication as a structured decoding process. **A rendered figure is evidence-bearing only through interpretable encodings and guides, and neither successful decoding nor uncertainty display automatically establishes scientific validity.**

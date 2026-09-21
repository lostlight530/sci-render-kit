# Frontier Research Part A2 — Accessibility and Alternate Representation

## 0. Identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Part:** `A2`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> What did Q1 accessibility work show about the relation among raster charts, SVG, CSV, alt text, tactile/screen-reader use, and communication equivalence?

## 2. Research object

O3 — Chart4Blind development/publication sequence.

Sources:

- S6: first public code push, 2024-01-07: https://github.com/moured/chart4blind_code/commit/8dc19c08c77096229b7839925a279fff8f1475a0
- S7: Chart4Blind repository: https://github.com/moured/chart4blind_code
- S8: arXiv paper, 2024-03-11: https://arxiv.org/abs/2403.06693
- S9: KIT publication record / IUI 2024 proceedings date: https://publikationen.bibliothek.kit.edu/1000183463

## 3. January code state

The project repository has a first code push on 2024-01-07. Its documented feature set includes automatic/manual data-point input, SVG/CSV exports, OCR for labels/axes/descriptions, and interface feedback.

This makes January a genuine implementation event even though the formal paper appears in March.

## 4. March publication: accessibility requires alternate representations

The Chart4Blind paper describes conversion from bitmap line-chart images into multiple accessible outputs, including SVG, CSV, and alt text, with intended support for screen readers, tactile display/print workflows, and other assistive modalities. The paper reports interviews/user studies and usability results.

The important scientific-communication implication is not that these formats are equivalent. It is almost the opposite: accessibility requires **multiple representations because one representation does not serve every interaction mode**.

```text
raster pixels
!= structured SVG
!= CSV data table
!= alt-text narrative
!= tactile representation
```

They may represent related content, but each exposes different affordances, omissions, and transformation risks.

## 5. Communication equivalence is a research question, not an automatic relation

Suppose an original chart is converted to CSV + SVG + alt text. The following questions remain:

- Were all plotted data values recovered?
- Were axes, scales, units, and ordering recovered?
- Were trends/annotations/statistical uncertainty preserved?
- Does alt text communicate the same salient evidence as the visual chart?
- Does the SVG structure support usable navigation?
- Does a tactile transformation preserve relevant spatial relationships?
- Were transformations manually corrected?

A checksum or successful export answers none of those semantic questions by itself.

## 6. Accessibility intent vs certification

Chart4Blind's authors report accessible-format goals and user studies. This Stage does not independently certify the outputs against all WCAG or assistive-technology requirements.

Therefore:

```text
accessible-format support
!= universal accessibility
paper reports compliance/compatibility
!= independent certification by this Stage
```

## 7. Claim binding across representations

A scientific claim may be bound to a figure, but alternate representations may communicate different subsets of the figure evidence.

A safe communication-transfer record should preserve:

- source figure identity;
- transformation method/tool;
- output representation;
- data extracted/reconstructed;
- textual description provenance;
- validation/user-check status;
- known losses or manual corrections.

## 8. Counterevidence / limitations

Chart4Blind focuses on line charts and a specific conversion workflow. It does not establish universal conversion for every scientific visualization type.

The same project/research family supplies code and paper evidence; they are not independent replications.

## 9. Repository relation

`DIRECTLY_RELEVANT`

This object strongly supports the repository boundary `communication transfer != inherited authority`. A derivative representation can be useful and accessible without inheriting every semantic property of the source.

## 10. Part conclusion

`SUPPORTED_OBSERVATION`

Accessibility is not a post-render boolean. It is a **representation and interaction problem**. Safe scientific communication needs provenance across alternate representations and explicit limits on semantic inheritance.

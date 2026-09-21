# Frontier Research Stage Brief — Stage A / 2024-Q1

## 0. Identity

- **Repository:** `lostlight530/sci-render-kit`
- **Specification:** `2026-09-19-first-batch`
- **Stage ID:** `A`
- **Canonical period:** `2024-Q1`
- **Research window:** `2024-01-01 through 2024-03-31`
- **Record type:** `RETROSPECTIVE`
- **Design:** `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- **Coverage intended:** `SEARCH_BOUNDED`
- **Reconstruction date:** `2026-09-21`
- **Research cutoff:** `2026-09-21`
- **Status:** `COMPLETE`

## 1. Rationale

Stage A reconstructs Q1 2024 through the scientific-communication layer: how uncertainty is visually communicated, how axes/legends/guides map graphical encodings back to data, how chart accessibility can require alternate structured representations, and how renderer/library revisions alter communication behavior.

The Stage does not ask which visualization library is “best.” It asks what evidence is needed to distinguish successful rendering from scientifically faithful communication.

## 2. Repository lens and non-claims

Lens: **scientific communication, figure evidence, claim binding, uncertainty expression, reproducibility context, accessibility intent, publisher-target workflows, and communication transfer.**

Hard boundaries:

- `render success != scientific validity`
- `claim binding != entailment`
- `uncertainty metadata != statistical validation`
- `publisher profile/alignment != acceptance`
- `accessibility support != WCAG certification`
- `checksum != independent reproduction`
- `communication transfer != inherited authority`

Stage-specific non-claims:

- visible axis/legend != correctly interpreted evidence;
- uncertainty depiction != calibrated statistical uncertainty;
- accessible export feature != complete accessibility;
- interactive tooltip != accessible communication for all users;
- static and interactive representations are not assumed semantically equivalent;
- library release != scientific validation.

## 3. Objectives and research questions

### Objective

Reconstruct Q1 2024 changes that illuminate the distinction between figure production, visual-semantic encoding, uncertainty communication, accessibility representation, and scientific authority.

### Research questions

1. **RQ1:** How did Q1 work make visual encodings, guides, and uncertainty expression more explicit, and what does this imply about figure evidence?
2. **RQ2:** What did Q1 accessibility work show about the relation among raster charts, SVG, CSV, alt text, tactile/screen-reader use, and communication equivalence?
3. **RQ3:** How did renderer/library revisions demonstrate that communication behavior depends on versions, backends, and target-specific semantics?

## 4. Conceptual scope

Included: axes, legends, visual scales, uncertainty representation, accessible chart conversion, SVG/CSV/alt text, interactivity/tooltips, browser/Jupyter/static renderers, backend fixes, and chart-library version coupling.

Excluded: generic UI design not tied to data/figure communication; aesthetic preference without evidence semantics; publisher acceptance claims; scientific validity inferred only from rendering.

## 5. Temporal scope

Q1 event dates are distinguished from later access dates. Current project documentation may be used to explain a Q1 release only when version/date evidence anchors the historical object.

## 6. Eligibility and selection

Include primary papers, official release notes, and direct repository histories with Q1 events. Multiple release-note pages from one project remain one source family.

## 7. Source authority plan

| Source class | Establishes | Does not establish |
|---|---|---|
| peer-reviewed/accepted research paper | studied design, method, reported user/interpretation evidence | universal accessibility or scientific validity |
| official release/changelog | feature/fix/version state | scientific correctness/adoption |
| repository commit | code/publication timing | user outcome |
| project docs | documented semantics | independent reproduction |

## 8. Discovery/search design

Targeted searches/navigation covered January uncertainty/interpretation work, Chart4Blind repository history, ggplot2 3.5.0, Matplotlib/Plotly Q1 releases, Vega-Lite 5.17, Altair 5.3, and Chart4Blind publication.

## 9. Research-object model

A paper/system release is one research object even when multiple pages describe it. Library patch releases may be grouped into one release-line object when the research question concerns evolving rendering semantics, with individual revisions preserved.

## 10. Planned Parts

- A1 — uncertainty, guides, and figure-evidence semantics;
- A2 — accessibility and alternate representation;
- A3 — renderer/version state and communication transfer.

## 11. Planned chart variables

representation, visual encoding, guide semantics, uncertainty form, accessibility modality, renderer/backend/version, interaction state, validation/user-study evidence, source family, and communication-transfer boundary.

## 12. Appraisal

Descriptive source-authority appraisal. No universal visualization-quality score.

## 13. Analysis

Chronological + cross-object mechanism analysis. Preserve differences among rendering, interpretation, accessibility, and scientific validation.

## 14. Longitudinal comparability

Future Stages should retain library/system version, representation target, interaction mode, accessibility modality, uncertainty semantics, and validation type.

## 15. Review plan

Same-producer full review in this run. Independent visualization/accessibility/statistics review preferred but not established.

## 16. Contribution/provenance

Human Maintainer: final governance. ChatGPT agent: research execution/drafting/review. Web/GitHub are instruments.

## 17. Amendments

Initial library-focused source set expanded to January/quarter research papers after the Maintainer required deeper month-complete research. Recorded in synthesis.

## 18. Completion criteria

Three thematic Parts, three month dossiers, register/chart, synthesis, contributor record, review, handoff, and longitudinal index.

## 19. Correction triggers

Historical version/date error, material paper correction, later source showing an interpretation overreached, or reproduced behavior contradicting release/document evidence.

## 20. Expected outputs

Complete first-batch Stage family plus month-level historical reconstruction.

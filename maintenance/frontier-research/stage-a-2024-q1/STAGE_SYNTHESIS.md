# Frontier Research Stage Synthesis — Stage A / 2024-Q1

## 0. Stage identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Window:** `2024-01-01 through 2024-03-31`
- **Record type:** `RETROSPECTIVE`
- **Design:** `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- **Coverage:** `SEARCH_BOUNDED`
- **Synthesis date:** `2026-09-21`
- **Status:** `COMPLETE`

## 1. Research questions revisited

| RQ | Outcome | Main evidence | Limitation |
|---|---|---|---|
| RQ1 uncertainty/guides/figure evidence | ANSWERED | O1,O2,O4 | no universal viewer model |
| RQ2 accessibility/alternate representations | ANSWERED/PARTIAL | O3 | one system/chart class; no independent certification |
| RQ3 renderer/version/communication transfer | ANSWERED | O5-O8 | no local cross-version/render execution |

## 2. Research inputs

Three thematic Parts, three monthly reconstructions, eight research objects, fifteen primary/high-authority sources, evidence chart, and repository-specific boundaries.

## 3. Method actually executed

The research first recovered the first-batch frontier specification and used its suggested `stage-a-2024-q1/` as the earliest Stage.

Initial discovery focused on Q1 plotting-library releases. After the Maintainer clarified that research depth and month completeness should dominate over template brevity, the source plan expanded to include January research on inferential/uncertainty visualization and the Chart4Blind code-to-paper sequence.

Executed method:

1. define scientific-communication research questions;
2. discover Q1 papers/releases/commits;
3. use primary papers and official release histories;
4. separate project source families;
5. create month dossiers for Jan/Feb/Mar;
6. distinguish visual semantics, alternate representation, renderer/version state, and scientific validation;
7. chart counterevidence and negative space;
8. synthesize the quarter;
9. same-producer review.

This remains `SEARCH_BOUNDED`, not a systematic visualization-literature review.

## 4. Evidence coverage

The Stage intentionally combines two evidence planes.

### Human/research plane

- inferential visualization and uncertainty interpretation;
- uncertainty representation in network visualization;
- accessible chart conversion and user study.

### Software/rendering plane

- ggplot2 guide architecture;
- Matplotlib backend fixes;
- Plotly guide/layout/serialization/visual changes;
- Vega-Lite interaction/mark fixes;
- Altair renderer/execution pathways.

The research plane asks whether information is interpretable/accessible. The software plane asks what visual/interactive artifact is produced. Neither plane alone establishes scientific validity.

## 5. Source-family independence

Chart4Blind code/paper/publication record are one family. ggplot2 release/explanatory posts are one family. Matplotlib, Plotly, and Vega ecosystem sources are project evidence.

The January papers come from separate research teams and provide independent conceptual convergence around uncertainty/interpretation.

No independent cross-library reproduction was performed.

## 6. January — pixels are not the full communication object

January's evidence shows that scientific visualization participates in reasoning, not only decoration.

“Visualization According to Statisticians” reports visualization across inferential work and resistance to simplistic dichotomous reasoning. “Uncertainty in humanities network visualization” focuses directly on representing uncertainty in network evidence. Chart4Blind's January code state provides a concrete implementation object for converting chart information out of raster pixels.

These objects converge on a shared claim: a figure is not exhausted by its bitmap.

A scientific communication artifact may include:

- source data;
- statistical/model outputs;
- visual encoding;
- axes/legends;
- annotations;
- uncertainty encoding;
- interactive state;
- accessible alternate representation;
- provenance and caption/claim context.

A PNG checksum only identifies one final representation.

## 7. February — the decoding and execution layers become explicit

### ggplot2 3.5.0: guides are semantic infrastructure

The ggplot2 3.5.0 release explicitly explains axes and legends as guides that map visual information back to data qualities/values.

That language reveals a key communication chain:

```text
data
 -> scale
 -> graphical property
 -> guide
 -> viewer-decoded data meaning
```

The guide system is not the data and not the scientific model. It is the interface that makes encoded visual variables recoverable.

A figure can therefore fail scientifically relevant communication even if its marks render correctly: wrong/missing labels, ambiguous legend keys, misleading scales, or inappropriate guide placement can break interpretation.

The 3.5.0 legend “awareness” changes are particularly illustrative because they make keys more sensitive to which layer/value they should represent. This is a software-level example of semantic binding between visual representation and category.

### Matplotlib: backend success is execution evidence

The 3.8.3/3.7.5 fixes show that backend/runtime state can determine whether a rendering pipeline hangs or crashes.

This yields a narrow but important boundary:

```text
render executable
!= scientific result validated
render failure
!= scientific hypothesis false
```

Execution state belongs to provenance, not truth state.

### Plotly 5.19: one release spans multiple communication layers

Tick angles, Sankey alignment, bar-corner geometry, typed-array transport, and deterministic scatter-mode fixes do not all have the same semantic weight. Some are guide/layout behavior, some visual style, some data transport, some determinism.

Therefore a changelog cannot be mapped wholesale to “better scientific visualization.” Each change needs its own relation to evidence communication.

## 8. March — communication transfer becomes visibly multi-path

### Chart4Blind: alternate representations

The March paper shows a deliberate pipeline from raster chart to SVG, CSV, and alt text, with intended support for screen readers and tactile workflows.

The critical insight is not “SVG is accessible.” It is that the same underlying chart can need several derived representations to support different modalities.

This creates a transfer graph:

```text
original visual artifact
  -> extracted data/structure
  -> SVG
  -> CSV
  -> alt text
  -> tactile/screen-reader modality
```

Each edge can lose or transform information.

### Vega-Lite 5.17 / Plotly 5.20: interaction and visual semantics are versioned

Tooltip fixes, stack behavior, gradients, and legend indentation show that information available to a viewer can change across library versions even when source data remain fixed.

Interactive figures are especially important: a static screenshot may not contain tooltip values or states. Conversely, an interactive chart may be unusable in a target publication or assistive context.

### Altair 5.3: one high-level spec can travel through different renderers

Browser/Jupyter/VegaFusion pathways make renderer choice part of the execution context.

This implies that figure provenance can require:

```text
specification identity
+ library version
+ renderer/backend
+ transformation/data engine
+ output representation
+ interaction mode
```

A final checksum cannot reconstruct this chain by itself.

## 9. What persisted across Q1

### 9.1 Rendering and validation remain separate

No selected source supports upgrading a successful render into a scientific validation state.

### 9.2 Visual semantics depend on decoding structures

Axes, legends, captions, labels, and interaction are not incidental. They mediate the relation between marks and meaning.

### 9.3 Accessibility requires alternate communication paths

A visually readable chart can be inaccessible to a screen reader. A CSV can expose values but lose spatial/form relationships. Alt text can communicate salient trends but omit detailed data. No representation automatically dominates all others.

### 9.4 Uncertainty remains a scientific rather than purely graphical property

Visualization can communicate uncertainty but cannot create valid uncertainty estimates from invalid statistics.

### 9.5 Renderer/library state is part of provenance

Backend bugs and versioned interactive behavior show why execution context matters.

## 10. What weakened, failed, or disappeared

### “If it rendered, it is fine”

Weakened by backend fixes, tooltip/mark fixes, and guide semantics.

### “The image is the figure”

Weakened by Chart4Blind and interactive renderer paths.

### “Alt text is accessibility”

Weakened by Chart4Blind's multi-representation design.

### “Uncertainty shown means uncertainty validated”

Not supported by visualization research.

### “Claim bound to figure means entailed by figure”

Not supported. Binding records a communication relation, not logical/scientific entailment.

### “Same spec/source means same communication”

Not established across multiple renderer/interaction paths.

## 11. Evidence maturity

| Object | Public research/artifact | Versioned implementation | User/interpretation evidence | Independent reproduction in Stage |
|---|---|---|---|---|
| O1 statisticians study | paper | n/a | interview study | not replicated |
| O2 uncertainty networks | paper | n/a | domain research | not replicated |
| O3 Chart4Blind | code + paper | yes | reported user study | not independently rerun |
| O4 ggplot2 3.5 | release | yes | no Stage user test | no |
| O5 Matplotlib | release | yes | software bug evidence | no |
| O6 Plotly | releases | yes | no Stage user test | no |
| O7 Vega-Lite | release/changelog | yes | no Stage user test | no |
| O8 Altair | release | yes | no Stage user test | no |

These states are descriptive, not a universal maturity score.

## 12. Counterevidence and competing interpretations

### Interpretation A — visualization libraries are progressively becoming scientifically safer

The quarter shows useful engineering improvements, but this conclusion would overreach. Library releases improve features/fixes; they do not validate the statistical model, data, or claim.

### Interpretation B — richer accessibility outputs preserve the original figure

Chart4Blind supports practical conversion, but alternate representations have different affordances. Preservation must be evaluated per representation and task.

### Interpretation C — declarative specs solve reproducibility

Declarative specs improve inspectability. But renderer/backend/version changes show the spec is only one part of execution provenance.

### Interpretation D — explicit uncertainty resolves interpretive uncertainty

Explicit uncertainty can improve communication, yet the underlying uncertainty model can still be wrong or incomplete.

## 13. Cross-Part synthesis: four non-collapsible evidence planes

Stage A supports a four-plane model:

### Plane 1 — Scientific/source evidence

Data, statistical model, uncertainty calculation, scientific claim.

### Plane 2 — Visual encoding evidence

Marks, scales, axes, legends, annotations, uncertainty encodings.

### Plane 3 — Render/execution evidence

Library version, renderer/backend, interaction engine, successful generation.

### Plane 4 — Communication/accessibility evidence

Viewer interpretation, alternate representation, assistive modality, user study/accessibility checks.

A figure pipeline is robust when these planes are linked. It becomes epistemically unsafe when they are collapsed.

Examples:

```text
Plane 3 PASS
does not imply Plane 1 PASS

Plane 4 accessible-format support
does not imply universal accessibility

Plane 2 uncertainty band
does not imply Plane 1 statistical calibration
```

## 14. Repository-level interpretation

### Independent convergence

Q1 evidence converges strongly with existing repository boundaries:

- render success != scientific validity;
- uncertainty metadata != statistical validation;
- accessibility support != certification;
- communication transfer != inherited authority.

### Potential watch items

Future current-state audits may ask:

- whether renderer/backend/version provenance is always recoverable;
- whether interactive vs static output identity is explicit;
- whether accessible alternate representations retain source-figure provenance;
- whether claim bindings can reference what part of a figure supports a claim without implying entailment;
- whether validation status is representation-specific.

No current defect is inferred.

### Non-gaps

The existence of ggplot2 guide changes, Chart4Blind, or multiple Altair renderers does not by itself expose a repository defect.

## 15. Hard boundaries preserved

- `render success != scientific validity`
- `claim binding != entailment`
- `uncertainty metadata != statistical validation`
- `publisher profile/alignment != acceptance`
- `accessibility support != WCAG certification`
- `checksum != independent reproduction`
- `communication transfer != inherited authority`

## 16. Temporal reconciliation

January Chart4Blind code availability is kept distinct from March paper publication. Later paper claims are not back-projected as fully implemented in January.

Current Vega-Lite changelog is used to recover a dated 5.17 release entry but is marked as a mutable current source.

No later library behavior is silently attributed to Q1 versions.

## 17. Previous-Stage delta

No prior comparable Stage. `NOT_COMPARABLE`.

## 18. Current repository assessment

- **Implementation drift confirmed:** `NO`
- **Active-contract drift confirmed:** `NO`
- **Documentation drift confirmed:** `NO`
- **Separate repair required:** `NO`

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

## 19. Contribution/provenance

See `CONTRIBUTOR_STATEMENT.md`. Same-producer review. No local rendering or accessibility validation.

## 20. Limitations

Search-bounded coverage, primary/project-source concentration for software objects, no render execution, no cross-renderer equivalence testing, no screen-reader/tactile re-evaluation, no WCAG certification, and no statistical recalculation of uncertainty.

The quarter should therefore be read as a **research-engineering communication baseline**, not a universal state of visualization science.

## 21. Review readiness

Independent review should focus on:

- whether the four-plane synthesis is appropriately bounded;
- accessibility claims around Chart4Blind;
- interpretation of ggplot guide semantics;
- inference from library/version changes to provenance requirements;
- uncertainty-representation versus statistical-validation language.

## 22. Stage conclusion

`FRONTIER_STAGE_COMPLETE`

Q1 2024 shows that scientific visualization cannot be reduced to “code produced a figure.”

January research emphasizes that figures participate in inferential reasoning and that uncertainty can be hidden or communicated in the visual layer. Chart4Blind's January code provides an early implementation object for extracting chart structure into alternate representations.

February's ggplot2 guide overhaul exposes axes and legends as semantic decoding infrastructure. Matplotlib and Plotly releases show that execution backends, guide layout, serialization, and deterministic behavior can change the artifact a viewer receives.

March makes the communication graph explicitly multi-modal and multi-renderer: Chart4Blind converts visual charts into SVG/CSV/alt text; Vega-Lite changes interactive behavior; Plotly changes visual/guide semantics; Altair adds renderer pathways.

The durable conclusion is:

```text
scientific communication validity
cannot be inferred from render success alone

figure evidence
= scientific/source context
+ visual encoding context
+ render/execution provenance
+ communication/accessibility evidence
with each plane retaining its own authority boundary
```

No current repository defect is established by this Stage.

## 23. Correction/update triggers

A dated correction is required if a Q1 release date/source is wrong, a paper is materially corrected, later evidence shows an accessibility/renderer interpretation overreached, or local reproduction materially contradicts the current Stage.

## 24. Carry-forward questions

- How do later visualization systems record representation-specific validation?
- Can interactive and static figure identities be reconciled without asserting semantic equivalence?
- How should figure-claim binding represent partial support, annotation regions, or uncertainty?
- What accessibility evidence is portable across SVG/HTML/PDF/CSV/text/tactile outputs?
- When do renderer changes become scientifically material enough to require regeneration/re-review?

## 25. Safe handoff

Safe: four-plane model, render-vs-validity distinction, representation-specific accessibility, versioned renderer provenance, guide/decoding semantics.

Unsafe: universal library rankings, WCAG certification, scientific correctness claims, publisher acceptance inference.

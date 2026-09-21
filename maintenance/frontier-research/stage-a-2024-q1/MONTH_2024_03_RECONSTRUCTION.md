# March 2024 Reconstruction — Stage A

## Month frame

March closes Stage A with three converging themes: alternate accessible chart representations, interactive communication semantics, and increasingly varied renderer/execution paths.

Coverage: `SEARCH_BOUNDED`.

## M1 — Chart4Blind paper, arXiv 2024-03-11; IUI publication record 2024-03-18

Sources:

- https://arxiv.org/abs/2403.06693
- https://publikationen.bibliothek.kit.edu/1000183463

The work converts bitmap line charts into accessible forms including SVG, CSV, and alt text and reports a user study around the conversion workflow.

### Research significance

The paper demonstrates why accessibility cannot be reduced to “add alt text.” Different users/modalities need different representations.

But:

```text
multiple accessible outputs
!= semantic equivalence across outputs
!= independent certification by this Stage
```

## M2 — Vega-Lite 5.17, released 2024-03-12

Source: https://github.com/vega/vega-lite/blob/main/CHANGELOG.md

The 5.17 release includes an interactive-tooltip-related fix and other mark/stack corrections.

### Research significance

Interactive retrieval is part of figure communication. If tooltip behavior changes, the visible static marks may remain similar while the interactive evidence surface changes.

## M3 — Plotly.py 5.20, released 2024-03-13

Source: https://github.com/plotly/plotly.py/releases/tag/v5.20.0

The release brings Plotly.js changes including scatter fill gradients and legend indentation.

### Research significance

Fill gradients can encode additional visual information or emphasis, while legend indentation changes guide structure. The scientific meaning depends on how those encodings are used, not on feature existence.

## M4 — Altair 5.3, released 2024-03-30

Source: https://github.com/vega/altair/releases/tag/v5.3.0

Altair 5.3 updates Vega-Lite to 5.17 and expands rendering/execution options including browser and JupyterChart renderers plus VegaFusion integration for large interactive datasets.

### Research significance

A high-level declarative chart can flow through multiple render paths with different execution context. A repository that records only the final PNG/SVG loses information about the renderer path that produced it.

## M5 — Cross-object accessibility/interactivity boundary

Chart4Blind and Vega/Altair/Plotly expose two different kinds of communication enhancement:

- alternate accessible representations;
- richer interactive/rendering affordances.

Neither class automatically inherits the scientific authority of the source data/model.

## March synthesis

March makes “communication transfer” a concrete research object:

```text
source data/claim
 -> chart specification
 -> renderer/runtime
 -> visual/interative artifact
 -> alternate representation
 -> user interpretation
```

Each arrow can alter available information. Therefore every transfer should have a bounded evidence claim.

## March negative space

Not established:

- that alternate formats communicate identical salience;
- that interactive tooltips are accessible to all users;
- that browser/Jupyter/static renderers produce semantically equivalent artifacts;
- WCAG certification;
- statistical validity from visual uncertainty alone;
- scientific validity from rendering success.

## Quarter-close implication

Q1 supports a strong communication-governance principle: **figure production, figure interpretation, accessibility, and scientific validation are distinct evidence planes that must remain linked but non-collapsed.**

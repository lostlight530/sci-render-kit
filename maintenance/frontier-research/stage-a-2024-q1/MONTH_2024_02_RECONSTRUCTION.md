# February 2024 Reconstruction — Stage A

## Month frame

February shifts from research-method interpretation to concrete plotting-library semantics: guide systems, backend behavior, and version-specific rendering options.

Coverage: `SEARCH_BOUNDED`.

## F1 — ggplot2 3.5.0, released 2024-02-23

Sources:

- https://tidyverse.org/blog/2024/02/ggplot2-3-5-0/
- https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-legends/
- https://tidyverse.org/blog/2024/02/ggplot2-3-5-0-axes/

The release substantially rewrites ggplot2's guide system. The release explanation explicitly states that axes and legends are visual representations of scales that allow visual information to be translated back into data qualities/values.

### Research significance

This makes guides part of the evidence-decoding path rather than ornamental metadata.

A plot can render successfully while:

- category-to-color mapping is unclear;
- axis labels are suppressed;
- facet axes are not where the reader expects;
- legend keys communicate the wrong layer/value relation.

The release's “awareness” changes to legends are therefore communication-semantic changes, not merely styling.

## F2 — Matplotlib 3.8.3 / 3.7.5, 2024-02-15 / 2024-02-16

Sources:

- https://github.com/matplotlib/matplotlib/releases/tag/v3.8.3
- https://github.com/matplotlib/matplotlib/releases/tag/v3.7.5

The releases fix hangs on the MacOS backend and a PGF-backend exit crash.

### Research significance

Backend state is part of executable provenance. A pipeline may be scientifically correct in intent but fail to produce output under a backend/runtime defect.

Conversely, a fixed backend establishes successful execution, not scientific correctness.

## F3 — Plotly.py 5.19, released 2024-02-15

Source: https://github.com/plotly/plotly.py/releases/tag/v5.19.0

Notable changes include automatic tick angles, Sankey-node alignment, rounded bar corners, typed-array/base64 representation, and deterministic scatter-mode fixes.

### Research significance

The release spans guide layout, geometry, serialization, and deterministic rendering behavior. These are separate evidence dimensions.

```text
same plotting API
+ different library version
!= guaranteed identical visual communication
```

## February synthesis

February makes the scientific communication stack explicit:

```text
data/statistics
 -> scale
 -> visual encoding
 -> guide
 -> renderer/backend
 -> output representation
 -> viewer interpretation
```

A PASS at one step does not inherit to the next.

## February negative space

Not established:

- user interpretation quality for every ggplot2 guide configuration;
- semantic equivalence across Plotly versions;
- whether fixed Matplotlib backends change any specific scientific conclusion;
- accessibility certification for any selected plotting library.

## Carry-forward

March should examine interactive information recovery, alternate accessible representations, and multiple renderer paths.

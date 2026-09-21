# Frontier Research Part A3 — Renderer/Version State and Communication Transfer

## 0. Identity

- **Repository:** `lostlight530/sci-render-kit`
- **Stage:** `A / 2024-Q1`
- **Part:** `A3`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> How did Q1 renderer/library revisions demonstrate that communication behavior depends on versions, backends, and target-specific semantics?

## 2. Objects

- O5 Matplotlib 3.8.3 / 3.7.5 bugfix releases.
- O6 Plotly.py 5.19/5.20.
- O7 Vega-Lite 5.17.
- O8 Vega-Altair 5.3.

## 3. Sources

- Matplotlib 3.8.3: https://github.com/matplotlib/matplotlib/releases/tag/v3.8.3
- Matplotlib 3.7.5: https://github.com/matplotlib/matplotlib/releases/tag/v3.7.5
- Plotly.py 5.19: https://github.com/plotly/plotly.py/releases/tag/v5.19.0
- Plotly.py 5.20: https://github.com/plotly/plotly.py/releases/tag/v5.20.0
- Vega-Lite 5.17 changelog: https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
- Altair 5.3: https://github.com/vega/altair/releases/tag/v5.3.0

## 4. February: backend/runtime correctness remains part of render provenance

Matplotlib 3.8.3 and 3.7.5 fixed MacOS backend hangs and a PGF-backend exit crash. These are operational defects rather than scientific-method changes, but they matter to reproducibility context:

```text
same plotting code
+ different backend/runtime state
-> different execution outcome
```

A failed or hanging backend can prevent figure production altogether. Conversely, successful production after a fix does not prove the figure's scientific content.

## 5. February: Plotly.py 5.19 changes both visual options and data transport

Plotly.py 5.19 updated Plotly.js and added or surfaced changes including rounded bar corners, automatic tick angles, Sankey node alignment, and typed-array transport using base64 data/shape fields. It also fixed deterministic scatter mode behavior in Plotly Express.

These changes span distinct communication layers:

- visual styling;
- guide/tick layout;
- structural layout;
- data serialization/transport;
- deterministic rendering behavior.

A figure-evidence record that only says “Plotly” is underspecified if version-specific behavior matters.

## 6. March: Plotly 5.20 and Vega-Lite 5.17 change presentation semantics

Plotly.py 5.20 introduced scatter fill gradients and legend indentation via the bundled Plotly.js update.

Vega-Lite 5.17 includes an interactive-tooltip fix and other mark/stack behavior corrections. Even seemingly small interaction/tooltip changes can affect what information a user can recover from an interactive figure.

This gives another boundary:

```text
underlying data unchanged
!= communication surface unchanged
```

## 7. March: Altair 5.3 expands renderer and large-data execution paths

Altair 5.3 updates Vega-Lite to 5.17 and adds integrations/renderers including VegaFusion support for larger interactive data, browser rendering, JupyterChart rendering, and editor workflows.

This means one high-level chart specification may travel through different execution/rendering paths.

Conceptually:

```text
chart specification
 -> renderer/backend A
 -> renderer/backend B
 -> browser/Jupyter/static export
```

The specification may be common, but the execution path, interaction affordances, data transformation, and output form can differ.

## 8. Communication transfer and authority

A rendered artifact can be transferred from interactive to static or from one renderer to another. That transfer should not automatically inherit:

- interaction semantics;
- data availability;
- accessibility behavior;
- exact text/tooltip content;
- rendering fidelity;
- scientific authority.

## 9. Counterevidence / limits

The Stage did not execute cross-version or cross-renderer comparison tests. Release notes establish project-reported changes, not measured semantic divergence for a specific scientific figure.

## 10. Repository relation

`DIRECTLY_RELEVANT`

Q1 library evolution supports explicit renderer/backend/version provenance and the boundary `render success != scientific validity`.

## 11. Part conclusion

`SUPPORTED_OBSERVATION`

Scientific visualization is a versioned execution pipeline. **Figure identity alone is insufficient when rendering behavior, interaction, serialization, or backend state can change the communication surface.**

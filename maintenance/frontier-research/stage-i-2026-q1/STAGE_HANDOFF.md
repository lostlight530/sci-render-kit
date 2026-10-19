# Stage I / 2026-Q1 — bounded L3 handoff

- Source repository: `lostlight530/sci-render-kit`; generated: `2026-10-19`
- Source owners: [Stage Synthesis](STAGE_SYNTHESIS.md) and [Research Review](RESEARCH_REVIEW.md).
- Finding status: `SOURCE_BOUNDED`; reviewer independence `SAME_PRODUCER_REVIEW`.

## Eligible transfers
- `I1`: Tooltip formatting and legend repair (https://github.com/vega/vega-lite/releases/tag/v6.4.2). A stable high-level spec may acquire different tooltip/legend behavior under a patch-level compiler revision. Date 2026-01-14; origin project `vega/vega-lite`.
- `I2`: Legend-title and interaction semantics (https://github.com/plotly/plotly.js/releases/tag/v3.4.0). Interactive figure semantics depend on the JS engine revision and user action, not just a static image. Date 2026-02-20; origin project `plotly/plotly.js`.
- `I3`: Renderer/export patch and side effects (https://github.com/plotly/plotly.py/releases/tag/v6.6.0). A wrapper patch can change diagnostics/export interpretation independent of scientific data or plot recipe. Date 2026-03-02; origin project `plotly/plotly.py`.

## Non-transfers / unresolved
- No runtime conformance, safety, scientific validity, local benchmark result, quantitative speedup, or cross-repository implementation parity is transferable.
- Different official projects' published release notes may support **different objects** but do not independently corroborate each other's released code.
- `handoff != authority transfer`; `cross-repo analogy != identical implementation`; uncertain data remain `UNKNOWN`.

## Research questions
Which of these versioned evidence surfaces could be evaluated by reproducible, narrow local tests? Which should remain metadata-only assertions until independent reproduction? No implementation change is authorized by this handoff.

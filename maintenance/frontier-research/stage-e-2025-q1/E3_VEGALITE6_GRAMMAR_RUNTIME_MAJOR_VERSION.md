# E3 — Vega-Lite 6 Grammar / Runtime Major-Version Identity

## Research question
What changes when a declarative visualization grammar moves to a new major version and runtime/package boundary?

## Evidence
Vega-Lite 6.0.0 was released 2025-03-28. The release record includes:
- ESM-only packaging;
- update to Vega 6;
- change to default continuous size;
- fixes for `timeFormatSpecifier`, tick-step preference and normalized examples.

Source: https://github.com/vega/vega-lite/releases/tag/v6.0.0

## Analysis
For declarative charts, a spec is interpreted by a versioned compiler/runtime. Major-version defaults and packaging can affect both generated Vega and deployability.

~~~text
Vega-Lite spec
+ compiler major
+ Vega runtime major
+ package/module environment
-> rendered communication state
~~~

The spec text alone is therefore insufficient to explain a derivative render.

## Limits
No local Vega-Lite 5→6 compile comparison, browser replay, accessibility-tree inspection or scientific claim audit was executed.

## Outcome
`SUPPORTED_OBSERVATION`
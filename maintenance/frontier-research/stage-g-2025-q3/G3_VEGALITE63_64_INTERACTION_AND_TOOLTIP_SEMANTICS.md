# G3 — Vega-Lite 6.3/6.4: Interaction and Tooltip Semantics Are Versioned

## Question
What do closely spaced Vega-Lite point/minor releases show about interaction and presentation semantics in declarative scientific communication?

## Object
- Research object: Vega-Lite 6.3.x / 6.4.x release sequence
- Events: 6.3.1 on 2025-09-10; 6.4.0 on 2025-09-17; 6.4.1 on 2025-09-23
- Source family: Vega-Lite project changelog
- Authority: project-described release behavior
- Accessed: 2026-09-26

## Primary source
- https://github.com/vega/vega-lite/releases
- Vega-Lite project changelog/release notes

## Observed release state
The September release sequence includes changes/fixes around interactive geographic examples, cursor behavior for interactive charts, stack ordering, tooltip newline support, and width/height behavior.

These are same-project, same-quarter revisions—not independent corroborations.

## Interpretation
Declarative specs can remain syntactically similar while the user-visible interaction/communication behavior changes with the renderer/compiler revision.

```text
declarative spec
+ Vega-Lite revision
+ interaction compiler/runtime
= user-visible interaction state
```

A cursor change or tooltip formatting fix may look small, but it demonstrates that affordance and annotation behavior are release-specific.

For scientific communication, that means a saved recipe/spec is not always sufficient to identify the exact interactive experience without runtime/version context.

## Boundary
Interaction/tooltip behavior is not a scientific-validity or accessibility-conformance verdict. No browser or accessibility-tree replay was performed.

## Finding
`G3_FINDING`: Q3 2025 reinforces that interactive communication semantics are versioned evidence surfaces; the declarative recipe and the realized interaction state should remain distinguishable.

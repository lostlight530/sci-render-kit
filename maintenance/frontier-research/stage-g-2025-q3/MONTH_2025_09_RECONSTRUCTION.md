# September 2025 Reconstruction — Interactive Semantics as Release State

## Monthly event
Vega-Lite released 6.3.1, 6.4.0, and 6.4.1 during September 2025, with changes/fixes affecting interactive examples, cursor behavior, stack ordering, tooltip newline behavior, and size handling.

## Historical interpretation
September shows that a stable-looking declarative spec does not freeze the entire user experience.

```text
recipe/spec
+ compiler/renderer revision
+ interaction behavior
+ tooltip/annotation behavior
= realized communication state
```

This makes interaction semantics a versioned provenance surface rather than a timeless property of the JSON spec.

## Month boundary
The releases are same-project lineage. No browser interaction, tooltip, accessibility-tree, or visual-regression replay was performed.

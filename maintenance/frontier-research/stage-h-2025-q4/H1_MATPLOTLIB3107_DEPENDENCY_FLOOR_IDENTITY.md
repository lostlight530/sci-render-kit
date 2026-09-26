# H1 — Matplotlib 3.10.7: Dependency Floor as Render-Environment Identity

## Source identity
- Object: Matplotlib 3.10.7
- Release-statistics date: 2025-10-08
- Primary sources:
  - https://matplotlib.org/stable/users/release_notes
  - https://matplotlib.org/stable/api/prev_api_changes/api_changes_3.10.7.html

## Frontier observation
Matplotlib 3.10.7 raises the minimum required `pyparsing` version from 2.3.1 to 3.0.0.

For scientific rendering this is not merely installation metadata. Parser/dependency floors are part of the environment that determines whether a recipe can even reach renderer execution.

```text
recipe
-> Python/package environment
-> dependency floor
-> parser behavior
-> backend/runtime
-> artifact
```

## Boundary
- dependency compatibility != renderer correctness
- installable != locally tested
- dependency update != scientific validity
- release statistics date != universal package availability time

## Repository interpretation
No Matplotlib 3.10.7 environment was installed or rendered locally in this Stage.

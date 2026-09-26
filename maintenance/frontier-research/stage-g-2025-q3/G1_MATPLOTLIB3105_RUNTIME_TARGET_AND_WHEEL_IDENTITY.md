# G1 — Matplotlib 3.10.5: Runtime Target and Wheel Identity

## Question
What changes in scientific-figure provenance when a plotting library expands the platforms/runtime variants for which it publishes wheels?

## Object
- Research object: Matplotlib 3.10.5
- Release date: 2025-07-31
- Source family: Matplotlib project release
- Authority: project release notes for released package state
- Accessed: 2026-09-26

## Primary source
- https://matplotlib.org/stable/users/prev_whats_new/github_stats_3.10.5.html
- project release/changelog surfaces for 3.10.5

## Observed release state
The 3.10.5 release includes packaging/runtime-target changes including wheels for Python 3.14, free-threaded Python variants, and Windows ARM, alongside bug fixes.

## Interpretation
A plotting library's version is only one coordinate of render provenance.

The actual execution surface increasingly looks like:

```text
library version
+ Python ABI/runtime variant
+ operating-system/architecture wheel
+ dependent libraries
+ renderer/backend
= candidate runtime identity
```

Adding a wheel does not prove that a particular scientific figure was rendered on that target. It changes the set of environments in which an official package artifact exists.

For a communication pipeline this matters because "Matplotlib 3.10.5" can refer to multiple platform-specific distribution artifacts and runtime contexts.

## Negative space
No 3.10.5 wheel was installed or executed by this reconstruction. No free-threaded Python or Windows ARM render was tested.

## Finding
`G1_FINDING`: Q3 2025 reinforces that renderer provenance should include package/runtime/platform identity, not only a human-readable library version.

# E2 — Matplotlib Patch Release and Render Behavior

## Research question
Can patch-level renderer releases matter to communication identity even without a major grammar change?

## Evidence
Matplotlib 3.10.1 was released 2025-02-27 as the first bugfix release of the 3.10.x series. The release notes include fixes/adjustments for array alpha with RGBA interpolation, `matshow` figure handling, axes-position behavior, polar title positioning and scatter color/facecolor warnings.

Source: https://matplotlib.org/3.10.1/

## Analysis
Patch releases may change concrete rendered behavior or diagnostics while preserving the same high-level API family.

~~~text
same plotting code
+ patch-level renderer change
may change output/diagnostics
~~~

Therefore exact renderer version remains part of reproducibility context. But a bugfix note does not prove every artifact made with an earlier patch is wrong.

## Boundary
~~~text
patch fix exists
!= every prior artifact invalid
release note
!= local reproduction
~~~

## Outcome
`SUPPORTED_OBSERVATION`
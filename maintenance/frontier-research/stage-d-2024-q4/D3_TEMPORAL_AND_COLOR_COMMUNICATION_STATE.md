# D3 — Temporal and Color Communication State

## Question
How do animation state and accessible-color design expand the identity of a scientific communication object?

## Objects and sources
- O5: Vega-Lite 5.23.0, 2024-12-10.
- O6: Matplotlib 3.10.0, 2024-12-13/14 release surface.
- S5: https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
- S6: https://matplotlib.org/stable/users/prev_whats_new/whats_new_3.10.0.html

## Observations
Vega-Lite 5.23.0 added frame animations using time encoding and a timer parameter. This makes temporal state an explicit part of the rendered communication experience.

Matplotlib 3.10.0 added a more-accessible `petroff10` color cycle designed using color-vision-deficiency constraints and an aesthetics model, along with dark-mode diverging colormaps.

## Analysis
The communication object now may depend on:

```text
representation
+ renderer revision
+ interaction state
+ temporal/frame state
+ color/palette state
+ display mode
+ user/device/task context
```

Animation can change what is visible at a given time. Color choices can improve distinguishability for targeted constraints while remaining only one accessibility dimension.

## Counterevidence / limits
- No animation replay or timing-equivalence test was executed.
- "More accessible" color design is not universal accessibility or WCAG certification.
- Color improvements do not validate scientific encoding or claim truth.

## Conclusion
`SUPPORTED_COMMUNICATION_STATE_EXPANSION`.

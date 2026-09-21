# Frontier Research Part C2 — Renderer / Wrapper Version Binding

## Question

How can wrapper and renderer revisions alter communication behavior even when user code appears stable

## Sources

- Altair 5.4.0, released 2024-08-11: https://github.com/vega/altair/releases
- Vega-Lite 5.20.1, 2024-07-31: https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
- Matplotlib 3.9.1, release date 2024-07-04 / announcement 2024-07-06: https://discourse.matplotlib.org/t/matplotlib-announce-ann-matplotlib-3-9-1/24539
- Matplotlib 3.9.2, 2024-08-12: https://matplotlib.org/3.9.2/users/github_stats.html

Altair/Vega-Lite and Matplotlib are distinct project families

## Observations

Altair 5.4.0 upgraded its bundled Vega-Lite from 5.17.0 to 5.20.1

Therefore unchanged high-level Altair code can execute against materially different underlying Vega-Lite semantics after an Altair upgrade

Matplotlib 3.9.1 fixed multiple interaction/backend behaviors including interactive SubFigure updates and IPython-console interactivity

3.9.2 followed as another bugfix state

## Analysis

```text
wrapper version
→ embedded renderer/spec version
→ backend/runtime behavior
→ communication state
```

The wrapper is not semantically isolated from its embedded renderer

Likewise a Matplotlib figure can carry interaction behavior that depends on backend/event-loop/version state

## Counterevidence

No cross-version rerender was executed in this Stage

Not every patch affects every chart

## Conclusion

`SUPPORTED_OBSERVATION`

```text
same user code
!= same communication behavior
across wrapper/renderer/backend revisions
```

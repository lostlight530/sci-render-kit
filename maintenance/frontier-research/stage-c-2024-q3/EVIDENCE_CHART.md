# Evidence Chart — Stage C / 2024-Q3

| Object | Evidence coordinate | Main lesson | Reproduction |
|---|---|---|---|
| Vega-Lite 5.20/5.21 | reactive params / opacity / responsive ticks | interaction/render state is versioned | NOT_EXECUTED |
| Altair 5.4 | embedded Vega-Lite 5.20.1 | wrapper version can change underlying communication semantics | NOT_EXECUTED |
| Matplotlib 3.9.1/3.9.2 | backend/interaction bugfix states | interactive behavior is revision/backend conditioned | NOT_EXECUTED |
| GraphLite | low-vision smartphone personalized interaction | accessibility validation is population/device/task scoped | NOT_EXECUTED |

## Communication-state model

```text
source/scientific context
+ encoding/specification
+ renderer/wrapper/backend revision
+ viewport/size
+ parameter values
+ reactive dependencies
+ interaction/query state
+ modality
+ user configuration
+ accessibility validation population
```

This is a reasoning model, not a universal mandatory schema

## Counterexamples

| Overclaim | Rejection |
|---|---|
| chart is accessible globally because one study succeeds | population-specific evidence only |
| wrapper API unchanged means output semantics unchanged | embedded Vega-Lite changed |
| same data/spec means same interactive state | reactive/render state can change |
| render success proves scientific truth | no |
| low-vision study validates blind screen-reader use | no |

## Amendments

`NONE`

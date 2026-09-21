# Frontier Research Part C1 — Reactive and Interactive Communication State

## Question

When does reactive parameter/interaction state become part of a scientific communication object's provenance

## Sources

- Vega-Lite 5.20.0, 2024-07-30: https://github.com/vega/vega-lite/blob/main/CHANGELOG.md
- Vega-Lite 5.20.1, 2024-07-31
- Vega-Lite 5.21.0, 2024-08-28

One Vega-Lite family

## Observations

5.20.0 exposed a `react` option for parameters and changed tick behavior responsively

5.20.1 fixed conditional opacity so it respects the default value

5.21.0 changed tick behavior for band/timeUnit/custom-band cases and made one-dimensional tick marks responsive to width/height

These are communication-semantics changes: user-visible or interaction-visible states can differ without changing the underlying data

## Analysis

A bounded communication state may need:

```text
data identity
+ encoding/spec identity
+ renderer version
+ parameter values
+ reactive dependency state
+ viewport/size state
+ interaction state
```

Not every figure needs every coordinate, but interactive/reaction-dependent outputs cannot be fully described by static pixels alone

## Limits

No Vega-Lite runtime was executed

No claim is made that every 5.20/5.21 chart changes

## Conclusion

`SUPPORTED_OBSERVATION`

```text
same data/spec
!= same communication state
when reactive/render state changes
```

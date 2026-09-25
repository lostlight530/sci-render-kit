# F1 — Wrapper / Grammar Migration State

## Evidence
On 2025-04-25, the Altair project opened an issue tracking support for `vega-lite>=6`, explicitly treating it as work toward a future Altair 6 major release.

Source: https://github.com/vega/altair/issues/3832

## Analysis
This is a migration-state observation, not a capability release.

```text
upstream grammar major available
+
wrapper migration issue open
!= wrapper major released
!= compatibility verified
```

The event is useful because it exposes an intermediate communication state: upstream specification/runtime changed before the downstream wrapper's major-version migration was established.

## Outcome
`MIGRATION_TRACKED / RELEASE_NOT_ESTABLISHED`

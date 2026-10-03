# Temporal `as_of` Semantics Reconciliation — 2026-10-04

Repository: `lostlight530/sci-render-kit`  
Exact starting main: `6dd840d3c94e90159fa1cc3179c31dff8d5badd4`  
Scope: maintenance-control / temporal-state contract clarification (Asia/Shanghai)

## Confirmed ambiguity

The executable maintenance scanner uses an execution/caller-supplied `as_of` date and derives calendar status from that date. Current render/communication and longitudinal maintenance records can therefore have observation cuts later than the static `MANIFEST.yaml.current_temporal_status.as_of` value.

Before this correction, the repository did not explicitly define whether the manifest field was a daily freshness heartbeat or the date of the latest explicit calendar-state reconciliation. Current main already demonstrates the distinction: the manifest snapshot remains at the 2026-10-01 October month-open transition while successor evidence is current through 2026-10-03.

This is a maintenance-contract ambiguity, not evidence of renderer/backend execution, scientific/statistical validity, accessibility certification, publisher acceptance, or reproduction.

## Correction

- define MANIFEST `current_temporal_status.as_of` as the latest explicit calendar-state reconciliation represented by the static manifest snapshot;
- define scanner/report `as_of` separately as execution or caller-supplied observation date;
- forbid automatic daily MANIFEST date bumps when calendar state is unchanged;
- preserve the 2026-10-01 manifest date as the October month-open reconciliation snapshot;
- preserve renderer/backend implementation, active communication contracts, README/Architecture, DOCUMENT_STATUS, frontier Stage records, FOUR_DAY/FIVE_DAY/SIX_DAY and LONGITUDINAL_INDEX history unchanged.

## Boundaries

```text
runtime report as_of != MANIFEST temporal snapshot date
maintenance freshness != renderer/runtime validation
render success != scientific validity
uncertainty metadata != statistical validation
accessibility support != WCAG certification
maintenance clean != scientific validation
```

## Evidence status

EXECUTED_AS_SOURCE_INSPECTION:
- fresh main and open-PR overlap recovery;
- `core/maintenance_cadence.py` date-derivation inspection;
- current MANIFEST, cadence contract/config, AGENTS and successor-record inspection;
- repository search for an existing explicit temporal-as-of definition (none found).

NOT_EXECUTED:
- local maintenance scanner;
- repository test suite;
- renderer/browser/compiler/backend runtime;
- scientific/statistical validation;
- accessibility/WCAG certification;
- independent reproduction / R3.

This record does not claim render/test/runtime/scientific success.

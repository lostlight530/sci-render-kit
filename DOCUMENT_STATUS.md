# Document Status — sci-render-kit

**Status:** active document-governance map  
**Calibrated:** 2026-08-31  
**Stage:** August 2026 scientific-communication phase closed on 2026-08-31

This file classifies repository documentation by current authority and historical role

## Current authoritative documents

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
FIGURE_CLAIM_CONTRACT.md
COMMUNICATION_TRANSFER_CONTRACT.md
ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md
MAINTENANCE_CADENCE.md
STAGE_2026_08_MAINTENANCE.md
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
metadata/recipe.schema.yaml
metadata/communication_transfer.contract.yaml
```

Authority is scoped by subject

- implementation defines actual renderer/audit/transfer behavior
- `MANIFEST.yaml` is the machine-readable capability map
- `RESEARCH_CONTRACT.md` defines active scientific-integrity semantics
- Figure Claim / Communication Transfer / Assertion Basis contracts define their named communication surfaces
- `MAINTENANCE_CADENCE.md` defines repository-maintenance horizons
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline
- `DOCUMENT_STATUS.md` defines documentation authority/history roles

## Historical snapshots

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

These remain historical records of earlier repository states

They are not current publisher, accessibility, uncertainty, or figure-evidence contracts

Do not rewrite them merely because later backend capabilities, profile names, or scientific-communication boundaries changed

```text
historical snapshot != current contract
later renderer capability != permission to rewrite history
```

## Examples and reference demonstrations

```text
examples/README.md
examples/communication_transfer.md
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

Examples demonstrate supported workflows but do not override implementation, Manifest, schemas, or active contracts

The dated maintenance demonstration is the first complete Daily / Weekly / Monthly worked example for the communication stack
It fixes commands and interpretation without pretending that a clean scanner execution was captured

```text
reference demonstration != entailment evidence
worked maintenance example != publisher validation
```

## External / citation metadata

```text
CITATION.cff
```

Real external/runtime versions such as WCAG 2.2, CFF 1.2.0, Observable Plot 0.6.17, and actually observed backend/library versions remain legitimate provenance metadata

They are not project-owned decorative profile versions

## Stage-close status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The earlier 2026-08-30 `month-to-date` statement remains correct historical context for that date but is no longer the current stage status

## Maintenance rule

Daily maintenance corrects demonstrated recipe, evidence, backend, or documentation drift

Weekly maintenance reconciles communication semantics, backend truth, publisher/WCAG boundaries, and cross-repository profile names

Monthly or explicit phase-close maintenance records a closed baseline and reviews historical/current/experimental status without automatic deletion

The first complete cadence demonstration under `maintenance/` is reference material for onboarding future maintainers and agents after they read the active cadence contract

## Hard boundaries

```text
document current != scientific validity
historical snapshot != invalid
maintenance consistency != entailment
reference demonstration != runtime proof
calendar close != publisher acceptance
monthly baseline != reproduction
```

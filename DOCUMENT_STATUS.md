# Document Status — sci-render-kit

**Status:** active document-governance map  
**Calibrated:** 2026-09-06  
**Stage:** August 2026 scientific-communication phase closed on 2026-08-31

This file classifies repository documentation by current authority and historical role.

## Current authoritative documents

```text
README.md
ARCHITECTURE.md
RESEARCH_CONTRACT.md
FIGURE_CLAIM_CONTRACT.md
COMMUNICATION_TRANSFER_CONTRACT.md
ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md
MAINTENANCE_CADENCE.md
JULES_CORRECTION_RECORD.md
STAGE_2026_08_MAINTENANCE.md
POST_STAGE_REPAIR_2026_09_01.md
MANIFEST.yaml
AGENTS.md
CONTRIBUTING.md
FRONTIER_ALIGNMENT.md
DOCUMENT_STATUS.md
maintenance/cadence.yaml
metadata/recipe.schema.yaml
metadata/communication_transfer.contract.yaml
```

Authority is scoped by subject:

- implementation defines actual renderer/audit/transfer behavior;
- `MANIFEST.yaml` and machine-readable schemas/contracts describe configured capability surfaces;
- `RESEARCH_CONTRACT.md` defines active scientific-integrity semantics;
- Figure Claim / Communication Transfer / Assertion Basis contracts define their named communication surfaces;
- `MAINTENANCE_CADENCE.md` defines repository-maintenance horizons;
- `JULES_CORRECTION_RECORD.md` defines the evidence/authority boundary for historical Jules-created PR/task narratives;
- `STAGE_2026_08_MAINTENANCE.md` is the closed August stage index and baseline;
- `POST_STAGE_REPAIR_2026_09_01.md` records post-close hardening without reopening the stage;
- `DOCUMENT_STATUS.md` defines documentation authority/history roles.

## Authority precedence for recovery

```text
current main implementation
> MANIFEST.yaml / current machine-readable schemas/contracts/configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active communication/scientific-integrity contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> Architecture / README
> historical snapshots
> historical PR/task narratives
```

## Historical snapshots

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

These remain historical records of earlier repository states. They are not current publisher, accessibility, uncertainty, backend, or figure-evidence contracts and should not be rewritten merely because later behavior changed.

## Dated maintenance / correction / research-calibration records

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
POST_STAGE_REPAIR_2026_09_01.md
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
maintenance/FRONTIER_REFRESH_2026_09_01_THROUGH_2026_09_06.md
```

- the 2026-09-06 Daily/Weekly record documents a real authority/cadence reconciliation and does not assert a scanner run, render, backend execution, test run, publisher verdict, WCAG result, or scientific validation;
- the 2026-09-01 through 2026-09-06 frontier refresh is **post-stage, non-normative, source-bounded research calibration** for scientific communication under fast-changing model versions, persistent agents, provider reliability events and enterprise workspaces. It does not change renderer capability, figure-evidence semantics, publisher/WCAG boundaries, or the active Research Contract.

`FRONTIER_ALIGNMENT.md` remains the August stage-close positioning snapshot. The dated frontier refresh is the newer external-research observation record through 2026-09-06 and must not be interpreted as runtime, publisher, accessibility or scientific proof.

Dated records are time-scoped maintenance/research evidence and do not override later implementation changes.

## Historical coding-agent / PR narratives

Early Jules-created PRs remain preserved in GitHub history.

Their task descriptions, PR bodies, automatic summaries, backend-completeness claims, execution/checksum/test statements, security/output-hygiene claims, and completion language are not current contracts or runtime evidence. Read `JULES_CORRECTION_RECORD.md` before reusing them.

```text
historical agent proposal != current authority
claimed backend/test success != current verification
requires re-verification != false
correction != history deletion
```

## Examples and reference material

```text
examples/README.md
examples/communication_transfer.md
```

Examples demonstrate supported workflows but do not override implementation, Manifest, schemas, or active contracts.

## External / citation metadata

```text
CITATION.cff
```

Real external/runtime versions such as WCAG 2.2, CFF 1.2.0, Observable Plot 0.6.17, and actually observed backend/library versions remain legitimate provenance metadata. They are not project-owned decorative profile versions.

## Stage-close and post-stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
```

The 2026-09-01 repair, 2026-09-06 maintenance reconciliation, and 2026-09-01 through 2026-09-06 frontier refresh do not extend or reopen that window.

## Maintenance rule

Daily maintenance corrects demonstrated recipe, evidence, backend, documentation, or governance drift.

Weekly maintenance reconciles communication semantics, backend truth, publisher/WCAG/reproducibility boundaries, current maintenance/correction records, coding-agent authority handling, and cross-repository profile names.

If one pass serves as both Daily and Weekly maintenance, one branch/PR may carry the combined real work; cadence labels do not require duplicate PR churn.

Monthly or explicit phase-close maintenance records a closed baseline and reviews historical/current/experimental status without automatic deletion.

## Hard boundaries

```text
document current != scientific validity
historical snapshot != invalid
post-stage repair != stage rewrite
frontier calibration != renderer verification
external model event != figure validity
maintenance consistency != entailment
reference demonstration != runtime proof
calendar close != publisher acceptance
monthly baseline != reproduction
agent PR narrative != current repository truth
cadence coalescing != skipped maintenance scope
```

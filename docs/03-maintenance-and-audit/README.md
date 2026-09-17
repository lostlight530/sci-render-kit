# 03 — Maintenance and Audit

This class answers: **what maintenance/governance rule applied, what was inspected, what was concluded, who owned the maintenance surface, and what historical evidence must remain reviewable?**

It does **not** define renderer, backend, publisher, accessibility, communication, or scientific truth merely because a record is newer than an active contract.

## Current maintenance / governance surfaces

- [`DOCUMENT_STATUS.md`](DOCUMENT_STATUS.md) — current document-governance router
- [`MAINTENANCE_CADENCE.md`](MAINTENANCE_CADENCE.md) — active human-readable maintenance contract
- root `maintenance/cadence.yaml` — machine-readable maintenance/scanner configuration and control metadata
- [`independent-gpt/README.md`](independent-gpt/README.md) — public cold-start recovery/delivery kernel
- root `AGENTS.md` — operational agent guidance
- root `CONTRIBUTING.md` plus `.github/pull_request_template.md` and `.github/ISSUE_TEMPLATE/governance.md` — collaboration/delivery entry points

`core/maintenance_cadence.py` remains **Class 01 executable source**. Its source/configuration review does not prove the scanner ran.

## Coordinated context

```text
lostlight530/auto-doc-engine
lostlight530/epistemic-pipeline
lostlight530/sci-render-kit
```

Coordination permits shared inspection windows and handoff-vocabulary review. It does not create cross-repository authority.

## Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / metadata / profiles / quality / recipes / current machine configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For renderer/communication semantics, continue to use the most specific implementation, machine contract/configuration, and active subject contract.

## Idempotent ownership

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Before writing, inspect open PRs/live branches for overlapping ownership. Overlap means `COORDINATE`; no confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch/PR. **Write never probes.**

## Dated / historical evidence

The August demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, frontier refresh, and 2026-09-13 month-to-date reconciliation remain point-in-time maintenance evidence. Closed-stage/frontier/FOUR/FIVE/SIX_DAY/Jules-correction/superseded-plan material under `history/` remains historical evidence.

A later record may report a newer observation or correction, but it does not silently override implementation, machine contracts, publisher/accessibility/runtime facts, or active scientific/communication contracts.

## Communication boundaries

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile/alignment != acceptance
accessibility support != WCAG certification
backend source != runtime availability
communication transfer != inherited scientific authority
```

## Validation and delivery boundary

```text
checker available != checker executed
checker executed != checker passed
historical render/test pass != current pass
contract inspection != runtime verification
Draft PR != merge approval or validation success
```

Record an unrun check as `NOT_EXECUTED`; use `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

When a real repair exists, verify aggregate branch diff, refresh current-main/overlap state, open one bounded **Draft PR**, and stop for maintainer review. Do not auto-merge or write maintenance repairs directly to `main`.

When current state conflicts with a dated record, preserve the dated record and correct forward in current governance or a later reconciliation record.

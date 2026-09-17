---
name: Contract or communication reconciliation
about: Report drift between current implementation, rendering/evidence contracts, maintenance control, and current documentation
title: "[Governance] "
labels: ""
assignees: ""
---

## Drifted claim or surface
Identify the exact renderer behavior, recipe/schema/profile semantics, machine contract, maintenance rule, metadata surface, or current document that is inconsistent.

## Current repository basis
- Current `main` revision:
- Owning surface/task:
- Logical period/evidence window, when applicable:
- Relevant live PR/branch ownership:

Distinguish current implementation/contract authority from dated maintenance and historical snapshots.

## Proposed reconciliation
Describe the minimum semantically complete correction and every dependent current surface that must stay synchronized.

If another live owner covers the same surface/period, record `COORDINATE`. If inspection confirms no defect, record `NO_CHANGE_REQUIRED` rather than manufacturing a change.

## Communication boundary
State whether any renderer success, entailment, statistical validity, publisher acceptance, WCAG conformance, backend availability, or scientific validity is involved. Do not silently strengthen structural evidence.

## Execution evidence
State what was actually executed, what was only inspected, and what remains `NOT_EXECUTED` or `EXECUTION_NOT_OBSERVED`.

## Historical preservation
State which dated maintenance/snapshot artifacts remain point-in-time evidence and whether a forward correction/reconciliation is required.

## Public/private boundary
Do not attach private Jules prompts, hidden reasoning, repository memory, credentials, or unrelated operator context.

## Review and rollback
Define non-goals, expected Draft-PR delivery boundary if a repair is accepted, and the smallest rollback.

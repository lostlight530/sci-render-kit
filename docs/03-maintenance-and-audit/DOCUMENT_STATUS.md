# Document Status — sci-render-kit

**Status:** active document-governance router  
**Calibrated:** 2026-09-17  
**Stage:** August 2026 scientific-communication phase closed on 2026-08-31

This file routes repository materials by current role and authority. It is a classifier/router, not an independent source of renderer, backend, publisher, accessibility, communication, or scientific truth.

See `docs/README.md` for the three-class taxonomy.

## Class 01 — source and explanation

Primary implementation/explanatory surfaces include:

```text
sci_render.py
core/
backends/
tests/
Makefile
package.json
README.md
docs/01-source-and-explanation/ARCHITECTURE.md
```

Implementation determines actual renderer/audit/transfer behavior. `core/maintenance_cadence.py` is executable source; source presence is not scanner execution.

## Class 02 — examples and contracts

Current capability/configuration surfaces include:

```text
MANIFEST.yaml
metadata/
profiles/
quality/
recipes/
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/02-examples-and-contracts/FIGURE_CLAIM_CONTRACT.md
docs/02-examples-and-contracts/COMMUNICATION_TRANSFER_CONTRACT.md
docs/02-examples-and-contracts/ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md
examples/
AGENTS.md
CONTRIBUTING.md
CITATION.cff
LICENSE
```

Machine-readable presence does not itself establish scientific validity, publisher acceptance, WCAG certification, backend runtime availability, statistical validity, or entailment.

## Class 03 — maintenance and audit

Current maintenance/governance surfaces:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/governance.md
```

The Independent GPT file is a public cold-start recovery/delivery router inside Class 03. It does not create a fourth class or outrank implementation/machine contracts/active subject contracts.

Dated maintenance records, including the August demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, frontier refresh, and 2026-09-13 month-to-date reconciliation, remain point-in-time maintenance evidence.

Closed-stage/frontier/FOUR/FIVE/SIX_DAY/Jules-correction/superseded-plan material under `history/` remains historical evidence.

## Two authority questions must not be collapsed

### Renderer / communication semantics

```text
current implementation
> current schema/profile/configuration/machine contract for the subject
> active subject-specific contract
> executable/operational evidence for supported use
> current explanatory documentation
> maintenance evidence
> historical records
```

### Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / metadata / profiles / quality / recipes / machine configuration
> latest relevant dated repair or current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

A newer maintenance record does not outrank implementation for renderer behavior, publisher acceptance, accessibility conformance, or scientific validity.

## Maintenance task ownership

```text
repository
+ owning surface/task
+ logical period/evidence window
+ producer/maintainer
+ exact base revision
+ run identity when available
```

Before writing, inspect open PRs/live branches for overlapping ownership. Same owning surface/period with another live owner means `COORDINATE`. No confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch/PR. **Write never probes.**

## Communication hard boundaries

```text
render success != scientific validity
claim binding != entailment
claim relation = explicit declaration only
uncertainty metadata != statistical validation
publisher profile/alignment != acceptance
accessibility support/metadata != WCAG certification
backend source != runtime availability
communication transfer != inherited authority
assertion basis != correctness
coverage != quality
coverage ratio != probability
```

## Dated evidence interpretation

The 2026-08-31 demonstration is historical/reference evidence, not an automatically preserved clean scanner/render/test run. The 2026-09-01 repair does not reopen August. The frontier refresh is source-bounded calibration, not renderer execution or scientific validation.

The 2026-09-13 reconciliation remains valid point-in-time evidence that the pass found `NO_CHANGE_REQUIRED` for renderer/communication semantics, refreshed maintenance observation through 2026-09-13, kept September month-to-date, and did not fabricate absent scanner/render/test execution. It does not mechanically advance `MANIFEST.yaml` capability/frontier calibration.

```text
maintenance freshness != renderer/communication capability calibration
latest observation != highest semantic authority
NO_CHANGE_REQUIRED != skipped inspection
```

## Execution evidence boundary

```text
implementation presence != execution evidence
scanner source != scanner execution
checker definition != checker execution
contract inspection != checker PASS
historical render/test PASS != current PASS
```

Unrun checks are `NOT_EXECUTED`. Unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.

## Historical preservation

Do not rewrite historical bodies merely because current terminology, paths, or behavior changed. Correct forward through a current owning file or later dated reconciliation.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
agent completion claim != current verification
path relocation != semantic change
```

## Stage status

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: closed
research_phase: closed
September 2026: month-to-date until natural month close
```

## Delivery boundary

For a confirmed repair, verify aggregate diff and live overlap, open one bounded **Draft PR**, and stop for maintainer review. Do not auto-merge, force-push, or write maintenance repairs directly to `main`.

```text
Draft PR != validation success
classification != deletion authority
calendar close != reproduction
```

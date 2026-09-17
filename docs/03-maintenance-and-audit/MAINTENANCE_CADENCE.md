# Maintenance Cadence — sci-render-kit

**Status:** active maintenance contract  
**Calibrated:** 2026-09-17  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates Daily, Weekly, and Monthly maintenance for the scientific-communication layer. It is not a scheduler, renderer validator, scientific validator, publisher validator, WCAG certifier, or GitHub merge gate.

## Authority recovery before every pass

For maintenance-control recovery use:

```text
current merged main implementation
> MANIFEST.yaml / metadata / profiles / quality / recipes / current machine configuration for the subject
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> maintenance/cadence.yaml and this cadence contract
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

For renderer/communication semantics, use the most specific implementation, machine contract/configuration, and active subject contract. Maintenance recency does not become renderer or scientific authority.

## Maintenance identity and idempotency

Record, when applicable:

```text
repository
owning surface / task
logical period or evidence window
producer / maintainer
exact base revision
run identity when available
```

Before any write, inspect open PRs/live branches for the same owning surface and logical period.

```text
overlap -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed current drift -> REPAIR
unsafe or unrecoverable evidence/access -> BLOCKED
```

`NO_CHANGE_REQUIRED` follows real inspection. Do not create activity-only branch/PR churn. **Write never probes.**

## Cadence model

```text
daily
  local recipe / figure-evidence / backend-boundary drift
        ↓
weekly
  cross-day communication-stack / authority / maintenance reconciliation
        ↓
monthly or explicit phase-close
  calendar baseline / full current communication-document inventory
```

Cadence labels do not require duplicate delivery. One real correction may satisfy Daily and Weekly in one branch and one Draft PR.

## Daily

Required behavior:

- start from current merged `main`;
- use `DOCUMENT_STATUS.md` to identify current authority and retained history;
- read the latest relevant dated repair/current maintenance record before older snapshots when relevant;
- preserve explicit/non-inferred claim bindings;
- preserve figure-evidence and communication-transfer profile names;
- preserve reproducibility context without upgrading it to independent reproduction;
- preserve uncertainty labels without upgrading them into validated statistics;
- preserve exact WCAG scope and publisher-preset boundaries;
- preserve real runtime/backend versions while rejecting decorative project versions;
- treat coding-agent PR/task narratives as proposal/delivery metadata unless current evidence independently supports them;
- record checks actually executed separately from checks merely available;
- create at most one bounded Draft PR when a real repair exists.

Daily maintenance must not infer claim relations from pixels/captions/legends/prose, rename publisher findings into acceptance, rename accessibility support into WCAG conformance, reuse historical backend/test/render claims as current verification without re-checking, rewrite history for neatness, or manufacture a change merely to satisfy cadence.

## Weekly

Weekly maintenance includes Daily checks plus full current-communication reconciliation:

- implementation ↔ `MANIFEST.yaml` ↔ metadata/profiles/quality/recipes ↔ active contracts;
- README / Architecture / Contributor / Examples consistency;
- `DOCUMENT_STATUS.md` against files actually present;
- current maintenance configuration, recovery kernel, operator/delivery surfaces, and dated maintenance evidence;
- claim communication audit ↔ figure evidence ↔ communication transfer consistency;
- reproducibility-context preservation across figure evidence/transfer;
- upstream Auto/Epistemic handoff names;
- uncertainty semantics, backend capability truth, WCAG scope, and publisher wording;
- retained historical snapshots without rewriting them;
- whether coding-agent narratives are being treated as current backend/runtime/publisher/scientific authority without current evidence;
- SHA-256 baseline only when the local scanner is actually used.

### Daily + Weekly coalescing

```text
one evidence-backed correction
!= two required PRs because two cadence labels apply
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest non-destructive communication-stack review.

Required behavior:

- derive calendar status from the actual date;
- use `month-to-date` before natural month close and `calendar-month-close` only at natural month close;
- reconcile the complete current communication/control set;
- inventory historical evidence non-destructively;
- review current / experimental / proposed / not-integrated labels;
- confirm publisher/accessibility/runtime findings have not been promoted into scientific verdicts;
- never convert calendar closure into reproduction or scientific validation.

The August 2026 scientific-communication phase remains closed after 2026-08-31.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of YYYY-MM-DD --output output/communication-maintenance-YYYY-MM-DD.json
```

The scanner enforces declared repository-local structural scope. It does not render figures, inspect pixels, call external services, run tests, validate statistics, certify WCAG conformance, predict publisher acceptance, establish independent reproduction, inspect GitHub PR ownership, or validate historical Jules claims.

## Execution evidence

```text
scanner source present != scanner executed
scanner executed != scanner passed
historical render/test pass != current pass
structural pass != scientific validity
contract inspection != runtime verification
```

If a relevant check was not run, record `NOT_EXECUTED`. If execution itself was not observed, use `EXECUTION_NOT_OBSERVED` when material.

## Dated maintenance evidence

The August demonstration, 2026-09-01 repair, 2026-09-06 reconciliation, frontier refresh, and 2026-09-13 month-to-date reconciliation remain point-in-time maintenance evidence. They are not silently rewritten into current render/runtime/publisher/accessibility/scientific evidence.

`MANIFEST.yaml` capability/frontier calibration changes only when actual renderer/communication capability semantics change. Maintenance freshness alone does not authorize a capability bump.

## History and correction discipline

Preserve closed-stage consolidations, frontier alignment, Jules correction, and superseded design evidence.

```text
historical snapshot != current contract
historical != invalid
later success != earlier success
correction != history rewrite
path relocation != semantic change
```

Correct forward through a current owning file or later dated reconciliation.

## Delivery contract

When a repair is confirmed:

1. branch from the exact observed current `main`;
2. modify only owning control surfaces and true synchronized dependencies;
3. inspect aggregate `main...branch` diff;
4. refresh current-main and overlap state;
5. record executed/unexecuted checks separately;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`.

## Shared boundaries

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile/alignment != acceptance
accessibility support != WCAG certification
backend source != runtime availability
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
reproducibility context != independent reproduction
report written != figure validated
agent task / PR narrative != current repository truth
claimed backend/test success != current runtime verification
cadence label != duplicate PR requirement
maintenance calibration != renderer capability transition
Draft PR != validation success
```

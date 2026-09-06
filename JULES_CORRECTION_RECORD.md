# Jules Correction Record — sci-render-kit

**Status:** active correction / authority record  
**Calibrated:** 2026-09-06  
**Scope:** historical Jules-created pull-request narratives and their relationship to current repository truth

## Purpose

This record does not declare historical Jules work invalid and does not rewrite old pull requests.

It corrects one authority ambiguity: early automated-agent PR descriptions include backend, execution, quality-gate, checksum, test, completeness, and security claims. Those remain useful point-in-time delivery metadata, but they are not durable current renderer/scientific authority by themselves.

```text
agent task / PR narrative != current repository truth
claimed test pass != current runtime verification
historical completion claim != permanent backend capability
proposal wording != normative communication contract
```

## Historical Jules PRs in scope

- PR #1 — `feat: implement unified quality gates, complete all chart backends, and add enterprise architecture docs`
- PR #2 — `Enhance adapters and CLI memory rules logic`
- PR #3 — `chore: align system with strict memory rules and output hygiene`

Each was created automatically by Jules for a user-started Jules task. Their PR bodies remain historical task/delivery narratives.

Statements about all backends being complete, generated code being executed, checksums being real, P2/P3 behavior, tests passing, strict security/memory alignment, or equivalent completion language are time-scoped assertions unless the current revision independently re-establishes them.

## Current authority order

```text
current main implementation
> MANIFEST.yaml and current machine-readable schemas/contracts/configuration
> latest dated repair / current maintenance record
> DOCUMENT_STATUS.md
> AGENTS.md
> active communication/scientific-integrity contracts
> MAINTENANCE_CADENCE.md and maintenance/cadence.yaml
> Architecture / README
> historical consolidation snapshots
> historical PR / task narratives, including Jules
```

Subject-specific contracts remain authoritative for their named surface.

## Correction rules

### J-C01 — PR body is not merged state

An unmerged agent PR is a proposal. After merge, the repository fact is the actual resulting tree on `main`, not every statement in the PR body.

### J-C02 — Execution and backend claims expire unless reverified

Historical test counts, render/run success, backend availability, checksum behavior, publisher/quality-gate behavior, or completeness claims must be reverified against the current revision before reuse as current evidence.

### J-C03 — Rendering success is not scientific or publisher authority

Historical agent wording does not override current boundaries:

```text
render success != scientific validity
claim binding != entailment
publisher preset != acceptance
accessibility support != WCAG certification
reproducibility context != independent reproduction
```

### J-C04 — Correct forward; do not rewrite history

If current implementation, machine contracts, or active documentation supersede an old agent narrative, preserve the historical PR and record the correction in current documentation or a dated repair/maintenance record.

```text
superseded != fabricated
requires re-verification != false
historical != current
```

## Current sci-render-kit calibration

The current repository has materially evolved beyond the early Jules PR descriptions. Current authority includes explicit figure-claim audit, assertion basis / communication coverage, figure evidence, communication transfer, reproducibility-context preservation, publisher/WCAG boundaries, maintenance cadence, document authority, and post-stage repair semantics.

Therefore early Jules PRs are development history, not a substitute for current implementation/machine contracts and not publisher, accessibility, scientific-validity, or independent-reproduction evidence.

## External calibration

Google's Jules guidance states that generated code should still be carefully reviewed before use even when agent-side review mechanisms are present. Later Jules evaluation work also focuses on measuring useful agent insight rather than treating confident completion language as correctness.

Primary references checked 2026-09-06:

- Google Developers Blog — `Meet Jules’ sharpest critic and most valuable ally` (2025-08-12)
- Google Developers Blog — `Measuring What Matters with Jules` (2026-06-22)

These references calibrate governance only. They do not prove any historical repository change wrong.

## Durable boundary

```text
agent assistance != repository authority
review mechanism != infallibility
PR metadata != runtime proof
backend execution claim != current backend availability
current main != historical PR prose
correction record != deletion of history
```

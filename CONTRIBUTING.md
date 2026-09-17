# Contributing

Contributions should strengthen explicit scientific-figure semantics, communication integrity, or maintenance clarity rather than only increase renderer/module count.

## Repository boundaries

Keep changes scoped to the owning layer: recipe schema, runtime rules, backend adapter, accessibility, publisher preset, claim communication, assertion basis, communication coverage, figure evidence, communication transfer, maintenance, or documentation.

Do not introduce GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as ordinary maintenance.

## Before changing the repository

Read current authority and maintenance surfaces:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/independent-gpt/README.md
AGENTS.md
MANIFEST.yaml
```

For maintenance work, start from exact current merged `main`, inspect live PRs/branches for overlapping ownership, and identify the owning surface before writing.

Record, when applicable:

```text
repository + owning surface/task + logical period/evidence window
+ producer/maintainer + exact base revision + run identity when available
```

Overlap means `COORDINATE`. No confirmed defect means `NO_CHANGE_REQUIRED` and no activity-only branch/PR. **Write never probes.**

## Current document authority

Current implementation/machine contracts/active contracts own present behavior for their subjects. Historical `*_DAY_CONSOLIDATION.md` and other records under `docs/03-maintenance-and-audit/history/` remain point-in-time evidence.

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## Scientific communication integrity

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile/alignment != acceptance
accessibility support != WCAG certification
backend source != runtime availability
communication transfer != inherited scientific authority
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
coverage != provenance soundness
```

Unknown metadata stays unknown. Never invent provider, model, version, source, review, runtime availability, publisher acceptance, WCAG conformance, or validation status.

Claim relations remain explicit and must not be inferred from pixels, captions, filenames, legends, prose, or data values.

## Communication transfer

Preserve explicit non-inheritance:

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

A transfer must not infer destination, publication status, review authority, or claim meaning from filenames, captions, pixels, or prose.

## Compatibility and cross-repository semantics

When a public field/semantic changes, synchronize the owning code or machine contract, active communication contracts, Manifest, examples, and public documentation as required.

Do not strengthen upstream references silently:

```text
artifact/claim ref -> trusted evidence       # prohibited
claim audit coverage -> scientific validity # prohibited
human review -> peer review                 # prohibited
supports relation -> proof                  # prohibited
claim transfer -> accepted claim            # prohibited
```

## Maintenance workflow

```text
daily -> bounded demonstrated recipe/evidence/backend/document drift
weekly -> current implementation / machine contract / documentation reconciliation
monthly -> calendar-month or explicit phase-close baseline
```

Cadence is not an obligation to manufacture a change. Daily/Weekly work may coalesce into one real branch/PR when they own the same correction.

The maintenance scanner `.py` implementation is not rewritten merely to synchronize governance prose. Source/config inspection is not scanner execution.

Before delivery:

1. verify aggregate diff against exact base;
2. refresh current `main` and live overlap;
3. list checks actually executed and checks not run;
4. open one bounded **Draft PR**;
5. stop for maintainer review.

Use `NOT_EXECUTED` for an unrun checker/test and `EXECUTION_NOT_OBSERVED` when execution itself was not observed.

```text
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
checker source != checker execution
Draft PR != validation success
```

## Public/private boundary

Do not publish private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public governance may encode the effect of a rule without copying private control text.

Final review, doctrine, and merge authority remains with the maintainer.

## License

Contributions are licensed under the repository license.

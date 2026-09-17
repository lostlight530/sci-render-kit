# Agent Guide — sci-render-kit

This is the operational contract for agents modifying the repository.

Keep runtime code, schemas, profiles, evidence sidecars, maintenance control, current documentation, and historical-document status semantically aligned without turning agent narrative into renderer or scientific truth.

## Document authority

Read `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` before broad documentation or governance maintenance.

Use `docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md` only when interpreting early Jules task/PR prose as historical renderer/backend/publisher/accessibility/scientific evidence. It is dated correction evidence, not a current authority layer.

```text
historical snapshot != current contract
later renderer capability != permission to rewrite history
historical agent PR narrative != current communication contract
```

## Recovery orders

### Maintenance-control recovery

```text
current merged main implementation
> MANIFEST.yaml / metadata / profiles / quality / recipes / machine configuration
> latest relevant dated repair or current maintenance record
> docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
> AGENTS.md
> active subject-specific contracts
> docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md / maintenance/cadence.yaml
> current Architecture / README explanation
> historical snapshots / superseded plans / PR-task narratives
```

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

A newer maintenance record does not become stronger renderer, publisher, accessibility, or scientific authority merely because of date.

## Maintenance task identity

Record, when applicable:

```text
repository
+ owning surface / task
+ logical period or evidence window
+ producer / maintainer
+ exact base revision
+ run identity when available
```

Before any write, inspect open PRs/live branches for the same owning surface and logical period.

```text
overlap -> COORDINATE
no confirmed defect -> NO_CHANGE_REQUIRED
confirmed current drift -> REPAIR
unsafe or unrecoverable evidence/access -> BLOCKED
```

Do not create repository objects to test write access. **Write never probes.**

## Canonical architecture

```text
recipe
  -> P0 schema
  -> P1 runtime + claim communication audit
       ├─ assertion basis
       └─ dimensional communication coverage
  -> backend capability resolution
  -> render
  -> render-manifest / provenance / a11y
  -> P2 artifact integrity
  -> P3 publisher-target alignment
  -> figure-evidence
  -> optional communication-transfer
       └─ explicit non-inheritance constraints

repository state
  -> daily / weekly / monthly maintenance
       └─ current-document / calendar / stage / delivery reconciliation
```

## Stable project identifiers

Use stable unversioned project-owned profile names. Preserve real WCAG/external/runtime versions when genuinely known. Do not invent decorative internal versions.

## Hard rules

1. Schema does not imply backend support.
2. Do not silently change DPI, format, uncertainty semantics, or declared data.
3. Claim bindings are explicit only and never inferred from titles, legends, pixels, prose, filenames, or data values.
4. Claim relation labels are communication declarations, not verified entailment.
5. Process disclosure is bounded and does not adjudicate authorship, peer review, or truth.
6. Unknown provider/model/version/review/source metadata remains unknown.
7. The canonical renderer does not infer AI authorship/use from text or pixels.
8. Assertion basis records how a field entered evidence and never upgrades a value to correctness.
9. Communication coverage remains dimensional and must not become an unsupported aggregate quality score.
10. Coverage ratios are not probability, entailment, evidence sufficiency, or provenance soundness.
11. Bounds alone are not a confidence interval or probability model.
12. WCAG scope stays exact; project all-pairs checks remain extra safeguards.
13. CVD simulation is extra and not normative WCAG certification.
14. Publisher presets are snapshots/config targets, not acceptance validators.
15. Optional backend source does not prove runtime availability.
16. Figure evidence is handoff, not truth.
17. Communication transfer may copy declared context but must not inherit scientific validity, entailment, evidence sufficiency, statistical validity, peer review, publisher acceptance, or WCAG conformance.
18. Unsupported experimental methods fail explicitly rather than fabricate output.
19. Calendar/month/stage status comes from actual date/configuration.
20. A worked maintenance demonstration is not a clean runtime result unless the scanner actually ran and output was preserved.
21. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, or merge-gate architecture as routine maintenance.
22. Agent task text/PR bodies/summaries/completion claims are proposal/delivery metadata, not automatic repository authority.
23. Historical `tests passed`, backend execution, checksum, `complete`, `fully aligned`, or `fixed` require current re-verification before reuse.
24. Correct historical overstatement forward; do not rewrite old PR history.
25. Path relocation does not change semantic status.
26. Scanner/checker source or configuration inspection is not execution.
27. Unrun checks are `NOT_EXECUTED`; unobserved scheduler/workflow execution is `EXECUTION_NOT_OBSERVED` when material.
28. A Draft PR is a review boundary, not renderer/test/scientific/merge success.
29. No confirmed maintenance defect means no activity-only branch or PR.

## Communication-audit invariants

```text
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
supports evidence-context coverage != evidence sufficiency
coverage != provenance soundness
```

Keep `aggregate_score: null` unless a future validated evaluation design explicitly justifies a composite score.

## Communication-transfer invariants

```text
transfer != entailment
upstream ref != inherited validity
uncertainty metadata != statistical validation
publisher target != acceptance
accessibility metadata != WCAG certification
human review != peer review
```

Destination and purpose are caller-declared when present and must not be inferred.

## Coding-agent provenance

Before reusing a historical agent statement, distinguish:

```text
what the PR body claimed
what actually entered merged main
what current main does now
what current machine contracts say
what was actually re-run or re-verified now
```

Historical backend/test/render/checksum/publisher wording does not establish current runtime success, publisher acceptance, WCAG certification, scientific validity, entailment, or independent reproduction.

## Maintenance cadence

The active maintenance system is jointly owned by:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
core/maintenance_cadence.py
```

The `.py` scanner is executable implementation. Governance prose changes do not by themselves require rewriting it, and source/config inspection is not scanner execution.

Local scanner:

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of YYYY-MM-DD
```

Daily corrects demonstrated recipe/evidence/backend/profile/document/governance drift only and permits `NO_CHANGE_REQUIRED` without branch/PR churn.

Weekly reconciles implementation, machine contracts, active communication contracts, README/Architecture, Agent/Contributor guidance, examples, document status, maintenance configuration/records, checker ownership, and upstream profile names.

Monthly/phase-close derives calendar/phase state from the actual date and never converts closure into reproduction or scientific validation.

If Daily and Weekly own the same real correction, one branch and one final Draft PR should carry it whenever practical.

## Execution evidence

```text
scanner source present != scanner executed
scanner executed != scanner passed
historical render/test pass != current pass
contract inspection != runtime verification
```

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| recipe field | `metadata/recipe.schema.yaml` | runtime + docs + evidence semantics |
| claim binding/audit/coverage | claim-audit / figure-evidence implementation | communication contracts + Manifest + examples |
| communication transfer | transfer implementation | transfer contract + machine contract + examples |
| maintenance cadence / agent provenance | `core/maintenance_cadence.py`, `maintenance/cadence.yaml` | Maintenance Cadence + Document Status + maintenance README + Independent GPT router + Agent Guide + current dated maintenance record; synchronize runtime scanner/Manifest only when executable/profile/path semantics actually change |
| accessibility | accessibility implementation/runtime | a11y + backend truth |
| backend | corresponding adapter | Manifest/provenance capability truth |
| publisher profile | `profiles/*.yaml` | source status + acceptance false |
| public capability | README / Architecture / active contracts / Manifest | update together when semantics change |

## Cross-repository references

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
sci-render-kit/communication-transfer
```

These are optional handoff references, not direct coupling or inherited scientific validity.

## Experimental semantics and R3

Metaphorical filenames are not scientific capability evidence. Experimental/importable modules are not canonical capability until intentionally integrated.

Render manifests, figure evidence, communication transfers, accessibility sidecars, maintenance reports, demonstrations, and canonical hash baselines never count as independent reproduction. R3 requires an actual separate rerun plus a declared comparison criterion.

## Delivery boundary

For a confirmed maintenance repair:

1. branch from exact observed current `main`;
2. synchronize owning control surfaces and true dependencies only;
3. inspect aggregate branch diff;
4. refresh current-main/open-PR overlap;
5. record executed/unexecuted checks separately;
6. open one bounded **Draft PR**;
7. stop for maintainer review.

Do not auto-merge, force-push, or write maintenance repairs directly to `main`. Final doctrine and merge authority remains with the maintainer.

## Public boundary

Do not publish private Jules prompts, repository memory, hidden reasoning, credentials, or unrelated operator context. Public governance may preserve the effect of a rule without copying private control text.

# Maintenance Cadence — sci-render-kit

**Status:** active maintenance contract  
**Calibrated:** 2026-09-15  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the scientific-communication layer. It is not a scheduler, scientific validator, publisher validator, or GitHub merge gate.

## Authority recovery before every pass

Use the most specific current subject authority rather than document date or legacy path placement:

```text
current main implementation
> current machine-readable capability contract / schema / configuration for the subject
> active docs/02-examples-and-contracts/RESEARCH_CONTRACT.md and active specialized contract for the subject
> operational examples / configuration / test evidence for supported use
> README / docs/01-source-and-explanation/ARCHITECTURE.md / current explanatory documentation
> maintenance / audit / reconciliation evidence
> historical snapshots / superseded plans / PR-task narratives
```

The historical `docs/03-maintenance-and-audit/history/JULES_CORRECTION_RECORD.md` records the 2026-09-06 correction boundary for earlier coding-agent task/PR narratives. Its historical authority-order wording does not override the current subject-scoped order above.

## Cadence model

```text
daily
  local recipe / figure-evidence / backend-boundary drift
        ↓
weekly
  cross-day communication-stack and document-authority reconciliation
        ↓
monthly or explicit phase-close
  calendar baseline / full communication-document inventory / deprecation review
```

## Daily

Required checks:

- start from current `main`;
- use `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` to identify current authoritative documentation;
- read the latest relevant dated repair/current maintenance record before older snapshots or PR narratives;
- verify claim bindings remain explicit and non-inferred;
- verify figure-evidence and communication-transfer profile names remain stable;
- preserve reproducibility context through communication transfer without upgrading it to independent reproduction;
- preserve uncertainty labels without upgrading them into validated statistics;
- preserve WCAG scope and publisher-preset boundaries;
- preserve real runtime/backend versions while rejecting decorative project versions;
- keep unsupported composite quality scores absent or null;
- incorporate external work only when it changes a real communication-contract decision;
- treat Jules/Codex/other coding-agent PR/task narratives and historical backend/test/completeness claims as proposal/delivery metadata unless current evidence independently supports them;
- create at most one final maintenance PR for the repository.

Daily maintenance must not infer claim relations from pixels/captions/legends/prose, rename publisher findings into acceptance, rename accessibility support into WCAG conformance, rewrite historical snapshots or PR prose, promote a historical backend/test claim into current verification without re-checking, or add GitHub-native merge governance.

## Weekly

Weekly maintenance includes daily checks plus complete current-communication reconciliation:

- implementation ↔ machine contracts ↔ active contracts under `docs/02-examples-and-contracts/`;
- root README / `docs/01-source-and-explanation/ARCHITECTURE.md` / Contributor / Examples consistency;
- `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` against files actually present;
- current dated maintenance records;
- claim communication audit ↔ figure evidence ↔ communication transfer consistency;
- reproducibility-context preservation across figure evidence and transfer;
- upstream Auto / Epistemic profile names;
- uncertainty semantics and backend capability truth;
- WCAG 2.2 scope and publisher-preset wording;
- historical snapshots without rewriting them;
- frontier calibration freshness;
- whether coding-agent narratives are being treated as current backend/runtime/publisher/scientific authority without current evidence;
- canonical SHA-256 baseline when the local scanner is used.

### Daily + Weekly coalescing

If one real maintenance pass serves as both Daily and Weekly reconciliation, prefer one branch and one final PR for the combined work.

```text
one evidence-backed correction
!= two required PRs because two cadence labels apply
```

Both scopes must be documented; duplicate cosmetic changes or duplicate PRs must not be manufactured.

## Monthly / explicit phase-close

Monthly maintenance performs the strongest communication-stack review while remaining non-destructive.

For the closed August stage:

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

On and after 2026-09-01 that stage remains closed; post-stage hardening and later maintenance do not reopen it.

Before the natural September month boundary, a monthly maintenance pass records `month-to-date`; it must not be represented as a calendar-month close.

Historical consolidation and closed-stage inventory lives under `docs/03-maintenance-and-audit/history/`.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-06 --output output/communication-maintenance-2026-09-06.json
```

Configured canonical / scan / governance paths must be repository-relative; absolute paths, `..`, and resolutions outside the repository fail closed; repository-local config identity is SHA-256-bound; duplicate paths are warnings; and report output is only written when explicitly requested.

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not render figures, inspect pixels, call external services, run tests, verify scientific entailment, validate statistics, certify WCAG conformance, predict publisher acceptance, establish independent reproduction, or validate historical Jules PR/task claims.

## Dated maintenance evidence

The first complete worked example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

The post-stage repair is:

```text
maintenance/POST_STAGE_REPAIR_2026_09_01.md
```

The previous Daily/Weekly governance reconciliation is:

```text
maintenance/DAILY_WEEKLY_RECONCILIATION_2026_09_06.md
```

The current Daily/Weekly/month-to-date reconciliation record is:

```text
maintenance/DAILY_WEEKLY_MONTH_TO_DATE_RECONCILIATION_2026_09_13.md
```

These are dated maintenance records, not renderer/runtime/publisher/accessibility/scientific-validation evidence. The 2026-09-13 record keeps `MANIFEST.yaml` capability/frontier calibration distinct from maintenance-layer freshness unless actual renderer/communication semantics change.

## Historical evidence

Closed-stage consolidations, frontier alignment, and the dated Jules correction live under `docs/03-maintenance-and-audit/history/`. Their paths changed; their point-in-time claims did not.

## External calibration

Long-horizon and scientific-agent work continues to emphasize process-level inspection, explicit interfaces and state, and the difference between a completed action and a scientifically valid conclusion. Current Google Jules guidance also preserves a careful-review boundary for generated code and evaluates agent insight quality rather than assuming completion language equals correctness.

These are design signals only. They do not validate this repository, establish an optimal maintenance interval, or prove any historical Jules change wrong.

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
reproducibility context != independent reproduction
publisher profile != acceptance
accessibility support != WCAG certification
provenance != truth
report written != figure validated
agent task / PR narrative != current repository truth
claimed backend/test success != current runtime verification
cadence label != requirement for duplicate PR churn
maintenance calibration != renderer capability transition
path relocation != semantic change
```

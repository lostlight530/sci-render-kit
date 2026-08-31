# Maintenance Cadence — sci-render-kit

**Status:** active maintenance contract  
**Calibrated:** 2026-09-01  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the scientific-communication layer. It is not a scheduler, scientific validator, publisher validator, or GitHub merge gate.

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
- use `DOCUMENT_STATUS.md` to identify current authoritative documentation;
- verify claim bindings remain explicit and non-inferred;
- verify figure-evidence and communication-transfer profile names remain stable;
- preserve reproducibility context through communication transfer without upgrading it to independent reproduction;
- preserve uncertainty labels without upgrading them into validated statistics;
- preserve WCAG scope and publisher-preset boundaries;
- preserve real runtime/backend versions while rejecting decorative project versions;
- keep unsupported composite quality scores absent or null;
- incorporate external work only when it changes a real communication-contract decision;
- create at most one final maintenance PR for the repository.

Daily maintenance must not infer claim relations from pixels/captions/legends/prose, rename publisher findings into acceptance, rename accessibility support into WCAG conformance, rewrite historical snapshots, or add GitHub-native merge governance.

## Weekly

Weekly maintenance includes daily checks plus complete current-communication reconciliation:

- implementation ↔ machine contracts ↔ Research Contract ↔ Figure Claim Contract ↔ Communication Transfer Contract;
- README / Architecture / Contributor / Examples consistency;
- `DOCUMENT_STATUS.md` against files actually present;
- claim communication audit ↔ figure evidence ↔ communication transfer consistency;
- reproducibility-context preservation across figure evidence and transfer;
- upstream Auto / Epistemic profile names;
- uncertainty semantics and backend capability truth;
- WCAG 2.2 scope and publisher-preset wording;
- historical snapshots without rewriting them;
- frontier calibration freshness;
- canonical SHA-256 baseline when the local scanner is used.

## Monthly / explicit phase-close

Monthly maintenance performs the strongest communication-stack review while remaining non-destructive.

For the closed August stage:

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

On 2026-09-01 that stage remains closed; post-stage hardening does not reopen it.

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional report output:

```bash
python core/maintenance_cadence.py daily --as-of 2026-09-01 --output output/communication-maintenance-2026-09-01.json
```

### 2026-09-01 portability and scope repair

- configured canonical / scan / governance paths must be repository-relative;
- absolute paths, `..`, and resolutions outside the repository root fail closed;
- historical inventory paths are repository-relative rather than machine-local absolute paths;
- repo-local configuration is recorded by relative path plus `configuration_file_sha256`;
- external configuration is labeled external without embedding the full machine path;
- duplicate configured paths are warnings;
- `repository_scope_enforced: true` is explicit.

The precise write boundary is now:

```text
inspected_files_mutated: false
report_output_write_requested: true | false
report_output_inside_repository: true | false | null
```

The scanner does not rewrite inspected recipe/evidence/code/configuration/history. It may write only the report explicitly requested by the caller.

## Scanner checks

The scanner reports configured paths, scope violations, forbidden governance paths, decorative project versions, Manifest freshness, configuration identity, optional canonical hashes, historical snapshots, calendar-month status, and configured stage status.

It does not render figures, inspect pixels, call external services, run tests, verify scientific entailment, validate statistics, certify WCAG conformance, predict publisher acceptance, or establish independent reproduction.

## First complete cadence demonstration

The first complete worked example remains:

```text
maintenance/FIRST_COMPLETE_CADENCE_DEMONSTRATION_2026_08_31.md
```

It is reference material, not a fabricated clean scanner result.

## External calibration

Long-horizon and scientific-agent work continues to emphasize process-level inspection, explicit interfaces and state, and the difference between a completed action and a scientifically valid conclusion. The 2026-09-01 communication repair applies that principle narrowly: handoff must preserve the source reproducibility semantics, while scanner scope and write behavior remain explicit.

These are design signals only. They do not validate this repository or establish an optimal maintenance interval.

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
```

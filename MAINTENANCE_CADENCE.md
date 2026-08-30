# Maintenance Cadence — sci-render-kit

**Status:** active maintenance contract  
**Calibrated:** 2026-08-31  
**Current closed stage:** 2026-08-24 through 2026-08-31

This contract separates daily, weekly, and monthly maintenance for the scientific-communication layer

It is not a scheduler, scientific validator, publisher validator, or GitHub merge gate

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

Daily maintenance remains narrow and source-grounded

Required checks

- start from current `main`
- use `DOCUMENT_STATUS.md` to identify current authoritative documentation
- verify claim bindings remain explicit and non-inferred
- verify figure-evidence and communication-transfer profile names remain stable
- preserve uncertainty labels without upgrading them into validated statistics
- preserve WCAG scope and publisher-preset boundaries
- preserve real runtime/backend versions while rejecting decorative project versions
- keep unsupported composite quality scores absent or null
- incorporate external work only when it changes a real communication-contract decision
- create at most one final maintenance PR for the repository

Daily maintenance must not

- infer claim relations from pixels, captions, legends, prose, or data values
- rename publisher-target findings into acceptance
- rename accessibility support into whole-publication WCAG conformance
- rewrite historical stage snapshots
- add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates

## Weekly

Weekly maintenance includes daily checks plus complete current-communication reconciliation

Required review

- implementation ↔ machine contracts ↔ Research Contract ↔ Figure Claim Contract ↔ Communication Transfer Contract
- README / Architecture / Contributor / Examples consistency
- `DOCUMENT_STATUS.md` against files actually present
- claim communication audit ↔ figure evidence ↔ communication transfer consistency
- upstream Auto / Epistemic profile names
- uncertainty semantics and backend capability truth
- WCAG 2.2 scope and publisher-preset wording
- previous seven days of historical snapshots without rewriting them
- frontier calibration freshness
- canonical SHA-256 baseline when the local scanner is used

Weekly questions

```text
Did a daily change make a claim binding implicit
Did an evidence-context ratio become a scientific score
Did an uncertainty label become a validated-method claim
Did a publisher profile become an acceptance claim
Did backend source presence become runtime-availability proof
Did a historical snapshot get treated as current authority
Did a cross-repository profile name drift
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest communication-stack review

Required behavior

- determine actual calendar status from the date
- use `month-to-date` before the final day and `calendar-month-close` on the final day
- inventory historical snapshots
- hash configured canonical contract/runtime/documentation files
- reconcile every current authoritative document in `DOCUMENT_STATUS.md`
- review integrated / experimental / proposed / not-integrated labels
- review stale-document candidates manually
- reconcile all merged month changes against current figure evidence and transfer surfaces
- confirm exact WCAG / publisher / uncertainty boundaries remain intact
- record whether an explicit research phase is active or closed

For the current stage

```text
as_of: 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

Hard boundaries

```text
monthly review != publisher validation
phase close != history rewrite
communication coverage != entailment
clean figure stack != scientific validity
calendar close != reproduction
```

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

Optional close report

```bash
python core/maintenance_cadence.py monthly --as-of 2026-08-31 --output maintenance/august-close.json
```

The scanner reports configured canonical paths, forbidden governance paths, decorative project-profile versions, Manifest calibration freshness, optional canonical hashes, historical snapshots, calendar-month status, and configured stage status

It does not render figures, inspect pixels, call external services, run tests, verify scientific entailment, validate statistics, certify WCAG conformance, or predict publisher acceptance

## Document authority and history

`DOCUMENT_STATUS.md` is the current map of authoritative, historical, example, and external-metadata documents

Historical `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, and `SIX_DAY_CONSOLIDATION.md` remain time-scoped snapshots rather than current contracts

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## External calibration

The cadence design is informed by long-horizon research work emphasizing phase structure, persistent/recoverable state, regime-aware re-validation, process-level evaluation beyond final scores, and re-openable provenance

These are design signals only

They do not establish an optimal figure-maintenance interval or validate this repository

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != entailment
calendar-month close != reproduction
publisher profile != acceptance
accessibility support != WCAG certification
provenance != truth
```

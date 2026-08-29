# Maintenance Cadence — sci-render-kit

**Status:** active maintenance contract  
**Calibrated:** 2026-08-30

This contract separates daily, weekly, and monthly maintenance for the scientific-communication layer

It is not a scheduler, not a scientific validator, and not a GitHub merge gate

## Cadence model

```text
daily
  local recipe / figure-evidence / backend-boundary drift
        ↓
weekly
  cross-day communication-contract reconciliation
        ↓
monthly or explicit phase-close
  canonical baseline / history inventory / deprecation review
```

## Daily

Daily maintenance should remain narrow and source-grounded

Required checks

- start from current `main`
- verify claim bindings remain explicit and non-inferred
- verify figure-evidence and communication-transfer profile names remain stable
- preserve uncertainty labels without upgrading them into validated statistics
- preserve WCAG scope and publisher-preset boundaries
- preserve real runtime/backend versions while rejecting decorative project versions
- keep `aggregate_score: null` on unsupported composite-quality surfaces
- incorporate new external work only when it changes an actual communication-contract decision
- create at most one final maintenance PR for the repository

Daily maintenance must not

- infer claim relations from pixels, captions, legends, prose, or data values
- rename publisher-target findings into acceptance
- rename accessibility support into whole-publication WCAG conformance
- rewrite historical stage snapshots
- add GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates

## Weekly

Weekly maintenance includes daily checks plus cross-day reconciliation

Required review

- implementation ↔ machine contracts ↔ Research Contract ↔ Figure Claim Contract ↔ Communication Transfer Contract
- claim communication audit ↔ figure evidence ↔ communication transfer consistency
- upstream Auto / Epistemic profile names
- uncertainty semantics and backend capability truth
- WCAG 2.2 scope and publisher preset wording
- previous seven days of stage snapshots without rewriting history
- frontier calibration freshness
- canonical SHA-256 baseline when the local scanner is used

Weekly questions

```text
Did a daily change make a claim binding implicit
Did an evidence-context ratio become a scientific score
Did an uncertainty label become a validated method claim
Did a publisher profile become an acceptance claim
Did backend source presence become runtime-availability proof
Did a cross-repository profile name drift
```

## Monthly / explicit phase-close

Monthly maintenance performs the strongest communication-stack review

Required behavior

- build a month-to-date or explicit phase-close baseline
- inventory historical consolidation snapshots
- hash canonical contract/runtime files
- review integrated / experimental / proposed / not-integrated labels
- review stale-document candidates manually
- reconcile all merged month changes against the current figure evidence and transfer stack
- confirm exact WCAG/publisher/uncertainty boundaries remain intact
- state explicitly whether the month is closed or only month-to-date

On 2026-08-30 the August record is **month-to-date**, not final calendar-month close

Hard boundaries

```text
monthly review != publisher validation
phase close != history rewrite
communication coverage != entailment
clean figure stack != scientific validity
```

## Deterministic local scanner

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-30
```

Optional report

```bash
python core/maintenance_cadence.py weekly --output maintenance/weekly-report.json
```

The scanner checks configured canonical paths, forbidden governance paths, decorative project-profile versions, Manifest calibration freshness, optional canonical hashes, and optional historical snapshots

It does not render figures, inspect pixels, call external services, run tests, verify scientific entailment, validate statistics, certify WCAG conformance, or predict publisher acceptance

## History rule

Historical stage notes remain evidence of earlier repository state

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## External calibration

The cadence design is informed by long-horizon research work emphasizing phase structure, persistent/recoverable state, regime-aware re-validation, and re-openable provenance

These are design signals only

They do not establish an optimal figure-maintenance interval or validate this repository

## Shared boundaries

```text
maintenance clean != scientific validity
weekly consistency != entailment
monthly baseline != reproduction
publisher profile != acceptance
accessibility support != WCAG certification
provenance != truth
```

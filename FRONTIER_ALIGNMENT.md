# Frontier Alignment — sci-render-kit

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-30

`sci-render-kit` addresses preserving scientific communication semantics when figures are produced inside AI-assisted or agentic workflows

## Current engineering thesis

The relevant artifact is not only an image

```text
figure
+ recipe/data/profile/backend identity
+ accessibility context
+ uncertainty semantics
+ declared claim-to-visual relations
+ assertion basis
+ dimensional communication coverage
+ process disclosure
+ runtime findings
+ provenance / upstream evidence refs
+ explicit downstream transfer constraints
```

This does not make the renderer a scientific verifier
It makes the communication artifact more inspectable and safer to hand downstream

## Assertion provenance

```text
claim binding / process / uncertainty -> recipe-declared
figure bytes                         -> runtime-observed-local-bytes
upstream ref resolution              -> runtime-observed-local-filesystem
```

```text
assertion basis != correctness
```

The renderer records `automatic_ai_detection_used: false` and does not infer AI authorship/use from captions, prose, pixels, or metadata

## Communication coverage

Sci Render computes only the communication-layer coverage it can directly observe

```text
claim-index/binding coverage
binding evidence-context coverage
supports evidence-context coverage
process-disclosure field coverage
```

No aggregate scientific-quality score is computed

```text
communication coverage != entailment
coverage ratio != probability
coverage != provenance soundness
reference context != evidence sufficiency
```

## Day-6 communication transfer without inherited authority

`core/communication_transfer.py` creates a bounded transfer view over an existing figure-evidence sidecar

It carries claim communication, upstream research context, uncertainty semantics, process disclosure, communication audit, and runtime validation while explicitly preventing automatic authority inheritance

```text
scientific_validity_inherited: false
entailment_inherited: false
evidence_sufficiency_inherited: false
statistical_validity_inherited: false
peer_review_inherited: false
publisher_acceptance_inherited: false
accessibility_conformance_inherited: false
```

## Day-7 phase-aware maintenance

Long-horizon research studies increasingly show that workflow phase and recovery structure matter independently of model capability

A behavioural case study of long-horizon autonomous architecture research reports clear phase transitions and recommends regime-aware re-validation

ScienceFlow organizes long-horizon scientific/ML research into persistent research segments to preserve evolving state and recover from dead ends

Autonomous-science provenance work likewise emphasizes re-openable records that can be audited and corrected

Borrowed maintenance principle

```text
different drift horizons deserve different review scopes
```

The repository therefore distinguishes

```text
daily
  local recipe / figure-evidence / backend-boundary drift

weekly
  cross-day communication-contract reconciliation

monthly or explicit phase-close
  canonical hash baseline / history inventory / deprecation review
```

This is implemented in `MAINTENANCE_CADENCE.md`, `maintenance/cadence.yaml`, `core/maintenance_cadence.py`, and `STAGE_2026_08_MAINTENANCE.md`

The scanner is read-only and local
It does not render figures, inspect pixels, run tests, validate statistics, certify WCAG conformance, or predict publisher acceptance

On 2026-08-30 the August maintenance snapshot is month-to-date, not final calendar-month close

```text
maintenance clean != scientific validity
weekly consistency != entailment
monthly baseline != reproduction
history inventory != deprecation decision
```

## Global signals used for calibration

Current calibration includes

- re-openable provenance for autonomous science
- transparent AI use and human oversight in scientific publishing
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- Brain Researcher evidence-bounded claims
- EarthVerse end-to-end consistency gaps
- claim-level auditability separating coverage from soundness
- Praxist solution/evidence lineage
- ReproAgent persistent implementation contracts
- long-horizon autonomous architecture research with phase-aware re-validation
- ScienceFlow segmented long-horizon research and recovery
- living research-software maintenance and metadata

These sources calibrate architecture only
They do not validate the renderer, certify a publisher target, establish WCAG conformance, or prove novelty

## Distinct layer

Existing plotting libraries remain deeper and more mature at rendering itself
This repository focuses on explicit communication semantics and handoff

```text
upstream research artifact / claim audit
        ↓
declared scientific communication semantics
        ↓
assertion basis + communication coverage
        ↓
rendered figure + evidence sidecars
        ↓
communication-transfer with non-inheritance constraints
```

## Cross-repository position

```text
auto-doc-engine
  artifact identity / basis / coverage / lineage
        ↓
epistemic-pipeline
  claim/evidence audit / transfer / provenance
        ↓
sci-render-kit
  claim-aware communication / figure evidence / communication transfer
```

Together the repositories explore evidence-aware research infrastructure with explicit inheritance and maintenance boundaries

## Hard boundaries

```text
figure evidence != scientific validity
assertion basis != correctness
communication coverage != entailment
coverage ratio != probability
claim binding != entailment
communication transfer != entailment
upstream reference != inherited validity
supports label != evidence sufficiency
publisher preset != acceptance
accessibility support != whole-document conformance
maintenance clean != scientific validity
monthly baseline != reproduction
provenance != truth
checksum != reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

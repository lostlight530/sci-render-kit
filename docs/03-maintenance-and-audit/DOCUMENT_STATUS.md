# Document Status — sci-render-kit

**Status:** active document-governance router  
**Calibrated:** 2026-09-17  
**Stage note:** the August 2026 scientific-communication phase closed on 2026-08-31

This file classifies current repository surfaces by role and authority. It is a router, not an independent source of renderer behavior, backend availability, publisher acceptance, accessibility conformance, communication validity, or scientific truth.

See `docs/README.md` for the repository documentation taxonomy.

## Class 01 — implementation and explanation

Primary implementation and explanatory surfaces:

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

Implementation determines actual renderer, audit, transfer, and sidecar behavior. README and Architecture explain current behavior and must remain bounded by implementation and active contracts.

`core/maintenance_cadence.py` is executable source. Source presence is not scanner execution.

## Class 02 — machine configuration, communication contracts, examples, and scholarly metadata

Current capability and communication constraints include:

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
codemeta.json
RELEASE_POLICY.md
LICENSE
```

Machine-readable presence does not establish scientific validity, publisher acceptance, WCAG certification, backend runtime availability, statistical validity, or entailment.

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` describe public software discovery, citation, release, and archival identity.

```text
repository DOI != figure validity
citation metadata != publisher acceptance
publication identity != backend availability
DOI != R3 reproduction
```

## Class 03 — current maintenance and repository governance

Current maintenance surfaces include:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/
```

These files govern maintenance, recovery, contribution, and delivery behavior. They do not outrank implementation, machine configuration, or subject-specific communication contracts for renderer/scientific semantics.

## Historical and dated evidence

Dated maintenance records and materials under `history/` remain point-in-time evidence. The August stage, frontier material, FOUR/FIVE/SIX_DAY consolidations, correction records, demonstrations, and later dated reconciliations remain recoverable at their original time boundary.

```text
historical snapshot != current contract
current path presence != earlier execution
later success != earlier success
correction != history rewrite
```

A later current document can narrow or correct interpretation without pretending that the corrected meaning existed at the earlier observation time.

## Current authority by question

### Renderer / communication question

```text
current implementation
> current schema/profile/configuration/machine contract for the subject
> active subject-specific contract
> revision-matched executable/operational evidence
> current explanatory documentation
> current maintenance/document router
> historical records
```

### Publication or citation question

```text
CITATION.cff / codemeta.json / RELEASE_POLICY.md / DOI record
```

These identify the software publication and citation surface; they do not validate a figure, source claim, uncertainty method, accessibility conformance, or publisher acceptance.

### Maintenance/document-routing question

Use the current maintenance contract, this router, cadence configuration, and current repository state. Dated maintenance records inform history but remain time-scoped.

## Scientific communication hard boundaries

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

## Execution evidence boundary

```text
implementation presence != execution evidence
scanner source != scanner execution
checker definition != checker execution
contract inspection != checker PASS
historical render/test PASS != current PASS
```

Unknown or unexecuted evidence remains unknown or unexecuted. A documentation, metadata, or profile update must not manufacture render/runtime evidence.

## Current stage interpretation

The 2026-08-24 through 2026-08-31 scientific-communication phase is closed. Later maintenance and publication updates do not reopen that historical phase.

Current September state must be recovered from current repository truth and current dated records rather than copied from an August or earlier September snapshot.

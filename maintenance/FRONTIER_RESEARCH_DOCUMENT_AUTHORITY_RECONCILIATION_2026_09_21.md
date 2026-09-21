# Frontier Research Document-Authority Reconciliation — 2026-09-21

**Repository:** `lostlight530/sci-render-kit`  
**Status:** current dated maintenance reconciliation  
**Base revision:** `3040080c93a8ef90e96750d6f5e639da218ffefd`  
**Result:** `REPAIR` for document-authority routing only  
**Implementation/runtime change:** none

## Confirmed drift

The 2026-09-19 first-batch frontier-research family introduced `maintenance/frontier-research/FIRST_BATCH_SPECIFICATION.md` with status `active research-documentation specification / non-normative to repository runtime`.

The current `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` was calibrated on 2026-09-17 and did not classify `maintenance/frontier-research/` as a current authority surface.

This was a current document-router drift. It was not a runtime, capability, renderer/communication, scientific-validity, or historical-execution defect.

## Repair

- advanced the document-router calibration date to 2026-09-21;
- added an explicit active frontier-research documentation class;
- bound the first-batch specification to documentation-method authority only;
- preserved implementation, `MANIFEST.yaml`, machine configuration, and active subject-specific contracts as higher authority for runtime/capability questions;
- preserved historical records and forward-only correction semantics.

## Deliberately unchanged

- runtime and implementation source
- `MANIFEST.yaml`
- active subject-specific scientific-integrity contracts
- historical FOUR/FIVE/SIX_DAY and August stage records
- GitHub Actions and scheduler surfaces

## Verification

Executed:

- fresh remote `main` recovery;
- open PR and branch overlap check;
- current first-batch specification inspection;
- current document-router inspection;
- exact-base branch creation;
- remote branch diff verification after the router update.

Not executed:

- repository-local maintenance scanner;
- tests, compile, renderer/provider execution, or runtime checks;
- scientific-validity or reproduction checks.

`NOT_EXECUTED` remains the correct status for those checks. No PASS is inferred from source presence.

## Final boundary

```text
frontier-research documentation method != runtime capability
structured research artifact != scientific truth
research handoff != authority transfer
correction != history rewrite
```

This repair is ready for maintainer review and must not be interpreted as a runtime capability change.

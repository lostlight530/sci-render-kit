# Post-Stage Repair — sci-render-kit — 2026-09-01

**Status:** current repair note for the closed August scientific-communication stage  
**Stage remains closed:** 2026-08-24 → 2026-08-31

This repair hardens current handoff and maintenance behavior without rewriting or reopening the closed stage.

## Repairs

### Reproducibility context survives communication transfer

`core/communication_transfer.py` now preserves the source figure-evidence `reproducibility` object.

This keeps the distinction between replay-addressable evidence and an actually reproduced result visible downstream.

```text
R1 context preserved != R3 achieved
reproducibility metadata copied != independent rerun executed
```

The transfer adds `independent_reproduction_inherited: false` and `independent_reproduction_claim: false`.

### Machine contract synchronization

`metadata/communication_transfer.contract.yaml` now lists `reproducibility` as copied context and includes `reproducibility_context_present` in descriptive transfer coverage.

### Maintenance-report portability and scope

The maintenance scanner now emits repository-relative portable paths, binds configuration bytes by SHA-256, rejects configured paths that escape the repository root, and records optional report-output writes accurately.

## External calibration checked through 2026-09-01

Current long-horizon and scientific-agent work reinforces two narrow engineering lessons relevant here:

- intermediate state and constraints should remain inspectable across handoffs rather than being reconstructed from terminal output;
- action completion and scientific validity are separate properties, especially as scientific agents move toward explicit physical experiment interfaces.

These are design signals only. They do not certify this renderer, its figures, its publisher presets, or its accessibility behavior.

## Boundaries

```text
reproducibility context != independent reproduction
communication transfer != entailment
config hash != configuration correctness
scope containment != scientific validity
publisher profile != acceptance
accessibility support != WCAG certification
provenance != truth
```

No GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates are introduced. No test execution is used as completion evidence.

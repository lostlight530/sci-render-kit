# Figure claim and communication transfer — source-derived negative cases

**Document class:** durable specialized research method, independent of periodic reports  
**Source baseline:** `main@df9c2424f661b2f0ef258f0064f4480dc8395913`, inspected 2026-11-15  
**Owning contracts:** [Figure Claim](./FIGURE_CLAIM_CONTRACT.md), [Communication Transfer](./COMMUNICATION_TRANSFER_CONTRACT.md), [Assertion Basis and Coverage](./ASSERTION_BASIS_AND_COMMUNICATION_COVERAGE.md)  
**Implementations:** `core/claim_binding_audit.py`, `core/figure_evidence.py`, `core/communication_transfer.py`

## Central research problem

A figure can be correctly generated, correctly linked to a declared Claim ID, and correctly transferred with a byte digest while still communicating a claim that its underlying data cannot support

The source creates three distinct evidence planes:

```text
recipe research_context / claim_bindings
   -> audit_claim_communication                [declared metadata consistency]
rendered figure + recipe + backend evidence
   -> build_figure_evidence                    [observed local bytes and declared context]
figure-evidence sidecar
   -> build_communication_transfer             [copy of bounded source information]
```

Neither an audit summary nor a successfully generated sidecar is an independent review of a graph's statistical, causal, or scientific meaning

## Code-grounded negative cases

| ID | Controlled input and variation | Exact source path | Supported result / rejected inference |
| --- | --- | --- | --- |
| F-1 | One `claim_bindings` entry uses `relation="supports"` with a `visual_ref`, `claim_refs` and opaque `evidence_ref` | `claim_binding_audit.py::claim_communication_coverage` | May count as a valid declaration with evidence context, not proof that the reference supports the proposition |
| F-2 | Change only the actual chart values but leave the same recipe's declared Claim ID and relation | `audit_claim_communication` | This function inspects recipe metadata, not pixels, chart data semantics or scientific entailment |
| F-3 | Repeat an identical `visual_ref/relation/claim_refs/evidence_ref` tuple | `audit_claim_communication` | Duplicate binding warning is documentary hygiene, not a truth check |
| F-4 | Add a `provenance_ref` string without validating the URI or paper | `claim_communication_coverage` | Evidence-context counts can rise without stronger actual support, `aggregate_score=None` |
| F-5 | Change the file bytes of a rendered PNG while retaining a prior figure-evidence sidecar | `figure_evidence.py::file_sha256` | A digest from the original production time does not continuously monitor later bytes, a separate read-back is needed for any later identity claim |
| F-6 | Transfer an evidence sidecar with an uncertainty field whose statistical method is incorrect | `communication_transfer.py::build_communication_transfer` | The field is copied after structural checks, not independently statistically validated |
| F-7 | A plot passes publisher style checks while visual content or source numbers are misleading | runtime-quality vs claim-audit profiles | Publisher-oriented profile success does not prove publisher acceptance or claim validity |

## Evidence obligations for an actual figure study

For every strong plotted conclusion, name (1) source dataset and exact version, (2) transformation and loss of information, (3) measured quantity and population/denominator, (4) uncertainty construction and assumptions, (5) visual encoding and potentially misleading alternatives, (6) external proposition the figure is meant to support, (7) accessibility and publisher criteria separately

For any execution claim retain the exact source revision, recipe, figure bytes, figure-evidence sidecar bytes and SHA-256, backend and installed version, original claim text, data source, independent validation procedure, command and actual result

**Status:** new negative-case runs `NOT_EXECUTED`, scientific truth/peer review `NOT_VERIFIED`, no code behavior added or implied by this document

The owning specialized contracts continue to define the implemented JSON and transfer fields, this companion defines falsifiable interpretation tests only

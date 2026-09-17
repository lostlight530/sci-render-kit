# Contributing

Contributions should strengthen scientific-figure semantics, renderer correctness, communication integrity, accessibility, reproducibility, documentation, or public metadata without turning presentation success into scientific validation.

## Start from the owning surface

Keep a change with the layer that owns it:

- renderer/runtime implementation and tests;
- recipe schemas and machine-readable metadata;
- backend adapters and capability boundaries;
- quality, accessibility, publisher-target, uncertainty, and communication contracts;
- figure evidence and communication-transfer records;
- `MANIFEST.yaml` and active contracts;
- current explanatory documentation;
- repository infrastructure such as `.github/`, security, citation, CodeMeta, and release metadata.

Use `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` to distinguish current contracts from dated/historical records.

## Scientific communication integrity

Keep these boundaries explicit:

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile != acceptance
accessibility support != WCAG certification
backend source != runtime availability
communication transfer != inherited scientific authority
assertion basis != correctness
coverage ratio != probability
repository DOI != figure validity
```

Unknown metadata stays unknown. Do not invent provider/model versions, publisher acceptance, accessibility conformance, source authority, or review state.

Claim relations remain explicit declarations and must not be inferred from pixels, captions, filenames, legends, prose, or data values.

## Implementation and contract changes

For executable or machine-contract changes:

1. define or reproduce the behavior at a named revision;
2. add or update proportionate tests/fixtures;
3. update the owning schema/profile/quality/communication contract when semantics change;
4. synchronize `MANIFEST.yaml`, examples, and explanatory docs where required;
5. retain explicit non-inheritance constraints for communication transfer.

Backend source presence is not evidence that a backend runtime is installed or semantically equivalent to another backend.

## Verification

Run tests, rendering checks, schema/profile validation, accessibility checks, or external tools relevant to the changed surface and supported by the environment. Record exact commands and observed results.

Do not report an unrun backend, publisher validator, accessibility audit, or renderer check as passed. Engineering validation of a rendered artifact is not scientific validation of the underlying claim.

## Documentation and historical evidence

Prefer the smallest current owning document. Do not rewrite historical snapshots merely because terminology or current behavior changed. Correct current interpretation forward while retaining earlier point-in-time evidence.

## Publication and citation metadata

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` describe the public software publication. A DOI identifies an archived software object; it does not prove scientific validity, publisher acceptance, accessibility conformance, backend availability, or R3 reproduction.

## Pull requests

Use the repository pull-request template and include:

- the problem and bounded change;
- affected renderer/schema/profile/contract/example/documentation/metadata surfaces;
- scientific-communication implications;
- verification actually performed;
- relevant backends/tools/checks not exercised;
- compatibility and historical impact;
- security/privacy impact;
- a practical rollback.

## Security, privacy, license, and attribution

Follow `SECURITY.md` for sensitive reports. Do not publish credentials, private data, or exploit details requiring coordinated disclosure.

Contributions to repository-owned work are licensed under the repository license. Third-party material retains its original attribution and licensing, and Git/PR history remains the source of contribution attribution.

# Interoperability, Runtime Verification and Offline Packaging — sci-render-kit

**Status:** current source and explicit optional test guidance, not publisher or WCAG certification

## Cross-repository consumer contract

`core/figure_evidence.py` records a figure's local output identity, declared claim bindings and **optional local byte hashes** of upstream `epistemic-pipeline/evidence-envelope`, `epistemic-pipeline/claim-verification`, or `auto-doc-engine/artifact-record` references. It does not dereference remote URIs or establish upstream profile authenticity, scientific validity or claim entailment

`core/communication_transfer.py` accepts an existing `sci-render-kit/figure-evidence` sidecar and copies bounded declared context while explicitly refusing scientific-validity, publisher-acceptance and independent-reproduction inheritance. `tests/test_cross_repo_contract.py` exercises these actual consumers using ephemeral upstream fixtures, not a three-repository installed end-to-end run

## JSON Schema dialect

`metadata/recipe.schema.yaml` and `metadata/reproducibility.schema.yaml` declare JSON Schema Draft 2020-12 explicitly. The contract test runs `Draft202012Validator.check_schema` against both; this is meta-schema validation, not semantic correctness or complete recipe/backend conformance

## Real Matplotlib integration check

`tests/test_render_integration.py` invokes the **actual Matplotlib backend** with a temporary recipe/output directory and checks PNG and final render-manifest/figure-evidence hashes, the stable accessibility profile, and explicit no-scientific-validity flags. It is separate from mock tests. Its result is unknown until `make test` has executed on a revision-matched environment

## Observable: online and caller-supplied offline modes

Online mode preserves `@observablehq/plot@0.6.17` via jsDelivr at browser view time, explicitly recording that network requirement

Offline mode requires **both** existing, nonempty local files, as described in Observable Plot's official UMD guide: https://observablehq.github.io/plot/getting-started

```text
/local/umd-bundles/
  d3.min.js
  plot.umd.min.js
```

```bash
python sci_render.py recipes/line-chart-interactive.yaml --backend observable --profile presentation --offline-assets /local/umd-bundles
# or use the Node backend directly:
node backends/observable_adapter.js render recipes/line-chart-interactive.yaml --profile presentation --offline-assets /local/umd-bundles
```

The adapter never downloads those files. It verifies source files remain inside the given asset root, refuses missing/empty inputs and conflicting existing output bytes, copies the bundles next to the HTML, removes CDN imports from the generated HTML, and records local dependency paths and SHA-256 hashes in the render manifest

**Important:** no third-party bundles are shipped in this repository. A caller must acquire, version-check and license-review the D3 and Plot UMD assets. The emitted offline dependency `version` remains `null` and `version_verified=false`, even though the project declares an *expected* Plot version. Byte identity does not establish upstream authenticity or browser runtime success. This mode addresses HTML viewer dependencies, not installation of Node/Python/R dependencies

`tests/test_observable_offline.js` checks asset staging, hash agreement, URL-free generated HTML and refusal of conflicting outputs using **dummy JS bytes**; it is explicitly not a real Plot/D3 browser render. Actual Plot/D3 browser behavior and offline accessibility require separate browser tests

## Verification scope and environment

Python verification baseline: **Python 3.13** and `requirements-python313.txt`, with both direct and observed transitive distribution versions pinned

```bash
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-python313.txt
python scripts/check_python_environment.py
make test
```

The version checker emits a JSON result and a nonzero exit code on mismatch. This is a bounded **version-set snapshot**, not a PEP 751 `pylock.toml`, a wheel-hash lock, a cross-platform guarantee, a validated new installation, or scientific reproduction. Reconcile a fresh Python 3.13 resolver output and archive package hashes/environment provenance when stronger byte-level replay is needed

The pre-existing optional `.github/workflows/tool-cli-agent-smoke.yml` runs the same bounded checks when matching PR paths trigger it. Workflow definition is not run evidence; inspect the workflow run and commit SHA before claiming execution success

## Scholarly metadata migration

`codemeta.json` uses the official CodeMeta 4.0 context `https://w3id.org/codemeta/4.0` (released 2026-09-29) rather than 3.1. Existing publication DOI, author, license and repository metadata are not rewritten. CodeMeta 4 changes the CodeMeta namespace and schema.org's HTTP/HTTPS mapping, and removes `relatedSoftware` (unused here). The local contract test verifies syntax and CITATION.cff field identity, **not** a remotely expanded JSON-LD graph, external repository index, or citation resolver

Official release: https://github.com/codemeta/codemeta/releases/tag/4.0

## Protocol boundaries

No MCP server, A2A agent service, OTel exporter, independently authenticated approval workflow, publisher certification, scientific truth verification, or R3 independent reproduction is created by these tests


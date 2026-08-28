# Scientific communication transfer example

Create a bounded downstream handoff from an existing figure-evidence sidecar.

```bash
python core/communication_transfer.py \
  output/figure.evidence.json \
  --destination manuscript-main-text \
  --purpose publication-handoff \
  --output output/figure.communication-transfer.json
```

The transfer keeps claim refs/bindings, upstream research references, uncertainty semantics, process disclosure, communication audit and runtime validation.

It does not infer anything from figure pixels, captions or filenames.

```text
communication transfer != entailment
upstream reference != inherited validity
uncertainty metadata != statistical validation
publisher target != acceptance
accessibility metadata != WCAG certification
```

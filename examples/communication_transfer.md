# Scientific communication transfer example

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 通信 sidecar 示例展示显式的图像与声明引用，不是审稿、出版或真实科研证据的替代

**English owning title:** Scientific communication transfer example

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |


**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


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

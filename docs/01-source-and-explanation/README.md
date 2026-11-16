# 01 — Source and Explanation

## 中文专业正文对照 / Chinese technical counterpart

**具体研究对象 / Concrete subject:** 本索引标出绘图实现与研究说明的来源，导航不构成已执行验证

**English owning title:** 01 — Source and Explanation

**图像证据判别 / Figure evidence reading:** 应分别取得源数据版本、recipe/profile、实际后端输出、manifest、声明绑定、上游 sidecar 与可访问性实测结果，不能将图像 bytes、示例文档或测试定义视为实际同行评审 / Keep source, recipe, backend, manifest and claim identities separate, verify the exact execution evidence before asserting quality or reproducibility

| English original section / 英文原章 | 中文对应定位 / Chinese section meaning |
| --- | --- |
| Implementation map | 该图像合同的局部机制与证据限制 |
| Architecture and explanation | 该图像合同的局部机制与证据限制 |
| Scientific-communication boundaries | 该图像合同的局部机制与证据限制 |
| Cross-layer reading | 该图像合同的局部机制与证据限制 |

**限界 / Limits:** 原有配置、图形行为与未知执行状态保持不变，本节不新增科学审定、出版接纳、WCAG 认证或真实浏览器通过声明 / Original behaviors and unknown states are unchanged, no scientific or publisher certification is implied


This class answers three durable questions:

1. **What does sci-render-kit actually implement?**
2. **Where are renderer/backend and scientific-communication boundaries explained?**
3. **Which successful outputs are engineering/render evidence rather than scientific validation?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| root `sci_render.py` | public/CLI rendering entry surface | successful invocation does not certify the scientific meaning of a figure |
| `core/` | recipe interpretation, communication/evidence logic, repository-owned rendering rules | implemented predicates remain narrower than scientific validity |
| `backends/` | backend adapters and backend-specific behavior | backend source presence != backend runtime availability in every environment |
| `tests/` | revision-scoped engineering/regression evidence | passing tests do not prove entailment, publisher acceptance, or accessibility conformance |
| root `Makefile` | supported engineering command entry points | command presence != command execution |
| root `package.json` | declared JavaScript/tooling metadata where applicable | declaration/installability != successful execution |

The maintenance scanner remains implementation source even when it supports class 03 materials. Scanner source is not scanner execution.

## Architecture and explanation

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed renderer/backend architecture, schema/profile/quality relationships, communication integrity boundaries, and cross-repository handoff context.

Implementation and revision-matched execution own actual renderer behavior. README and Architecture explain that behavior; they do not upgrade it.

## Scientific-communication boundaries

Keep these distinctions explicit:

```text
render success != scientific validity
claim binding != entailment
uncertainty metadata != statistical validation
publisher profile/alignment != publisher acceptance
accessibility metadata/support != WCAG certification
backend adapter present != backend available
```

A generated figure can be structurally correct for a declared recipe while the underlying scientific claim, data provenance, uncertainty interpretation, or publication status remains unverified.

## Cross-layer reading

Machine/configuration surfaces such as `metadata/`, `profiles/`, `quality/`, and `recipes/` are routed with the active contracts in class 02 because they constrain supported communication behavior. Their presence does not by itself prove a runtime backend, publication acceptance, or scientific correctness.

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) define figure-claim, communication-transfer, assertion-basis, and research-contract semantics.

Current document taxonomy is routed from [`../README.md`](../README.md). Class 03 maintenance/audit material is operational/historical context and does not own figure validity.

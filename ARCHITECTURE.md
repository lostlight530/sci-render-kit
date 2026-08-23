# 架构设计、科研完整性与可复现边界 / Architecture, Scientific Integrity & Reproducibility Boundaries

> 当前架构校准日期 / Calibration date: 2026-08-23

`sci-render-kit` 是一个**声明式、能力有界、多后端的科学可视化工具包**。它把 recipe、profile、质量门、后端能力和溯源信息分离，使图表生成过程更可检查、更容易重放，也更容易发现不支持的组合。

`sci-render-kit` is a **declarative, capability-bounded, multi-backend scientific visualization toolkit**. It separates recipes, profiles, quality gates, backend capabilities, and provenance so that rendering decisions are inspectable and unsupported combinations remain explicit.

它不承诺“同一 recipe 在所有后端完全等价”，也不把成功渲染描述成科学正确性、期刊接受或独立复现的证明。

---

## 1. 规范数据流 / Canonical data flow

```text
recipe + profile + data
          |
          v
schema validation (P0)
          |
          v
declared visual/accessibility gates (P1)
          |
          v
backend capability resolution
          |
          v
backend render
          |
          v
output / metadata checks (P2/P3)
          |
          v
figure + reproducibility metadata
```

“Declaration First” 的准确含义是：用户可以通过统一 recipe 描述图表意图，而不是每次手写完整后端代码。它**不等于**每种图表、格式、profile、后端组合都可用；组合必须先落在对应 adapter 的声明能力集内。

## 2. 统一入口与能力解析 / Unified dispatcher and capability resolution

`sci_render.py` 负责：

1. 读取 recipe；
2. 使用 `metadata/recipe.schema.yaml` 做结构验证；
3. 读取 profile；
4. 执行 P0/P1 前置门禁；
5. 检查输出格式是否在 `BACKEND_CAPABILITIES` 中；
6. 调用对应 adapter；
7. 对输出执行 P2/P3 检查。

当前声明的输出能力是：

| Backend | Declared output formats |
| --- | --- |
| Matplotlib | PNG, SVG, PDF |
| ggplot2 | PNG, SVG, PDF |
| Observable | HTML |

“Backend agnostic” 因此应理解为**统一声明模型 + 明确 capability negotiation**，而不是后端完全互换或像素级一致。

## 3. Recipe 与 Profile 的责任边界 / Recipe and profile responsibilities

### Recipe

Recipe 表达数据、图表类型、输出意图和部分视觉语义。它是待验证输入，不因为采用 YAML 就自动安全、正确或可发表。

### Profile

Profile 编码仓库选择实现的一部分目标出版约束，例如字体、尺寸或格式规则。它不是目标期刊全部实时规则的权威镜像，也不能代替投稿指南、编辑审查或人工核对。

因此：

```text
profile pass != journal acceptance
profile pass != complete journal compliance
```

## 4. Quality Gates 的严格含义 / Exact meaning of quality gates

质量门只证明**实际执行的谓词**。

### P0 — Schema

验证 recipe 的结构与类型。结构合法不代表数据真实或研究设计正确。

### P1 — Visual and accessibility-oriented checks

包括颜色数量、文字对比、背景对比、语义色板、CVD 模拟和可选邻接色检查等。

#### WCAG 2.2 scope calibration

WCAG 2.2 SC 1.4.11 要求理解内容所必需的非文本图形对象与相邻颜色之间具备足够对比。它不是“所有分类色板任意两色必须 3:1”的通用要求。

本仓 `palette-adjacency` 在启用 `adjacency_check: true` 时执行更严格的**分类色板两两对比**策略。该策略受 SC 1.4.11 / Technique G209 启发，但属于**项目自定义的 stricter safeguard**，不是 WCAG 原文的普遍性要求。

### P2 — Output integrity

检查输出文件、格式和声明的 metadata/provenance 产物是否存在并满足已实现条件。存在文件不代表图中的科学结论正确。

### P3 — Profile-oriented constraints

检查仓库当前编码的目标规范子集，例如某些尺寸、DPI 或矢量格式条件。通过 P3 仍然只是“通过了本仓实现的规则”，不是期刊官方认证。

## 5. Provenance 与 Reproducibility 的区别

旧架构文档使用过“保证 100% 实验可溯源 / reproducibility”一类绝对表述。当前架构明确拆开：

### 5.1 Reproducibility manifest

用于记录 recipe/profile/backend/environment 等渲染上下文。它提高可追踪性与 replay 可寻址性。

### 5.2 Matplotlib provenance path

Matplotlib 后端当前实现了图件 metadata 与同名 `.prov.json` 旁车，其中可记录配方、输入、后端和输出摘要。

### 5.3 不能从 metadata 推导出的结论

```text
manifest exists != independent reproduction
SHA-256 matches != semantic equivalence
render succeeded != scientific validity
timestamp exists != trusted timestamping
```

真正的“已复现”必须发生一次独立重跑并按声明判据比较结果，而不是仅生成一个 metadata 文件。

## 6. 科研完整性规则 / Scientific-integrity rules

视觉系统必须避免通过默认样式暗示不存在的证据：

- 不用视觉编码暗示未被数据支持的显著性；
- 不把相关性画法包装成因果结论；
- 不因置信区间/误差带存在就假定不确定性模型正确；
- 缺失值、聚合、过滤、变换和剔除若影响解释，应在上层研究对象或 manifest 中保留可追踪语义；
- 颜色可访问性是最低保障之一，不能替代文字、标记形状、线型和完整图注等多通道表达。

## 7. 后端卫生与失败语义 / Backend hygiene and failure semantics

Adapter 应保持“dumb”：只负责把已验证 payload 映射为具体后端行为，不偷偷扩张上层语义。

系统必须区分：

- supported and rendered；
- unsupported capability；
- optional runtime missing；
- backend execution failure；
- post-render gate failure。

Skip、fallback 或缺失可选运行时都不能被计作“该后端已验证成功”。不同 Matplotlib/R/JS 版本也不承诺像素级完全一致。

## 8. Research Contract / 科研契约

根目录新增 [RESEARCH_CONTRACT.md](RESEARCH_CONTRACT.md)，用于把本仓与 `auto-doc-engine`、`epistemic-pipeline` 的 artifact/evidence/provenance 语义统一起来。

推荐上游 handoff 至少能够表达：

```text
artifact/source identity
content/data digest
analysis/run reference
uncertainty semantics
provenance reference
validation status
```

本仓输出侧则优先表达 recipe、数据、profile、backend、figure、manifest 与 provenance 的可检查关系。

这仍然是**contract-only interoperability**；三个仓没有因为这份文件就变成运行时强耦合系统。

## 9. RO-Crate 1.3 作为未来互操作目标

RO-Crate 1.3 于 2026-06-22 发布为 Recommendation。它适合未来把 figure、recipe、profile、数据、软件环境和 render action 打包成一个机器可读 Research Object。

当前 `.manifest.json` 与 `.prov.json` **不是 RO-Crate**。本仓状态明确为 `proposed_mapping`。只有实现符合规范的 exporter/validator 并增加可执行测试后，才可升级为 implemented。

## 10. 可复现性分级 / Reproducibility levels

本仓采用项目内部术语：

- `R0 Traceable` — 图件能关联其声明 recipe/profile；
- `R1 Replay-addressable` — 数据/spec/profile/output 标识和摘要以及工具版本足以定位 replay；
- `R2 Environment-bounded` — 同时记录 runtime/backend/dependency 环境；
- `R3 Reproduced` — 已真正执行独立重跑并按声明判据比较。

这些不是外部标准，不能把 manifest 或 `.prov.json` 的存在直接翻译成 `R3`。

## 11. 2026-08-23 外部校准 / Ecosystem calibration

- Matplotlib 当前 stable 最新观察版本为 3.11.1（2026-07-17）。这是一条上游事实，不会自动升级仓库已有测试证据；只有实际运行验证后才能声明对应版本兼容性。
- WCAG 基线仍按 W3C WCAG 2.2 的相关 Success Criteria 解释，并将本仓更严格的 project policy 与标准原义分开。

## 12. 架构 doctrine / Architecture doctrine

1. **能力矩阵高于“后端无关”口号。** 不支持的组合必须显式拒绝。
2. **质量门只证明实际谓词。** 不能从格式检查外推科研正确性。
3. **Profile 不是期刊认证。** 外部规则会变化，必须保留来源与验证日期。
4. **Provenance 不是 reproduction。** 记录生成过程与真正独立重跑是两个层级。
5. **项目严格策略要标明是项目策略。** 不扩大 WCAG 等外部标准的原始范围。
6. **实验模块不能靠文档晋级。** 进入 canonical path 需要代码接线和测试。
7. **跨仓互操作先统一语义，再决定耦合。** artifact/evidence/provenance contract 优先于直接依赖。

## 13. 主要参考 / Primary references

检索日期 / Retrieved: 2026-08-23

- [RO-Crate 1.3 Specification](https://www.researchobject.org/ro-crate/1.3/)
- [FAIR Principle R1.2](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)
- [W3C WCAG 2.2 — Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html)
- [W3C Technique G209](https://www.w3.org/WAI/WCAG22/Techniques/general/G209)
- [Matplotlib release notes](https://matplotlib.org/stable/users/release_notes.html)

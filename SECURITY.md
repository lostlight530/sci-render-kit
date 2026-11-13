# Security Policy

Please report security-sensitive issues privately to the maintainer rather than opening a public issue.

### 双语安全与图形输出边界 / Bilingual security and figure-output boundary

**中文**：以私密渠道报告敏感问题，不在公开 Issue、PR、日志或图表示例中暴露凭据、私人数据和未修复漏洞细节；渲染结果、哈希一致性、版式检查和期刊 profile 仅支持其明确检查范围，不自动证明输入可信、科研结果正确或符合外部出版与无障碍认证

**English**: Report sensitive issues privately, without exposing credentials, personal data or unpatched exploit details in public issues, PRs, logs or figure examples. Rendering outputs, matching digests, layout checks and publisher profiles support only the checks performed; they do not certify source trust, scientific correctness or external publication/accessibility compliance

## Scope

Security reports should concern repository-owned code, automation, rendering or validation logic, workflows, or documentation that could materially mislead users about a security boundary.

Do not include credentials, private data, or exploit details in public issues or pull requests. External runtimes, renderers, publisher targets, and source material retain their own security and trust boundaries.

Passing repository checks is evidence only for the tested revision and declared scope; it is not a general security certification.

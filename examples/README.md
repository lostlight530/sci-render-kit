# sci-render-kit 示例 / Example

本目录包含 sci-render-kit 的配方使用示例。
所有渲染均应通过统一 CLI `sci_render.py` 进行（直接调用后端适配器已废弃，
会直接绕过 P0–P3 质量门）。`--profile` 接收 profile **名称**
（如 `nature`），CLI 自动从 `profiles/` 目录解析。

## 示例命令 / Example Commands

```bash
# 1. 渲染折线图（matplotlib 后端，presentation 配置）
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend matplotlib

# 2. 语义色彩编码演示（语义色板 + palette-contrast 对比度门禁）
python3 sci_render.py recipes/semantic-line-chart.yaml --profile presentation --backend matplotlib

# 3. 交互式 HTML（observable 后端，需 node + npm install）
python3 sci_render.py recipes/line-chart-interactive.yaml --profile presentation --backend observable

# 4. ggplot2 后端（可选，需本机 R 环境）
python3 sci_render.py recipes/line-chart.yaml --profile presentation --backend ggplot2

# 5. 批量渲染所有 PNG 配方
for recipe in recipes/*.yaml; do
  case "$recipe" in
    *interactive*) continue ;;  # html 配方仅 observable 后端支持
  esac
  python3 sci_render.py "$recipe" --profile presentation --backend matplotlib
done
```

## 配方类型 / Recipe Types

| 配方 | 适用场景 | 后端 |
|------|---------|------|
| line-chart | 时间序列趋势 | matplotlib / ggplot2 / observable |
| bar-chart | 分类对比 | matplotlib / ggplot2 / observable |
| scatter-plot | 相关性分析 | matplotlib / ggplot2 / observable |
| heatmap | 矩阵热力图 | matplotlib / ggplot2 / observable |
| boxplot | 分布对比 | matplotlib / ggplot2 / observable |
| histogram | 单变量分布 | matplotlib / ggplot2 / observable |
| semantic-line-chart | 语义色彩编码 | matplotlib / ggplot2 / observable |
| line-chart-interactive | 交互式 HTML 输出 | observable |

注：输出格式受后端能力约束（dispatch 前强制校验）：
matplotlib / ggplot2 支持 `png`/`svg`/`pdf`，observable 支持 `html`。

## 期刊配置 / Journal Profiles

- nature.yaml — Nature 期刊风格（P3 强制矢量输出 PDF/EPS，DPI ≥ 300，版宽 ≤ 7.2in）
- science.yaml — Science 期刊风格（P3 强制矢量输出 PDF/EPS，DPI ≥ 600，版宽 ≤ 6.85in）
- cell.yaml — Cell 期刊风格（P3 强制矢量输出 PDF/EPS，仅 Arial，线图 DPI ≥ 1000）
- ieee.yaml — IEEE 会议论文风格（版宽 ≤ 7.17in，版面高度 ≤ 8.8in）
- presentation.yaml — 演示文稿风格（位图友好，适合快速验证配方）

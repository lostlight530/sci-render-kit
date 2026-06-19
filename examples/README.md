# sci-render-kit 示例 / Example

本目录包含 sci-render-kit 的配方使用示例。

## 示例：折线图配方 / Line Chart Recipe

```bash
# 1. 使用 Nature 期刊配置渲染折线图
python backends/matplotlib_adapter.py render \
  recipes/line-chart.yaml \
  --profile profiles/nature.yaml \
  --output output/line-chart.png

# 2. 使用 ggplot2 后端渲染（R）
Rscript backends/ggplot2_adapter.R render \
  recipes/line-chart.yaml \
  --profile profiles/science.yaml

# 3. 批量渲染所有配方
for recipe in recipes/*.yaml; do
  python backends/matplotlib_adapter.py render "$recipe" --output "output/$(basename $recipe .yaml).png"
done
```

## 配方类型 / Recipe Types

| 配方 | 适用场景 | 后端 |
|------|---------|------|
| line-chart | 时间序列趋势 | matplotlib / ggplot2 / Observable |
| bar-chart | 分类对比 | matplotlib / ggplot2 / Observable |
| scatter-plot | 相关性分析 | matplotlib / ggplot2 / Observable |
| heatmap | 矩阵热力图 | matplotlib / ggplot2 / Observable |

## 期刊配置 / Journal Profiles

- nature.yaml — Nature 期刊风格
- science.yaml — Science 期刊风格
- ieee.yaml — IEEE 会议论文风格
- presentation.yaml — 演示文稿风格

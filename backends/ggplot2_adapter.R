#!/usr/bin/env Rscript
# ggplot2 后端适配器 — 将 YAML 配方渲染为图表
# 依赖：ggplot2, yaml, jsonlite

library(yaml)
library(jsonlite)

load_recipe <- function(path) {
  yaml.load_file(path)
}

load_profile <- function(name) {
  profile_path <- paste0('profiles/', name, '.yaml')
  if (!file.exists(profile_path)) {
    return(list())
  }
  yaml.load_file(profile_path)
}

validate_recipe <- function(recipe) {
  errors <- c()
  required <- c('type', 'data', 'aesthetics')
  for (key in required) {
    if (!key %in% names(recipe)) {
      errors <- c(errors, paste('缺少必需字段:', key))
    }
  }
  if (!'output' %in% names(recipe)) {
    errors <- c(errors, '缺少 output 配置')
  }
  return(errors)
}

generate_r_code <- function(recipe, profile) {
  # 合并配置
  aesthetics <- modifyList(profile$aesthetics %||% list(), recipe$aesthetics)
  
  # 构建 ggplot 代码
  chart_type <- recipe$type
  data <- recipe$data
  
  # 默认色板
  palette <- aesthetics$palette %||% c('#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000')
  
  # 构建数据框
  if (chart_type == 'line-chart') {
    # 长格式数据
    df_lines <- c()
    for (label in names(data)) {
      values <- data[[label]]
      df_lines <- c(df_lines, sprintf(
        'data.frame(x = 1:%d, y = %s, series = "%s")',
        length(values), 
        paste(values, collapse = ', '),
        label
      ))
    }
    df_code <- paste('df <- rbind(', paste(df_lines, collapse = ',\n  '), ')')
    
    plot_code <- sprintf('
%s
library(ggplot2)
p <- ggplot(df, aes(x = x, y = y, color = series)) +
  geom_line(linewidth = 0.8) +
  geom_point(size = 1.5) +
  scale_color_manual(values = %s) +
  theme_minimal() +
  theme(
    legend.position = "bottom",
    legend.title = element_blank(),
    panel.grid.major = element_line(color = "#BBBBBB", linewidth = 0.3),
    panel.grid.minor = element_blank(),
    axis.title = element_text(size = %d),
    axis.text = element_text(size = %d)
  )
', df_code, jsonlite::toJSON(palette), aesthetics$font_size %||% 10, aesthetics$font_size %||% 10 - 2)
  } else {
    plot_code <- paste('# TODO: 实现', chart_type, '的 ggplot2 渲染')
  }
  
  output <- recipe$output
  output_dir <- output$dir %||% 'output'
  output_file <- output$filename %||% 'figure.png'
  
  full_code <- sprintf('
%s
ggsave("%s/%s", plot = p, dpi = %d, width = %f, height = %f, units = "in")
cat(sprintf("已保存: %s/%s\\n", "%s", "%s"))
', plot_code, output_dir, output_file, max(aesthetics$dpi %||% 300, 300), 
     aesthetics$figsize[1] %||% 6, aesthetics$figsize[2] %||% 4,
     output_dir, output_file)
  
  return(full_code)
}

write_manifest <- function(recipe, profile, output_path) {
  manifest <- list(
    generated_at = format(Sys.time(), "%Y-%m-%dT%H:%M:%S"),
    generator = 'sci-render-kit/ggplot2',
    recipe = recipe$id %||% 'unknown',
    profile = profile$name %||% 'default',
    backend = 'ggplot2',
    output = output_path
  )
  manifest_path <- sub('\\.[^.]+$', '.manifest.json', output_path)
  write_json(manifest, manifest_path, auto_unbox = TRUE, pretty = TRUE)
}

render <- function(recipe_path, profile_name = 'nature') {
  recipe <- load_recipe(recipe_path)
  
  # 静态验证
  errors <- validate_recipe(recipe)
  if (length(errors) > 0) {
    cat('❌ 配方验证失败:\n')
    for (e in errors) {
      cat('  -', e, '\n')
    }
    quit(status = 1)
  }
  
  profile <- load_profile(profile_name)
  
  # 生成代码
  code <- generate_r_code(recipe, profile)
  
  output <- recipe$output
  output_dir <- output$dir %||% 'output'
  dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
  
  script_path <- file.path(output_dir, '_generated_render.R')
  writeLines(code, script_path)
  
  cat(sprintf('✅ 已生成渲染脚本: %s\n', script_path))
  cat(sprintf('📋 运行以下命令执行渲染:\n'))
  cat(sprintf('   Rscript %s\n', script_path))
  
  output_path <- file.path(output_dir, output$filename %||% 'figure.png')
  write_manifest(recipe, profile, output_path)
}

# 主入口
args <- commandArgs(trailingOnly = TRUE)
if (length(args) >= 2 && args[1] == 'render') {
  profile <- if (length(args) >= 3) args[3] else 'nature'
  render(args[2], profile)
} else {
  cat('用法: Rscript backends/ggplot2_adapter.R render <recipe.yaml> [profile]\n')
}

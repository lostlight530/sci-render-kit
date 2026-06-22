#!/usr/bin/env Rscript
# ggplot2 后端适配器 — 将 YAML 配方渲染为图表
# 依赖：ggplot2, yaml, jsonlite

library(yaml)
library(jsonlite)
library(digest)


`%||%` <- function(a, b) if (is.null(a)) b else a


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
  aesthetics <- modifyList(profile$aesthetics %||% list(), recipe$aesthetics)
  chart_type <- recipe$type
  data <- recipe$data
  palette <- aesthetics$palette %||% c('#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7', '#000000')
  palette_r <- paste("c(", paste(sprintf('"%s"', palette), collapse=", "), ")", sep="")
  font_size <- aesthetics$font_size %||% 10
  
  df_code <- ""
  plot_code <- ""

  if (chart_type == 'line-chart') {
    df_lines <- c()
    for (label in names(data)) {
      values <- data[[label]]
      df_lines <- c(df_lines, sprintf(
        'data.frame(x = 1:%d, y = c(%s), series = "%s")',
        length(values), 
        paste(values, collapse = ', '),
        label
      ))
    }
    df_code <- paste('df <- do.call(rbind, list(', paste(df_lines, collapse = ',\n  '), '))')
    
    plot_code <- sprintf('
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
', palette_r, font_size, max(1, font_size - 2))

  } else if (chart_type == 'bar-chart') {
    labels <- names(data)
    values <- unlist(unname(data))
    df_code <- sprintf('df <- data.frame(category = c(%s), value = c(%s))\ndf$category <- factor(df$category, levels = c(%s))',
                       paste(sprintf('"%s"', labels), collapse=", "),
                       paste(values, collapse=", "),
                       paste(sprintf('"%s"', labels), collapse=", "))
    plot_code <- sprintf('
library(ggplot2)
p <- ggplot(df, aes(x = category, y = value, fill = category)) +
  geom_bar(stat = "identity", color = "black", linewidth = 0.5, width = 0.6) +
  scale_fill_manual(values = rep(%s, length.out=nrow(df))) +
  theme_minimal() +
  theme(legend.position = "none", axis.title = element_text(size = %d))
', palette_r, font_size)

  } else if (chart_type == 'scatter-plot') {
    df_lines <- c()
    for (label in names(data)) {
      pts <- data[[label]]
      df_lines <- c(df_lines, sprintf(
        'data.frame(x = c(%s), y = c(%s), series = "%s")',
        paste(pts[[1]], collapse = ', '),
        paste(pts[[2]], collapse = ', '),
        label
      ))
    }
    df_code <- paste('df <- do.call(rbind, list(', paste(df_lines, collapse = ',\n  '), '))')
    plot_code <- sprintf('
library(ggplot2)
p <- ggplot(df, aes(x = x, y = y, color = series)) +
  geom_point(size = 3, stroke = 1, shape = 21, fill = "white") +
  scale_color_manual(values = %s) +
  theme_minimal() +
  theme(legend.position = "bottom", axis.title = element_text(size = %d))
', palette_r, font_size)

  } else if (chart_type == 'heatmap') {
    matrix_data <- data$matrix
    row_labels <- data$row_labels %||% paste0("R", 1:length(matrix_data))
    col_labels <- data$col_labels %||% paste0("C", 1:length(matrix_data[[1]]))

    df_lines <- c()
    for (i in 1:length(matrix_data)) {
      for (j in 1:length(matrix_data[[i]])) {
        df_lines <- c(df_lines, sprintf('data.frame(Row="%s", Col="%s", Value=%f)', row_labels[i], col_labels[j], matrix_data[[i]][[j]]))
      }
    }
    df_code <- paste('df <- do.call(rbind, list(', paste(df_lines, collapse = ',\n  '), '))\n',
                     sprintf('df$Row <- factor(df$Row, levels=rev(c(%s)))', paste(sprintf('"%s"', row_labels), collapse=", ")),
                     '\n',
                     sprintf('df$Col <- factor(df$Col, levels=c(%s))', paste(sprintf('"%s"', col_labels), collapse=", "))
                     )

    cmap <- aesthetics$cmap %||% "RdBu"
    plot_code <- sprintf('
library(ggplot2)
p <- ggplot(df, aes(x = Col, y = Row, fill = Value)) +
  geom_tile(color = "white") +
  geom_text(aes(label = sprintf("%%.2f", Value)), color = ifelse(df$Value < 0.5, "white", "black"), size = %d/3) +
  scale_fill_distiller(palette = "RdBu", direction = -1) +
  theme_minimal() +
  theme(axis.title = element_blank(), axis.text = element_text(size = %d))
', font_size, font_size)

  } else if (chart_type == 'boxplot') {
    df_lines <- c()
    for (label in names(data)) {
      values <- data[[label]]
      df_lines <- c(df_lines, sprintf(
        'data.frame(value = c(%s), group = "%s")',
        paste(values, collapse = ', '),
        label
      ))
    }
    df_code <- paste('df <- do.call(rbind, list(', paste(df_lines, collapse = ',\n  '), '))\n',
                     sprintf('df$group <- factor(df$group, levels=c(%s))', paste(sprintf('"%s"', names(data)), collapse=", ")))
    plot_code <- sprintf('
library(ggplot2)
p <- ggplot(df, aes(x = group, y = value, fill = group)) +
  geom_boxplot(alpha=0.7) +
  scale_fill_manual(values = %s) +
  theme_minimal() +
  theme(legend.position = "none", axis.title = element_text(size = %d))
', palette_r, font_size)

  } else if (chart_type == 'histogram') {
    values <- data$values
    bins <- aesthetics$bins %||% 10
    df_code <- sprintf('df <- data.frame(value = c(%s))', paste(values, collapse = ', '))
    color <- if (length(palette) > 0) palette[1] else "#1f77b4"
    plot_code <- sprintf('
library(ggplot2)
p <- ggplot(df, aes(x = value)) +
  geom_histogram(bins = %d, fill = "%s", color = "black", alpha=0.7) +
  theme_minimal() +
  theme(axis.title = element_text(size = %d))
', bins, color, font_size)

  } else {
    plot_code <- paste('# TODO: 实现', chart_type, '的 ggplot2 渲染')
  }
  
  output <- recipe$output
  output_dir <- output$dir %||% 'output'
  output_file <- output$filename %||% 'figure.png'
  
  full_code <- sprintf('
%s
%s
ggsave("%s/%s", plot = p, dpi = %d, width = %f, height = %f, units = "in")
cat("已保存: %s/%s\n")
', df_code, plot_code, output_dir, output_file, max(aesthetics$dpi %||% 300, 300),
     aesthetics$figsize[1] %||% 6, aesthetics$figsize[2] %||% 4,
     output_dir, output_file)
  
  return(full_code)
}
write_manifest <- function(recipe, profile, output_path) {
  chksum <- "none"
  if (file.exists(output_path)) {
    chksum <- paste0("sha256:", digest(output_path, file=TRUE, algo="sha256"))
  }
  manifest <- list(
    generated_at = format(Sys.time(), "%Y-%m-%dT%H:%M:%S"),
    generator = 'sci-render-kit/ggplot2',
    recipe = recipe$id %||% 'unknown',
    profile = profile$name %||% 'default',
    backend = 'ggplot2',
    output = output_path,
    checksum = chksum
  )
  manifest_path <- sub('\\.[^.]+$', '.manifest.json', output_path)
  write_json(manifest, manifest_path, auto_unbox = TRUE, pretty = TRUE)
}

render <- function(recipe_path, profile_name = 'nature') {
  recipe <- load_recipe(recipe_path)
  

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
  system2('Rscript', args=script_path)
  
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

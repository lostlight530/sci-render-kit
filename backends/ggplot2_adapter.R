#!/usr/bin/env Rscript
# ggplot2 backend for declarative scientific figure recipes.
# Dependencies: ggplot2, yaml, jsonlite, digest.
# The backend writes sci-render-kit/render-manifest@2 replay-addressable evidence.

library(yaml)
library(jsonlite)
library(digest)
library(ggplot2)

`%||%` <- function(a, b) if (is.null(a)) b else a
MANIFEST_PROFILE <- "sci-render-kit/render-manifest@2"

load_recipe <- function(path) {
  value <- yaml.load_file(path)
  if (!is.list(value)) stop(paste("recipe root must be a mapping:", path))
  value
}

load_profile <- function(name) {
  profile_path <- paste0("profiles/", name, ".yaml")
  if (!file.exists(profile_path)) return(list())
  value <- yaml.load_file(profile_path)
  if (!is.list(value)) return(list())
  value
}

normalize_for_hash <- function(value) {
  if (is.list(value)) {
    if (!is.null(names(value))) value <- value[sort(names(value))]
    return(lapply(value, normalize_for_hash))
  }
  value
}

canonical_sha256 <- function(value) {
  text <- toJSON(normalize_for_hash(value), auto_unbox=TRUE, null="null", digits=NA, pretty=FALSE)
  paste0("sha256:", digest(text, algo="sha256", serialize=FALSE))
}

file_sha256 <- function(path) {
  if (is.null(path) || !file.exists(path)) return(NULL)
  paste0("sha256:", digest(path, file=TRUE, algo="sha256"))
}

validate_recipe <- function(recipe) {
  errors <- c()
  for (key in c("type", "data", "aesthetics", "output")) {
    if (!key %in% names(recipe)) errors <- c(errors, paste("missing required field:", key))
  }
  errors
}

semantic_palette <- function(labels) {
  semantic_map <- c(
    positive="#009E73", negative="#D55E00", neutral="#56B4E9",
    critical="#D55E00", stable="#0072B2", energetic="#E69F00",
    creative="#CC79A7", attention="#F0E442"
  )
  fallback <- c("#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9", "#F0E442", "#D55E00", "#000000")
  vapply(seq_along(labels), function(i) {
    key <- tolower(labels[i])
    if (key %in% names(semantic_map)) unname(semantic_map[[key]]) else fallback[(i - 1) %% length(fallback) + 1]
  }, character(1))
}

resolve_palette <- function(recipe, aesthetics) {
  data <- recipe$data
  labels <- names(data) %||% character()
  palette <- aesthetics$palette %||% c("#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000")
  if (isTRUE(aesthetics$semantic_palette) && length(labels) > 0 &&
      recipe$type %in% c("line-chart", "bar-chart", "scatter-plot", "boxplot", "histogram")) {
    palette <- semantic_palette(labels)
  }
  palette
}

build_plot <- function(recipe, profile) {
  aesthetics <- modifyList(profile$aesthetics %||% list(), recipe$aesthetics %||% list())
  chart_type <- recipe$type
  data <- recipe$data
  palette <- resolve_palette(recipe, aesthetics)
  font_size <- aesthetics$font_size %||% 10
  p <- NULL

  if (chart_type == "line-chart") {
    frames <- lapply(names(data), function(label) {
      values <- unlist(data[[label]])
      data.frame(x=seq_along(values), y=values, series=label)
    })
    df <- do.call(rbind, frames)
    names(palette) <- names(data)[seq_along(palette)]
    p <- ggplot(df, aes(x=x, y=y, color=series)) +
      geom_line(linewidth=0.8) + geom_point(size=1.5) +
      scale_color_manual(values=palette) + theme_minimal() +
      theme(legend.position="bottom", legend.title=element_blank())

  } else if (chart_type == "bar-chart") {
    labels <- names(data)
    df <- data.frame(category=factor(labels, levels=labels), value=as.numeric(unlist(data)))
    names(palette) <- labels[seq_along(palette)]
    p <- ggplot(df, aes(x=category, y=value, fill=category)) +
      geom_col(color="black", linewidth=0.5, width=0.6) +
      scale_fill_manual(values=palette) + theme_minimal() + theme(legend.position="none")

  } else if (chart_type == "scatter-plot") {
    frames <- lapply(names(data), function(label) {
      pair <- data[[label]]
      if (length(pair) != 2) stop(paste("scatter series must contain x/y pair:", label))
      data.frame(x=unlist(pair[[1]]), y=unlist(pair[[2]]), series=label)
    })
    df <- do.call(rbind, frames)
    names(palette) <- names(data)[seq_along(palette)]
    p <- ggplot(df, aes(x=x, y=y, color=series)) +
      geom_point(size=2.5, stroke=0.6) + scale_color_manual(values=palette) +
      theme_minimal() + theme(legend.position="bottom")

  } else if (chart_type == "heatmap") {
    matrix_data <- data$matrix
    if (is.null(matrix_data) || length(matrix_data) == 0) stop("heatmap matrix must be non-empty")
    row_labels <- data$row_labels %||% paste0("R", seq_along(matrix_data))
    col_labels <- data$col_labels %||% paste0("C", seq_along(matrix_data[[1]]))
    records <- list()
    index <- 1
    for (i in seq_along(matrix_data)) {
      for (j in seq_along(matrix_data[[i]])) {
        records[[index]] <- data.frame(Row=row_labels[i], Col=col_labels[j], Value=matrix_data[[i]][[j]])
        index <- index + 1
      }
    }
    df <- do.call(rbind, records)
    df$Row <- factor(df$Row, levels=rev(row_labels))
    df$Col <- factor(df$Col, levels=col_labels)
    # R backend uses a documented ggplot2 gradient instead of pretending every Matplotlib cmap name exists in R.
    p <- ggplot(df, aes(x=Col, y=Row, fill=Value)) +
      geom_tile(color="white") +
      scale_fill_viridis_c(option="D") +
      theme_minimal() + theme(axis.title=element_blank())

  } else if (chart_type == "boxplot") {
    frames <- lapply(names(data), function(label) {
      data.frame(value=unlist(data[[label]]), group=label)
    })
    df <- do.call(rbind, frames)
    df$group <- factor(df$group, levels=names(data))
    names(palette) <- names(data)[seq_along(palette)]
    p <- ggplot(df, aes(x=group, y=value, fill=group)) +
      geom_boxplot(alpha=0.7) + scale_fill_manual(values=palette) +
      theme_minimal() + theme(legend.position="none")

  } else if (chart_type == "histogram") {
    df <- data.frame(value=unlist(data$values %||% list()))
    bins <- as.integer(aesthetics$bins %||% 10)
    color <- if (length(palette) > 0) palette[1] else "#1f77b4"
    p <- ggplot(df, aes(x=value)) +
      geom_histogram(bins=bins, fill=color, color="black", alpha=0.7) + theme_minimal()

  } else {
    stop(paste("unsupported chart type:", chart_type))
  }

  p <- p + theme(
    axis.title=element_text(size=font_size),
    axis.text=element_text(size=max(1, font_size - 2))
  )
  if (!is.null(aesthetics$title)) p <- p + labs(title=aesthetics$title)
  if (!is.null(aesthetics$x_label)) p <- p + labs(x=aesthetics$x_label)
  if (!is.null(aesthetics$y_label)) p <- p + labs(y=aesthetics$y_label)
  p
}

write_manifest <- function(recipe, profile, recipe_path, profile_name, output_path) {
  profile_path <- paste0("profiles/", profile_name, ".yaml")
  merged_aesthetics <- modifyList(profile$aesthetics %||% list(), recipe$aesthetics %||% list())
  manifest <- list(
    profile=MANIFEST_PROFILE,
    generated_at=format(Sys.time(), "%Y-%m-%dT%H:%M:%OS%z"),
    generator="sci-render-kit",
    recipe=list(
      id=recipe$id %||% "unknown",
      canonical_sha256=canonical_sha256(recipe),
      file_sha256=file_sha256(recipe_path),
      source=recipe_path
    ),
    target_profile=list(
      id=profile$name %||% profile_name,
      canonical_sha256=canonical_sha256(profile),
      file_sha256=file_sha256(profile_path)
    ),
    backend=list(
      name="ggplot2",
      version=as.character(packageVersion("ggplot2")),
      runtime=R.version.string
    ),
    output=output_path,
    output_sha256=file_sha256(output_path),
    parameters=list(
      aesthetics=merged_aesthetics,
      data_canonical_sha256=canonical_sha256(recipe$data %||% list()),
      data_keys=names(recipe$data) %||% list()
    ),
    provenance=list(
      sidecar=NULL,
      accessibility_sidecar=if (!is.null(recipe$accessibility)) sub("\\.[^.]+$", ".a11y.json", basename(output_path)) else NULL,
      figure_evidence_sidecar=NULL
    ),
    reproducibility=list(
      level="R1",
      semantics="Replay-addressable recipe/data/profile/backend/output identity; no independent rerun claimed.",
      independently_rerun=FALSE
    )
  )
  manifest_path <- sub("\\.[^.]+$", ".manifest.json", output_path)
  write_json(manifest, manifest_path, auto_unbox=TRUE, pretty=TRUE, null="null")
}

render <- function(recipe_path, profile_name="nature") {
  recipe <- load_recipe(recipe_path)
  errors <- validate_recipe(recipe)
  if (length(errors) > 0) stop(paste(errors, collapse="; "))
  profile <- load_profile(profile_name)
  aesthetics <- modifyList(profile$aesthetics %||% list(), recipe$aesthetics %||% list())
  p <- build_plot(recipe, profile)

  output <- recipe$output
  output_dir <- output$dir %||% "output"
  output_file <- output$filename %||% "figure.png"
  output_path <- file.path(output_dir, output_file)
  dir.create(output_dir, recursive=TRUE, showWarnings=FALSE)

  figsize <- aesthetics$figsize %||% c(6, 4)
  dpi <- as.integer(aesthetics$dpi %||% 300)
  ggsave(output_path, plot=p, dpi=dpi, width=figsize[[1]], height=figsize[[2]], units="in")
  if (!file.exists(output_path)) stop(paste("render completed without declared output:", output_path))
  cat(sprintf("saved: %s\n", output_path))
  write_manifest(recipe, profile, recipe_path, profile_name, output_path)
}

args <- commandArgs(trailingOnly=TRUE)
if (length(args) >= 2 && args[1] == "render") {
  profile <- "nature"
  flag_idx <- match("--profile", args)
  if (!is.na(flag_idx) && length(args) >= flag_idx + 1) profile <- args[flag_idx + 1]
  else if (length(args) >= 3 && !startsWith(args[3], "--")) profile <- args[3]
  render(args[2], profile)
} else {
  cat("usage: Rscript backends/ggplot2_adapter.R render <recipe.yaml> [--profile <name>]\n")
  quit(status=2)
}

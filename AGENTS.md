# Agent Guide for Customization

Welcome, Agent/Bot! If you are assigned to extend, modify, or customize the `sci-render-kit` repository on behalf of a user, please read this guide. This document explains the architecture, design philosophy, and step-by-step instructions on how to extend the framework.

## 1. The Core Philosophy
- **Declaration First**: Users don't write code to plot; they write YAML (`recipes/*.yaml`).
- **Backend Agnostic**: The same recipe can be rendered in Python (Matplotlib), R (ggplot2), or JS (Observable).
- **Quality Ahead (Gates)**: Before ANY rendering occurs, the recipe is validated statically (`jsonschema` + custom rules) by the CLI.
- **Mandatory Metadata**: A `manifest.json` MUST be generated next to the output for 100% reproducibility.

## 2. System Architecture

The workflow is orchestrated by `sci_render.py` (The CLI).
1. `sci_render.py` loads `recipes/xxx.yaml` and merges it with `profiles/yyy.yaml`.
2. It validates the merged configuration against `metadata/recipe.schema.yaml` (P0) and `quality/gates.yaml` (P1).
3. If validation passes, it dispatches the payload to the corresponding backend adapter (e.g., `backends/matplotlib_adapter.py`).
4. The backend adapter generates code, executes it, produces the image, and writes the `manifest.json`.

**Rule of Thumb:**
- Adapters are DUMB. They do NOT perform validation. They simply take data and aesthetic properties and generate drawing code.
- Validation is SMART and CENTRALIZED in `sci_render.py`.

## 3. How to Customize / Extend

### A. Add a New Chart Type
1. Define the required schema for your new chart in `metadata/recipe.schema.yaml` under `type` enum.
2. Create a demo recipe in `recipes/your-new-chart.yaml`.
3. Implement the generation logic in **ALL** backends:
   - `backends/matplotlib_adapter.py`
   - `backends/ggplot2_adapter.R`
   - `backends/observable_adapter.js`
4. Test it by running: `python3 sci_render.py recipes/your-new-chart.yaml --backend [matplotlib|ggplot2|observable]`

### B. Add a New Quality Gate
1. Add the rule definition to `quality/gates.yaml`.
2. Implement the enforcement logic inside `run_quality_gates` function in `sci_render.py`.

### C. Add a New Backend Adapter (e.g., ECharts, Plotly)
1. Create `backends/yourbackend_adapter.xxx`.
2. Write a script that takes the recipe data, merges aesthetics, generates the specific visualization code, and saves both the image/HTML and the `.manifest.json`.
3. Register your backend inside the `backend_script_map` dict located in `sci_render.py`.

## 4. Constraints & Conventions
- Ensure NO version locking in CDN links unless strictly necessary. (e.g., use `@observablehq/plot` instead of `@observablehq/plot@0.6`).
- Always run the test suite: `python3 tests/test_all.py` before finalizing any change.
- Never bypass the `sci_render.py` CLI workflow. Direct backend invocation is deprecated.

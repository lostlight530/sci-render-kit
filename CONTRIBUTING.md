# Contributing to sci-render-kit

## Getting Started

1. Clone the repository.
2. Create an isolated environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install pyyaml jsonschema matplotlib numpy
   ```
3. (Optional) For the observable (JS) backend, install Node.js dependencies:
   ```bash
   npm install
   ```
   The ggplot2 (R) backend requires a local R installation with the
   `yaml`, `jsonlite`, `digest`, and `ggplot2` packages. Tests that need
   node/R are skipped automatically when the environment lacks them.
4. Run tests to verify baseline:
   ```bash
   make test
   ```

## Development Principles

- **Declaration first**: Users write YAML recipes, not code. New chart types must be expressible as a recipe.
- **Backend agnostic**: New chart types must be implemented in ALL backends (matplotlib, ggplot2, observable). If a backend cannot support a feature, fail gracefully with a TODO comment.
- **Quality ahead**: Recipes are validated statically before rendering. Do not bypass `sci_render.py` CLI workflow.
- **Output hygiene**: Generated render scripts must be cleaned up after execution (see `matplotlib_adapter.py` for the pattern). `ggplot2_adapter.R` follows the same convention.
- **Mandatory metadata**: A `manifest.json` must be generated next to every output for reproducibility.

## Pull Request Checklist

- [ ] All tests pass (`make test`)
- [ ] New chart types have recipes in `recipes/`
- [ ] New chart types implemented in all 3 backends
- [ ] Generated scripts are cleaned up after execution
- [ ] Manifest is written for every output (matplotlib also writes the `.prov.json` provenance sidecar — P2 `prov-exists` gate)
- [ ] R/JS adapters' embedded semantic-color constants stay in parity with `core/color_encoding.py`
- [ ] New modules are marked as `[EXPERIMENTAL]` if not integrated
- [ ] Documentation updated if behavior changes

## License

By contributing, you agree that your contributions are licensed under the MIT License.

.PHONY: test-interoperability test-failure-injection test-render-integration test-observable-offline help clean test test-core test-accessibility test-tools

help:
	@echo "sci-render-kit manual maintenance commands"
	@echo "  make test               optional local contract checks"
	@echo "  make test-core          core/runtime contract file"
	@echo "  make test-accessibility accessibility contract file"
	@echo "  make clean              remove generated local artifacts"
	@echo "These commands are not GitHub merge gates."

clean:
	rm -rf __pycache__ .pytest_cache output/*
	@echo "Cleaned local caches and generated artifacts"

test: test-core test-accessibility test-tools test-tool-ui test-interoperability test-render-integration test-maintenance-scope

test-core:
	python3 tests/test_all.py

test-accessibility:
	python3 -m unittest tests.test_accessibility -v

test-tools:
	python3 -m unittest tests.test_tool_cli tests.test_agent_plan -v

.PHONY: test-tool-ui
test-tool-ui:
	python3 -m unittest tests.test_tool_ui -v

test-interoperability:
	python3 -m unittest tests.test_cross_repo_contract -v

test-render-integration:
	python3 -m unittest tests.test_render_integration -v

# Optional Node dependency validation; install package.json dependencies first
test-observable-offline:
	node tests/test_observable_offline.js

.PHONY: test-maintenance-scope
test-maintenance-scope:
	python3 -m unittest tests.test_maintenance_scan_scope -v

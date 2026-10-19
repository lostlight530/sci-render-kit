.PHONY: help clean test test-core test-accessibility

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

test: test-core test-accessibility test-tool-interface

test-core:
	python3 tests/test_all.py

test-accessibility:
	python3 -m unittest tests.test_accessibility -v

.PHONY: test-tool-interface
test-tool-interface:
	python3 -m unittest tests.test_tool_cli -v

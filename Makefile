.PHONY: clean test test-core test-accessibility

clean:
	rm -rf __pycache__ .pytest_cache output/*
	@echo "🧹 缓存和生成文件已清理"

test: test-core test-accessibility

test-core:
	python3 tests/test_all.py

test-accessibility:
	python3 -m unittest tests.test_accessibility -v

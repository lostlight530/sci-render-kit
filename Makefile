.PHONY: clean test

clean:
	rm -rf __pycache__ .pytest_cache output/*
	@echo "🧹 缓存和生成文件已清理"

test:
	python3 tests/test_all.py

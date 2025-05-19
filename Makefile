.PHONY: format lint typecheck test quality all

format:
	black src
	isort src

lint:
	flake8 src

typecheck:
	mypy src

test:
	python -m pytest src/tests

quality:
	@echo ">> Cyclomatic Complexity (radon cc)"
		radon cc src -a
	@echo "\n>> Maintainability Index (radon mi)"
		radon mi src

all: format lint test

.PHONY: format lint typecheck test all

format:
	black src
	isort src

lint:
	flake8 src

typecheck:
	mypy src

test:
	python -m pytest src/tests

all: format lint test

install:
	uv sync

build:
	uv run ruff check
	uv run ruff format
	uv build

package-install:
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff

lint:
	uv run ruff check

format:
	uv run ruff format

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

test-build:	build package-install
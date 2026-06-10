test:	build package-install
	
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
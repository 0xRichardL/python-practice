.PHONY: sync run test lint format format-check check

sync:
	uv sync --locked

run:
	@test -n "$(FILE)" || (echo "Usage: make run FILE=path/to/main.py" >&2; exit 2)
	uv run --locked python "$(FILE)"

test:
	@if find algorithms concepts problems interviews -type f -name 'test_*.py' -print -quit | grep -q .; then \
		uv run --locked pytest -q; \
	else \
		echo "No tests yet; add test_*.py beside an exercise."; \
	fi

lint:
	uv run --locked ruff check .

format:
	uv run --locked ruff format .

format-check:
	uv run --locked ruff format --check .

check: lint format-check test

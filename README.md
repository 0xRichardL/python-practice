# Python Practice

A personal workspace for learning Python through small concept demos, reusable
algorithms, coding problems, and interview exercises. The directory layout
follows the sibling `nodejs-practice` repository; its solutions and learner
progress are intentionally absent.

## Setup

Requirements: Python 3.14 and [uv](https://docs.astral.sh/uv/). The version in
`.python-version` is the target for this workspace. From the repository root:

```bash
make sync
```

The lockfile pins Ruff and pytest for development. The exercises use the Python
standard library until a lesson calls for another dependency.

## Layout

| Path | Purpose |
| --- | --- |
| `concepts/basics/` | Language, modules, standard library, files, CLI, and errors |
| `concepts/concurrency/` | `asyncio`, threads, processes, subprocesses, and cleanup |
| `algorithms/` | Reusable algorithms with nearby tests |
| `problems/leetcode/` | LeetCode exercises |
| `problems/hackerrank/` | HackerRank exercises |
| `interviews/` | Company and mock interview exercises |

See `FUNDAMENTALS_PRACTICE.md` for the broader learning roadmap and
`INTERVIEWING_CHECKLIST.md` for interview review. The concurrency directory
contains a Python-specific guide and a fresh progress log.

## Conventions

- Name code and learning material files with lowercase snake_case, such as
  `main.py`, `test_main.py`, and `values_and_names.md`. Learning guide and
  progress files keep their paired `<TOPIC>_GUIDE.md` and
  `<TOPIC>_PROGRESS.md` names for the learning skills.
- Put each standalone demo or problem in its own directory with `main.py`.
- Keep reusable functions importable and put `test_*.py` files beside them.
- Use pytest for tests and the standard library for exercise code. Add runtime
  packages for a concrete exercise, then update the lockfile with `uv add`.
- Use `if __name__ == "__main__":` for runnable scripts that may be imported,
  especially multiprocessing examples.
- Avoid copying Node.js solutions; solve each problem in Python.

## Commands

```bash
make run FILE=concepts/basics/<topic>/main.py
make test
make lint
make format-check
make format
make check
```

Run one test file with `uv run --locked pytest
problems/leetcode/<problem>/test_main.py`. `make test` explains when there
are no tests yet. `make check` runs lint, formatting,
and tests; Python does not compile static types the way TypeScript does. Type
annotations are covered in the roadmap; add a type checker when typed modules
make it useful.

Inspect concurrency demos before running them. An exercise may intentionally
block, fail, or leave work running; use a timeout when that behavior is the
lesson.

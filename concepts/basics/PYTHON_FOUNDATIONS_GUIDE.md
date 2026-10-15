# Learning Guide: Level 1 Python Foundations

> Created: 2026-10-09
> Guide version: 1
> Target slug: python-foundations

## Learning contract

| Field | Value |
| --- | --- |
| Desired outcome | Independently write, run, and debug one small Python command-line tool that stores data in JSON. |
| Current level | Novice; start with the interpreter, expressions, and small programs. |
| Success criteria | Explain names and mutation, use branches, loops, functions, and collections, handle a file error, find an answer in the official docs, and finish a JSON task-list CLI with tests for a normal and a failure path. Explain and debug a nearby variation without copying a finished solution. |
| Total active-learning budget | 22 hours over 3 days, at most 8 active hours per day; breaks are additional. |
| Constraints | Use this repository's Python 3.14, `uv`, `make`, and configured pytest. The budget covers a focused subset of Level 1, not every checklist item or the full Foundations-to-Intermediate milestone. |

## Priority and scope

### Must learn

- Run Python in this repository; locate relevant official documentation.
- Use basic values, names, truthiness, mutation, and text formatting.
- Write branches, loops, functions, and basic collection operations.
- Handle specific exceptions; read and write text with an explicit encoding and `with`.
- Use imports, a guarded entry point, CLI arguments, and JSON for one small program.

### Supporting knowledge

- Know that CPython runs Python source and may cache bytecode; no bytecode inspection is needed.
- Recognize floating-point approximation and distinguish `str` from `bytes`.
- Add simple parameter and return annotations; know they do not enforce types at runtime.
- Write a few focused pytest cases for the finished program.

### Deliberately deferred

- The other three Level 1 foundation projects and the milestone of three independent tools: one integrated tool is the outcome for this focused plan.
- `match`, advanced parameter forms (`*args`, `**kwargs`, unpacking), detailed scope rules, sorting stability, and complex comprehensions: revisit after core control flow and functions are fluent.
- Classes, `dataclass`, type aliases, `Any`, and `Callable`: unnecessary for the selected CLI.
- Exception chaining, package layout, detailed import paths, `datetime`, `collections`, and `itertools`: useful next steps after the tool works.
- CPython bytecode details, floating-point internals, and deep lockfile inspection: recognize the concepts now; investigate later if a concrete problem calls for them.

## Roadmap

Each estimate includes a short recall of earlier material, hands-on application, and an end-of-unit review. Resume at any unit ID; use its mastery evidence before moving on.

| ID | Unit | Observable outcome | Key ideas | Practice and mastery evidence | Estimate |
| --- | --- | --- | --- | --- | ---: |
| LG-01 | Run the workspace | Run a script and find a relevant official doc page. | Python 3.14, REPL, `.python-version`, `pyproject.toml`, `uv.lock`, `uv sync --locked`, `make run`, `python -m`. | Try the REPL, run a tiny script, pass one argument, then locate a standard-library function in the docs; repeat the commands from memory. | 1.5 h |
| LG-02 | Values and names | Predict the result of small expressions and assignments. | `None`, `bool`, `int`, `float`, `str`, `bytes`; equality vs identity; aliasing; mutable vs immutable; truthiness, short circuiting, f-strings. | Predict then run 8 short examples, including two names for one list, `0.1 + 0.2`, and `str` versus `bytes`; explain two surprises. | 2.5 h |
| LG-03 | Decisions and repetition | Turn a short written rule into a working loop. | `if`/`elif`/`else`, `for`, `while`, `range`, `break`, `enumerate`; indentation. | Write a number classifier and a loop that reports numbered items; test empty input and a boundary value, then trace one loop by hand. | 2 h |
| LG-04 | Functions | Split a small task into functions with clear inputs and outputs. | `def`, `return`, positional and keyword arguments, defaults, local scope, simple annotations, mutable-default pitfall. | Refactor the classifier into two functions; call with positional and keyword arguments, fix a mutable-default example, and explain each returned value. | 2 h |
| LG-05 | Collections | Choose and update a suitable collection for a task list. | List order, tuple immutability, dict key lookup, set uniqueness, indexing/slicing, iteration, `zip`, simple comprehensions. | Model three tasks as dictionaries in a list; add, find, and mark one done; explain why a set is unsuitable for ordered task records and whether a slice shares nested objects. | 3 h |
| LG-06 | Errors and text files | Read a UTF-8 file and report a specific failure clearly. | `try`/`except`, `else`/`finally` at a recognition level, `with`, `pathlib.Path`, explicit encoding, missing versus malformed input. | Write a tiny text reader; handle a missing file and malformed content separately; confirm the file is closed and errors are not silently swallowed. | 0.5 h |
| LG-07 | Modules, CLI, and JSON | Run a module with arguments and round-trip task data through JSON. | `import`, `__name__ == "__main__"`, `argparse`, `json.load`/`dump`, JSON-compatible values, exit status. | Start `concepts/basics/task_list/main.py` with one `add` command; save and load one task, then run the same program as a script and with `python -m concepts.basics.task_list.main`. | 1.5 h |
| LG-08 | Build one task-list CLI | Build a usable JSON-backed task-list program. | Combine functions, collections, paths, JSON, CLI parsing, and specific errors; keep business logic importable. | Extend LG-07 with `list` and `done`; check persistence, help, and a clear malformed-JSON error; write one normal-path and one failure-path test nearby. | 3 h |
| LG-09 | Recall and debug | Explain and repair the program without a finished solution. | Retrieval, tracing, boundary cases, and documentation lookup. | Explain CLI-to-JSON data flow from memory; check empty list, repeated `done`, and missing file; fix one observed or deliberately introduced bug, then rerun focused tests and `make check`. | 1.5 h |

**Planned total:** 17.5 hours (Day 1: LG-01–LG-04, 8 h; Day 2: LG-05–LG-07, 5 h; Day 3: LG-08–LG-09, 4.5 h). LG-07–LG-09 are focused implementation blocks that reuse earlier work; extend a block if its mastery evidence is not met.

## Milestones

| Milestone | Units | Cumulative time | Evidence |
| --- | --- | ---: | --- |
| Day 1: core syntax | LG-01–LG-04 | 8 h | Run code and explain values, branching, loops, and function calls. |
| Day 2: data boundaries | LG-05–LG-07 | 13 h | Model tasks in collections and round-trip them through a CLI and JSON file. |
| Day 3: independent tool | LG-08–LG-09 | 17.5 h | The task-list CLI works across runs, passes normal and failure tests, and you can explain and debug it. |

## Compact reference

### Run and inspect

- From the repo root: `uv sync --locked`; `uv run --locked python`; `make run FILE=path/to/main.py`; `uv run --locked pytest path/to/test_file.py`.
- `pyproject.toml` states project requirements; `.python-version` selects Python 3.14 here; `uv.lock` records resolved dependencies. Search the official Python docs by module or function name when stuck.

### Predict Python behavior

- A name refers to an object. `==` compares values; `is` checks identity. Mutating a shared list is visible through every alias; rebinding one name is not.
- `and` and `or` short circuit and return an operand. Empty collections, `0`, `""`, and `None` are false in conditions.
- Default argument expressions are evaluated when the function is defined. Use `None` as a sentinel when a new mutable value is needed per call.
- Annotations describe expected types but do not validate input at runtime.

### Keep the CLI dependable

- Parse arguments at the edge, keep task operations in importable functions, and call the CLI only under `if __name__ == "__main__":`.
- Use `with path.open(..., encoding="utf-8")` for text files. JSON stores data, not arbitrary Python objects; handle missing files and malformed JSON explicitly.
- Prefer a specific exception handler and an observable error over `except:` or a silent fallback.

## Sources

1. [Local Level 1 checklist](../../FUNDAMENTALS_PRACTICE.md) — defined the target topics and the original, broader Foundations-to-Intermediate milestone.
2. [Python tutorial](https://docs.python.org/3/tutorial/) — established the order and examples for interpreter use, values, control flow, functions, collections, modules, files, and exceptions. Its introduction assumes some programming experience, so this roadmap starts with smaller practice.
3. [Python virtual environments](https://docs.python.org/3/library/venv.html) — established environment isolation and why a project environment can be recreated.
4. [uv project guide](https://docs.astral.sh/uv/guides/projects/) — established `pyproject.toml`, `uv.lock`, project environments, and `uv run` behavior.
5. [Python `pathlib` reference](https://docs.python.org/3/library/pathlib.html) — established path-based file operations for the tool.
6. [Python `json` reference](https://docs.python.org/3/library/json.html) — established JSON serialization and parsing behavior.
7. [Python `argparse` reference](https://docs.python.org/3/library/argparse.html) — established basic command-line parsing and help output.
8. [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) — established test discovery, assertions, and expected-exception tests.
9. [PCEP entry-level syllabus](https://pythoninstitute.org/pcep-exam-syllabus) — validated prioritizing basic syntax, control flow, collections, functions, and exceptions for an entry-level learner.

## Research limits

- The 17.5-hour plan is an instructional estimate within the 22-hour budget, not a guarantee of mastery; the full Level 1 checklist needs additional practice. Python 3.14 and tool behavior should be checked against the pinned repository files if they change.

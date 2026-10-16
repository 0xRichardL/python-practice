# Learning Guide: Level 1 Python Foundations

> Created: 2026-10-09
> Updated: 2026-10-16
> Guide version: 2
> Target slug: python-foundations

## Learning contract

| Field | Value |
| --- | --- |
| Desired outcome | Independently write, run, and debug one small Python command-line tool that stores data in JSON. |
| Current level | Novice; start with the interpreter, expressions, and small programs. |
| Success criteria | Explain names and mutation; use branches, loops, functions, and collections; handle file errors; and finish a JSON task-list CLI with tests for a normal and a failure path. Explain and debug a nearby variation without copying a finished solution. |
| Total active-learning budget | 22 hours, with at most 8 active hours per study day; breaks are additional. |
| Constraints | Use this repository's Python 3.14, `uv`, `make`, and configured pytest. The original three-day schedule is a planning aid; study may span more days. The budget covers a focused subset of Level 1, not every checklist item or the full Foundations-to-Intermediate milestone. |

## Priority and scope

### Must learn

- Run Python in this repository and use a supplied official reference when needed.
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

Each estimate includes recall of earlier material, hands-on application, and review. Resume at any unit ID; use its mastery evidence before moving on. The [progress file](./PYTHON_FOUNDATIONS_PROGRESS.md) records demonstrated evidence and the next action.

| ID | Unit | Observable outcome | Knowledge to learn | Practice and mastery evidence | Estimate |
| --- | --- | --- | --- | --- | ---: |
| LG-01 | Run the workspace | Run a script and explain how this repository selects Python and dependencies. | Python 3.14 interpreter and REPL; `.python-version`, `pyproject.toml`, `uv.lock`; `uv sync --locked`, `make run`, script arguments, `python -m`; using a supplied official reference. | Run a REPL expression and a script with an argument; run a module with `-m`; explain the three project files and repeat the commands from memory. Use a supplied docs link to answer one concrete API question. | 1.5 h |
| LG-02 | Values and names | Predict the result of small expressions and assignments. | `None`, `bool`, `int`, `float`, `str`, `bytes`; `==` versus `is`; aliasing, mutation versus rebinding; truthiness and short circuiting; f-strings; floating-point approximation. | Predict and run examples covering all six types, shared-list mutation and rebinding, `==`/`is`, false values and `and`/`or`, an f-string, `str` versus `bytes`, and `0.1 + 0.2`; explain the results. | 2.5 h |
| LG-03 | Decisions and repetition | Turn written rules into branches and loops that handle boundaries. | Indented `if`/`elif`/`else`; `for`, `while`, `range`, `enumerate`, `break`. | Write a number classifier and numbered-item loop; use `range`, a `while` loop, and `break` in small variations. Check empty and boundary inputs; trace a loop and explain when it stops. | 2 h |
| LG-04 | Functions | Split a small task into functions with clear inputs and outputs. | `def`, `return` versus `print`, local names, positional and keyword calls, default arguments, simple parameter and return annotations, mutable defaults. | Refactor the classifier into two functions; call them by position and keyword; explain local and returned values and what annotations do at runtime. Show the shared-list default bug across calls, then fix it. | 2 h |
| LG-05 | Collections | Choose and update a suitable collection for a task list. | List order and indexing, tuple immutability, dict lookup and update, set uniqueness; iteration, slicing and shared nested references, `zip`, simple comprehensions. | Store three task dictionaries in a list; index, add, find, and mark one done. Demonstrate tuple and set behavior, slice aliasing, paired iteration with `zip`, and one comprehension; explain each collection choice. | 3 h |
| LG-06 | Errors and text files | Read a UTF-8 file and report specific failures clearly. | `Path.open` with explicit encoding; `with` cleanup; `try`/specific `except`; missing file, invalid UTF-8, malformed integer; `else` and `finally` at recognition level. | Run a text reader on valid, missing, invalid UTF-8, and malformed-integer inputs; name the exception for each failure and show that errors are reported. Explain file closure and when `else` and `finally` run. | 0.5 h |
| LG-07 | Modules, CLI, and JSON | Run an `add` command that persists one task in JSON. | `import`, module guard, script versus `-m` execution; `ArgumentParser`, `add_argument`, `parse_args`, help and error exit status; JSON-compatible task values, `json.load`/`dump`. | Explain import versus entry-point behavior; predict parsed values, run `--help` and a missing-argument case, and explain their exit statuses. Build one guarded `add` command, save and load a task, then run it by file path and with `python -m concepts.basics.task_list.main`. | 1.5 h |
| LG-08 | Build one task-list CLI | Build a usable JSON-backed task-list program. | `add`, `list`, and `done` operations; functions over list/dict data; `Path` and JSON persistence; specific errors; importable logic; pytest assertions and a temporary file. | Extend LG-07 with `list` and `done`; verify data survives separate runs, help works, and malformed JSON gives a clear error without overwriting data. Write one normal-path and one failure-path test against a temporary file. | 3 h |
| LG-09 | Recall and debug | Explain and repair the program without a finished solution. | Retrieval of CLI-to-JSON flow; tracing; empty and repeated-operation boundaries; focused test and `make check` commands; using a supplied reference if needed. | Explain data flow from memory; check empty list, repeated `done`, and missing file; trace and fix one observed or introduced bug. Rerun focused tests and `make check`, and explain any remaining failure. | 1.5 h |

**Planned total:** 17.5 hours (LG-01–LG-04: 8 h; LG-05–LG-07: 5 h; LG-08–LG-09: 4.5 h), leaving 4.5 hours within the 22-hour budget for extra practice where evidence is weak. The original three-day grouping is optional; each study day stays within 8 active hours.

## Milestones

| Milestone | Units | Cumulative time | Evidence |
| --- | --- | ---: | --- |
| Core syntax | LG-01–LG-04 | 8 h | Run code and explain values, branching, loops, and function calls. |
| Data boundaries | LG-05–LG-07 | 13 h | Model tasks in collections and round-trip one task through a CLI and JSON file. |
| Independent tool | LG-08–LG-09 | 17.5 h | The task-list CLI works across runs, passes normal and failure tests, and you can explain and debug it. |

## Compact reference

### Run and inspect

- From the repo root: `uv sync --locked`; `uv run --locked python`; `make run FILE=path/to/main.py`; `uv run --locked pytest path/to/test_file.py`.
- `pyproject.toml` states project requirements; `.python-version` selects Python 3.14 here; `uv.lock` records resolved dependencies. Use the relevant Python 3.14 reference linked below when an API question arises.

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
2. [Python 3.14 tutorial](https://docs.python.org/3.14/tutorial/) — established the sequence and examples for interpreter use, values, control flow, functions, collections, modules, files, and exceptions. It assumes some programming experience, so this roadmap uses smaller practice.
3. [uv project guide](https://docs.astral.sh/uv/guides/projects/) — established `pyproject.toml`, `uv.lock`, project environments, and `uv run` behavior.
4. [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/) — established what `--locked` checks.
5. [Python 3.14 `pathlib` reference](https://docs.python.org/3.14/library/pathlib.html) — established path-based text file operations for the tool.
6. [Python 3.14 `json` reference](https://docs.python.org/3.14/library/json.html) — established JSON serialization, parsing, and malformed-input errors.
7. [Python 3.14 `argparse` reference](https://docs.python.org/3.14/library/argparse.html) — established argument parsing, help output, and error handling.
8. [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html) — established test discovery, assertions, and expected-exception tests.
9. [PCEP entry-level syllabus](https://pythoninstitute.org/pcep-exam-syllabus) — validated prioritizing basic syntax, control flow, collections, functions, and exceptions for an entry-level learner.

## Research limits

- The 17.5-hour plan is an instructional estimate within the 22-hour budget, not a guarantee of mastery; the full Level 1 checklist needs additional practice. Unit estimates are planning values, not reported study time. Check Python and tool behavior against the repository files if they change.

# JSON task-list CLI

## Core model

The CLI translates text arguments into one operation. Each operation loads a
list of task dictionaries from JSON. `add` and `done` change that list and
save it; `list` only reads it. The data file is the boundary between separate
program runs.

| Command | Input | Data change | Save? |
| --- | --- | --- | --- |
| `add TITLE` | A title string | Append `{"title": TITLE, "done": false}` | Yes |
| `list` | None | None | No |
| `done NUMBER` | A one-based task number | Set one task's `done` value to `true` | Yes |

## Parsing commands with different inputs

A required positional `title` makes `list` impossible. With `nargs="?"`, one
positional value is optional and is `None` when absent. Validate what each
command needs after parsing:

```python
parser.add_argument("command", choices=["add", "list", "done"])
parser.add_argument("value", nargs="?", help="title or task number")
args = parser.parse_args()

if args.command in ("add", "done") and args.value is None:
    parser.error(f"{args.command} needs a value")
if args.command == "list" and args.value is not None:
    parser.error("list takes no value")
```

`parser.error()` prints a usage error and exits with status 2. Keep the
existing `if __name__ == "__main__":` guard so imports do not parse arguments.

## Numbering, loading, and errors

Use `enumerate(tasks, start=1)` for displayed numbers. A displayed number `n`
refers to `tasks[n - 1]`. Validate `1 <= n <= len(tasks)` before indexing:
Python also accepts negative indexes, but a user-facing task number should not.

Treat a missing data file as an empty list. Malformed JSON is a different
case: report it and stop before writing, preserving the original file. A JSON
document can also be valid JSON with the wrong shape, such as `{}` instead of
a list; do not assume `json.load()` validates the task schema.

`Path.open(..., encoding="utf-8")` plus `with` keeps text encoding explicit
and closes the file. `json.dump()` writes the task data, and `json.load()`
recreates Python values on a later run.

## Focused verification

Pytest finds functions named `test_*` in files named `test_*.py` and runs them.
An `assert` states the expected result; a false assertion fails the test.
`tmp_path` is a temporary `Path` supplied by pytest, so tests do not touch the
real `tasks.json`:

```python
def test_text_round_trip(tmp_path):
    path = tmp_path / "sample.txt"
    path.write_text("hello", encoding="utf-8")
    assert path.read_text(encoding="utf-8") == "hello"
```

To verify a failure, `with pytest.raises(ValueError):` passes only when the
enclosed operation raises that exception. For the task list, one normal-path
test can add, reload, mark done, and reload again. One failure-path test can
write malformed JSON, assert the operation raises `SystemExit`, and assert
that the original text was not overwritten.

References: [argparse](https://docs.python.org/3.14/library/argparse.html),
[json](https://docs.python.org/3.14/library/json.html),
[pathlib](https://docs.python.org/3.14/library/pathlib.html), and
[pytest `tmp_path`](https://docs.pytest.org/en/stable/how-to/tmp_path.html).

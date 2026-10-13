# LG-01: Run the workspace

Run these commands from the repository root. This unit uses [run_workspace/main.py](./run_workspace/main.py).

## Use the REPL

The REPL (read, evaluate, print loop) runs Python one entry at a time. It is useful for trying an expression or inspecting a value without editing a file.

```bash
uv run --locked python
```

At the `>>>` prompt, type Python code **without** the prompt characters:

```pycon
>>> 2 + 3
5
>>> message = "hello"
>>> message.upper()
'HELLO'
>>> print(message)
hello
>>> for number in range(2):
...     print(number)
...
0
1
>>> import sys
>>> sys.executable
'/path/to/python-practice/.venv/bin/python3'
>>> quit()
```

The REPL displays the value of an expression automatically. Assignment does not display a value; `print()` explicitly writes output. The exact `sys.executable` path depends on your machine. A `...` prompt means Python is waiting for another line of a multi-line statement. On macOS, `Control-D` also exits the REPL. [Python's interpreter tutorial](https://docs.python.org/3.14/tutorial/interpreter.html) covers the prompts and exit behavior.

## Run a file and pass an argument

```bash
make run FILE=concepts/basics/run_workspace/main.py
uv run --locked python concepts/basics/run_workspace/main.py hello
```

The first command prints `Please pass one argument`. The second prints `hello`. The repository's `make run` target runs `uv run --locked python "$(FILE)"`; for an argument after the filename, use the direct `uv run` form above.

In the example, `sys.argv` is a list of command-line strings. `sys.argv[0]` identifies the script; `sys.argv[1]` is `hello`. The `len(sys.argv) > 1` check prevents an `IndexError` when no argument was passed. See the official [`sys.argv` reference](https://docs.python.org/3.14/library/sys.html#sys.argv).

## Run the same file as a module

```bash
uv run --locked python -m concepts.basics.run_workspace.main hello
```

Run this from the repository root. `-m` finds the module by its dotted name and executes it; it does not take a `.py` suffix. The argument remains available as `sys.argv[1]`. For this example, both the file and module commands print `hello`. See [Python's command-line reference](https://docs.python.org/3.14/using/cmdline.html#cmdoption-m).

## Know which Python runs

| File or command | Role in this repository |
| --- | --- |
| `.python-version` | Requests Python 3.14 for uv. |
| `pyproject.toml` | Declares `requires-python = ">=3.14"` and development dependencies. |
| `uv.lock` | Records resolved dependency versions. |
| `make sync` | Runs `uv sync --locked` to prepare the project environment. |
| `uv run --locked ...` | Runs in the project environment and fails if the lockfile is out of date. |

The project environment is normally `.venv`. `uv run` uses it without requiring you to activate it in your shell. Check which interpreter is running:

```bash
uv run --locked python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
```

The first line should point into this project's `.venv`; the second should be `True`. The comparison checks whether the interpreter is in a virtual environment. A bare `python` command can select a different interpreter depending on your shell. See the official [uv Python version](https://docs.astral.sh/uv/concepts/python-versions/#python-version-files), [uv sync](https://docs.astral.sh/uv/concepts/projects/sync/), and [Python virtual environment](https://docs.python.org/3.14/library/venv.html#how-venvs-work) documentation.

## Find an official answer

Search the [Python 3.14 documentation](https://docs.python.org/3.14/) for a module or function name. For example, [`sys.executable`](https://docs.python.org/3.14/library/sys.html#sys.executable) documents the interpreter path printed above. The official docs are the source for Python behavior; this repository's README and Makefile show how this workspace invokes Python.

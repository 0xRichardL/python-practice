# Command-line argument basics

## What the program receives

A command such as `python main.py Ada --upper` consists of the interpreter,
the script, and argument text for that script. The shell passes argument text
to Python. `argparse` names and checks those arguments for us.

- A **positional** argument is identified by its place, such as `Ada`.
- An **option** is identified by a flag, such as `--upper`.
- `parse_args()` returns a namespace with the parsed values.

```python
import argparse

parser = argparse.ArgumentParser(description="Greet one person")
parser.add_argument("name")
parser.add_argument("--upper", action="store_true")
args = parser.parse_args()

message = f"Hello, {args.name}"
print(message.upper() if args.upper else message)
```

Argument text starts as strings. `argparse` can convert or restrict values
when requested, but it does not know our program's business rules by itself.
It generates `--help`; for missing or invalid arguments, it reports an error
and exits with a nonzero status before the remaining program runs.

Try this folder's demo from the repository root:

```sh
make run FILE=concepts/basics/cli_arguments/main.py
uv run --locked python concepts/basics/cli_arguments/main.py Ada
uv run --locked python concepts/basics/cli_arguments/main.py Ada --upper
uv run --locked python concepts/basics/cli_arguments/main.py --help
```

The first command intentionally shows the missing-name error. The later
task-list CLI will use the same idea for commands such as `add`.

Reference after the example: [Python `argparse` documentation](https://docs.python.org/3.14/library/argparse.html).

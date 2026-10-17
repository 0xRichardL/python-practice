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
parser.add_argument("--greeting", choices=["Hello", "Hi"], default="Hello")
args = parser.parse_args()

message = f"{args.greeting}, {args.name}"
print(message.upper() if args.upper else message)
```

`choices` restricts an argument to the listed values. Here `--greeting Hi`
sets `args.greeting` to `"Hi"`; leaving the option out uses the default
`"Hello"`. `--greeting Bye` is rejected by `parse_args()` before the greeting
prints. The same rule works for a positional argument. In the task-list CLI,
`parser.add_argument("command", choices=["add"])` accepts `add` and rejects
any other command. The one-item list is intentional until more commands exist.

Argument text starts as strings. `argparse` can convert or restrict values
when requested, but it does not know our program's business rules by itself.
It generates `--help`; for missing or invalid arguments, it reports an error
and exits before the remaining program runs. Help exits with status `0`;
a missing required argument exits with status `2`. In a shell, `echo $?`
shows the status of the command that just finished.

Try this folder's demo from the repository root:

```sh
make run FILE=concepts/basics/cli_arguments/main.py
uv run --locked python concepts/basics/cli_arguments/main.py Ada
uv run --locked python concepts/basics/cli_arguments/main.py Ada --upper
uv run --locked python concepts/basics/cli_arguments/main.py Ada --greeting Hi
uv run --locked python concepts/basics/cli_arguments/main.py Ada --greeting Bye
uv run --locked python concepts/basics/cli_arguments/main.py --help
```

The first command intentionally shows the missing-name error. The `Hi` command
prints `Hi, Ada`; the `Bye` command reports an invalid choice and exits with
status `2`.

Reference after the example: [Python `argparse` documentation](https://docs.python.org/3.14/library/argparse.html).

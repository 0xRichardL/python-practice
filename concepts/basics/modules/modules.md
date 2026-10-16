# Module basics

## What a module is

A `.py` file such as `main.py` is a module. It groups names—functions,
variables, and imports—so another Python file can use them. Python executes a
module's top-level statements when it imports the module; a normal import does
not rerun that code every time within the same process.

Every module has a `__name__`. When imported, it is the module's import name.
When run as the program's entry point, it is `"__main__"`. Put runnable behavior
under the guard so an import can access functions without starting the program:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


if __name__ == "__main__":
    print(greet("Ada"))
```

`python path/to/main.py` runs a file by path. `python -m package.module` finds
the module by its dotted import name. Both forms make that module the entry
point, so its guard runs. Importing it defines `greet` but does not call it.

Try this folder's demo from the repository root:

```sh
make run FILE=concepts/basics/modules/main.py
uv run --locked python -m concepts.basics.modules.main
uv run --locked python -c 'import concepts.basics.modules.main as example; print(example.module_name())'
```

Reference after the example: [Python `__main__` documentation](https://docs.python.org/3.14/library/__main__.html).

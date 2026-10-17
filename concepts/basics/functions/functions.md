# Functions

## Core model

`def` binds a function to a name. Calling it binds the supplied arguments to its parameters in a new local scope, runs the body, and gives the caller the value from `return`. A function without an executed `return` gives back `None`. `print` displays a value; it does not return that displayed value.

```python
def describe_score(score: int, label: str) -> str:
  message = f"{score}: {label}"
  return message


result = describe_score(80, "strong")
print(result)  # 80: strong
```

Here `score`, `label`, and `message` are local to the call. The caller's `result` receives the returned string. The annotations describe the intended inputs and output; Python does not enforce them at runtime.

## Calling and defaults

```python
def greet(name: str, prefix: str = "Hi") -> str:
  return f"{prefix}, {name}"


greet("Ada")  # positional name; default prefix
greet(name="Ada", prefix="Hello")  # keyword arguments
greet("Ada", prefix="Hello")  # mixed call
```

For ordinary parameters, positional arguments match by order and keyword arguments match by name. A call cannot supply the same parameter twice, use an unknown keyword, or omit a required parameter. Defaults are evaluated when `def` runs, then reused on later calls.

## Mutable-default pitfall

```python
def add_task(task: str, tasks: list[str] | None = None) -> list[str]:
  if tasks is None:
    tasks = []
  tasks.append(task)
  return tasks
```

Using `tasks=[]` as the default would share that same list across calls that omit `tasks`. The `None` default above makes a fresh list for each such call. When a list is passed explicitly, the function mutates that list; every alias sees the change.

## Useful distinctions and edge cases

| Need | Use | Result |
| --- | --- | --- |
| Produce a value for later code | `return value` | Ends the call and gives the value to its caller. |
| Show a value to a person | `print(value)` | Writes output and returns `None`. |

- Code after an executed `return` in the same block does not run.
- A local name is not available outside its call unless the value is returned or otherwise shared.
- Type annotations document expected types but are not runtime validation.
- A function that receives a mutable object can change it in place; rebinding its local parameter alone does not rebind the caller's name.

## Source

- [Python 3.14 tutorial: defining functions](https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions)
- [Python 3.14 tutorial: default values and keyword arguments](https://docs.python.org/3.14/tutorial/controlflow.html#more-on-defining-functions)

# Collections for a task list

## Core model

A collection holds references to objects. A list keeps items in order and can be changed. A tuple keeps its item slots fixed. A dictionary maps unique hashable keys to values. A set keeps unique hashable values and has no task-list position to rely on.

```python
tasks = [{"title": "plan", "done": False}]
first = tasks[0]  # The same dictionary as tasks[0].
copied_list = tasks[:]  # A new outer list, with the same dictionary inside.
first["done"] = True  # Visible through tasks and copied_list.
```

Indexing gets one item; slicing creates a new list. A missing list index raises `IndexError`, and a missing dictionary key raises `KeyError`. Use `in` or `.get()` when missing keys are expected. Changing a dictionary in place is visible through any alias. A shallow list slice does not copy nested dictionaries.

| Need | Collection | Reason |
| --- | --- | --- |
| Keep task records in entry order | `list` of `dict` | The list preserves order; each dictionary holds named fields. |
| Fixed group of values | `tuple` | Its item slots cannot be reassigned. |
| Look up a field in a task | `dict` | Use a key such as `task["title"]`. |
| Track unique labels | `set` | Duplicates collapse; order is not the model. |

Iterate over a list to visit each task. `enumerate(tasks, start=1)` adds display numbers. `zip(names, priorities, strict=True)` pairs items and raises `ValueError` if their lengths differ. Without `strict=True`, `zip` stops when the shorter input ends. A simple comprehension such as `[task["title"] for task in tasks if not task["done"]]` creates a new list from selected tasks.

## Practice

Run the separate examples as needed: `list_type.py`, `tuple_type.py`, `dict_type.py`, and `set_type.py` in this directory. Each is a standalone script with a small `Try` prompt. `list_type.py` includes a task-dictionary append, a search for `"write"`, and a mark-done update. Try an empty list and a missing title in its search example. Explain why a set is unsuitable for ordered task records and why a list slice still shares its dictionaries.

## Source

- [Python 3.14 tutorial: data structures](https://docs.python.org/3.14/tutorial/datastructures.html)

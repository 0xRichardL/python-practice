# Decisions and repetition

## Core model

Python runs a block when its condition is true. Indentation defines the block. An `if`/`elif`/`else` chain chooses the first matching branch, then skips the rest. A loop repeats its indented block: `for` takes successive values from an iterable, while `while` checks its condition before each iteration.

```python
number = 0
if number < 0:
    label = "negative"
elif number == 0:
    label = "zero"
else:
    label = "positive"
```

Order matters: a broad condition placed first can hide a later, more specific one. An empty iterable runs a `for` body zero times. A `while` condition that never becomes false needs an intentional `break` or another exit.

## Choosing a loop

| Need | Direct form |
| --- | --- |
| Visit each item | `for item in items:` |
| Number items while visiting them | `for number, item in enumerate(items, start=1):` |
| Repeat over a known numeric interval | `for number in range(start, stop):` |
| Repeat until a condition changes | `while condition:` |

## How `for` works

```python
for item in ["read", "write"]:
    print(item)
print("finished")
```

The `for` statement asks the iterable for one value at a time. On each pass, `item` is bound to the next value and the indented body runs. After the values run out, execution continues at the first dedented line. With an empty iterable, the body runs zero times. The loop variable holds a value, not an automatic position number.

Lists and strings can be iterated directly; `range(...)` supplies integers for numeric repetition. `enumerate(items, start=1)` supplies `(number, item)` pairs. The two names in `for number, item in ...` unpack each pair.

Rebinding the loop variable does not replace a list element. Avoid changing a list's length while iterating over it, because that can skip or revisit elements. `break` ends the loop immediately and execution continues after it. See `for_loops.py` for runnable examples without conditions inside the loops.

`range` excludes its stop value. `break` exits the nearest enclosing loop immediately. Avoid changing a list's length while iterating over it; the next items can become easy to miss.

### `range()` bounds

`range(stop)` starts at 0. `range(start, stop)` starts at `start`. A third argument sets the step. Each value advances by the step while it stays before `stop` in the step's direction; the stop value itself is never included.

| Expression | Values produced |
| --- | --- |
| `range(4)` | `0, 1, 2, 3` |
| `range(2, 6)` | `2, 3, 4, 5` |
| `range(2, 9, 3)` | `2, 5, 8` |
| `range(5, 0, -2)` | `5, 3, 1` |
| `range(3, 3)` | no values |

A positive step produces values below `stop`; a negative step produces values above it. A step of zero raises `ValueError`. `range` is an immutable sequence object, not a list; `list(range(...))` is useful only when you want to display or store all values. To visit items directly, use `for item in items`; use `enumerate(items, start=1)` when you need item numbers.

```python
for attempt in range(1, 4):  # 1, 2, 3; the stop value 4 is excluded
    print(attempt)

count = 0
while count < 3:  # Check before each repetition.
    count += 1  # Change state so the loop can finish.
    if count == 2:
        break  # Leave this loop immediately.
```

The `while` example reaches `count == 2` and exits; it never reaches 3. A `while` loop whose condition stays true can run forever. When the number of repetitions is already known, `for` with `range` is usually clearer.

For a list, indices start at 0. The condition `index < len(items)` keeps an indexed `while` loop within the list. Increase the index on each pass that continues.

```python
animals = ["cat", "dog", "bird"]
index = 0
while index < len(animals):
    animal = animals[index]
    if animal == "dog":
        print(f"Found at position {index + 1}")
        break
    index += 1
```

This prints `Found at position 2`. With an empty list, the condition is false immediately, so the body never tries to index it. Without a match, the index eventually reaches the list length and the loop finishes.

```python
tasks = ["read", "write"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

An empty `tasks` list prints nothing. If output is required for that case, handle it explicitly.

## Core while-loop patterns

Python checks a while condition before every pass. There are two useful stopping arrangements:

| Arrangement | Example in while_loops.py | Exit |
| --- | --- | --- |
| Check before each pass | Indexed search | The condition becomes false, or a match calls break. The body may run zero times. |
| Decide inside the body | Unconditional loop | The body runs, then an explicit break stops it. The exit must be reachable. |

A counter, flag, sentinel, or collection can supply the changing condition in the first arrangement; they are uses of the same rule. Continue, else, and nested loops alter control flow, but do not create new stopping patterns. Continue retests the condition, else runs only when it becomes false without break, and break exits the nearest loop. When every item should be visited, for is usually clearer.

## Sources

- [Python 3.14 control flow tutorial](https://docs.python.org/3.14/tutorial/controlflow.html)
- [Python 3.14 while statement reference](https://docs.python.org/3.14/reference/compound_stmts.html#the-while-statement)
- [Python 3.14 `enumerate` reference](https://docs.python.org/3.14/library/functions.html#enumerate)

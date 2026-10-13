# Values and names

## Core model

A Python name refers to an object. Every object has an identity, type, and value. Assignment binds or rebinds a name; it does not copy an object. Mutation changes an existing mutable object, so every name that refers to it sees the change.

```python
first = ["read"]
second = first
first.append("write")  # Both names see ["read", "write"].
first = ["new"]  # Only first now refers to the new list.
```

`==` asks whether values compare equal. `is` asks whether two references point to the same object. Use `is None` to check for the unique `None` object. Do not use `is` for numeric or string value comparisons: implementations may reuse immutable objects.

| Operation | What changes? | Seen through an alias? |
| --- | --- | --- |
| `a = new_value` | The binding of `a` | No |
| `a.append(value)` | The list object | Yes |
| `a == b` | Compares values | Not applicable |
| `a is b` | Compares identity | Not applicable |

## Basic values

`None` means no value; `bool` holds `True` or `False`; `int` represents whole numbers; `float` represents approximate binary floating-point numbers; `str` is Unicode text; `bytes` is a sequence of byte values. These types are immutable. Lists and dictionaries are mutable.

```python
0.1 + 0.2 == 0.3  # False: decimal fractions can be approximate
"café".encode("utf-8")  # b'caf\xc3\xa9'
b"caf\xc3\xa9".decode("utf-8")  # 'café'
```

For display, an f-string inserts a formatted value: `f"Count: {count}"`. It produces a `str`, not `bytes`.

## Conditions and short circuiting

`None`, `False`, numeric zero, and empty strings or collections are false in conditions. Most other objects are true. `and` and `or` stop once the result is known and return an operand, not necessarily a `bool`.

```python
items = []
label = items and items[0]  # []: right side is not evaluated
name = "" or "anonymous"  # 'anonymous'
```

Check `is None` when zero or an empty value has a different meaning from missing data. Use parentheses or simple expressions when combining conditions.

## Sources

- [Python data model](https://docs.python.org/3.14/reference/datamodel.html)
- [Built-in types and truth value testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)
- [Floating-point arithmetic](https://docs.python.org/3.14/tutorial/floatingpoint.html)

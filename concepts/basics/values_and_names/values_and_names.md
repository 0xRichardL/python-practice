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

Run the focused scripts in this directory with `make run FILE=concepts/basics/values_and_names/<file>.py`. Each runs directly without an import guard.

| Type | Demo | Important boundary or failure case |
| --- | --- | --- |
| `NoneType` | `none_type.py` | Only `None` means absent. It is false, but so are zero and empty text. A function without `return` and many mutating methods return `None`. Ordering it with an integer raises `TypeError`. |
| `bool` | `bool_type.py` | Nonempty text such as `"False"` is true. `bool` is an `int` subtype, so `True == 1` and the two can collide as dictionary keys. `and` and `or` return operands and short circuit. |
| `int` | `int_type.py` | Integers have arbitrary precision. `int(float)` truncates toward zero; `//` floors, including for negatives. Bad conversion raises `ValueError`; division by zero raises `ZeroDivisionError`. |
| `float` | `float_type.py` | Binary floats approximate many decimal fractions. Use an appropriate `math.isclose` tolerance; near zero may need `abs_tol`. NaN is unequal even to itself; infinities and signed zero need care. Division by zero raises an exception. |
| `str` | `str_type.py` | Text is Unicode and immutable. Length counts code points, so visually identical text may have different sequences; normalize when that distinction matters. An invalid index raises `IndexError`, while an out-of-range slice is empty. Default `split()` collapses whitespace, while an explicit separator retains empty fields; `join()` requires strings. |
| `bytes` | `bytes_type.py` | Bytes are immutable integers from 0 to 255. Encoded byte length can differ from text length. Indexing gives an `int`; slicing gives `bytes`. Decode with the right encoding; malformed input raises `UnicodeDecodeError`, while an incompatible encoding raises `UnicodeEncodeError`. `str(raw_bytes)` is not decoding. |

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

- [Python built-in constants (`None`)](https://docs.python.org/3.14/library/constants.html)
- [Python data model](https://docs.python.org/3.14/reference/datamodel.html)
- [Built-in types and truth value testing](https://docs.python.org/3.14/library/stdtypes.html#truth-value-testing)
- [Floating-point arithmetic](https://docs.python.org/3.14/tutorial/floatingpoint.html)

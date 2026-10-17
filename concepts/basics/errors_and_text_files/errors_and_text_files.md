# Errors and text files

## Core model

- `Path.open("r", encoding="utf-8")` opens a file for text reading and decodes its bytes as UTF-8. A missing path raises `FileNotFoundError`; invalid UTF-8 raises `UnicodeDecodeError` while reading.
- `with` calls the file's cleanup method on exit, even when reading or parsing raises an exception. After the block, the file is closed.
- `int(text)` raises `ValueError` when the decoded text is not a valid integer. That is a content failure, distinct from a missing file.
- A matching `except` handles an exception raised in its `try` block. An unmatched exception propagates. Avoid `except:` or returning a plausible value after an error.

## Small example

```python
from pathlib import Path

path = Path("number.txt")
try:
  with path.open("r", encoding="utf-8") as file:
    number = int(file.read().strip())
except FileNotFoundError:
  print(f"Missing file: {path}")
except ValueError:
  print(f"Expected one integer in: {path}")
else:
  print(number)
```

`else` runs only when the `try` block succeeds. `finally` runs on both success and failure; it is useful for cleanup that is not already managed by `with`. The file closes before either `except` or `else` runs.

## Failure boundaries

| Input | Result |
| --- | --- |
| `42` | `int` returns `42` |
| `hello` or an empty file | `ValueError` while parsing |
| Missing path | `FileNotFoundError` while opening |
| Invalid UTF-8 bytes | `UnicodeDecodeError` while decoding; report separately if the program needs a friendly message for this case |

Handle errors where the program can report them meaningfully. Keep the reader's success result an `int`; let unexpected failures remain visible.

## References

- [Python 3.14 exceptions tutorial](https://docs.python.org/3.14/tutorial/errors.html)
- [Python 3.14 `Path.open`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.open)

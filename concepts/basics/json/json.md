# JSON basics

## What JSON is

JSON is a text format for storing and exchanging data. A Python list or
dictionary exists in memory only while the program runs. Converting it to JSON
text lets another run of the program read the data back.

JSON has arrays, objects, strings, numbers, Booleans, and `null`:

```json
[{"title": "plan", "done": false}]
```

The nearest Python value is `[{"title": "plan", "done": False}]`. JSON uses
`true`, `false`, and `null` where Python uses `True`, `False`, and `None`. JSON
strings and object keys use double quotes. JSON does not allow comments or
trailing commas.

## Two directions

**Encode (serialize):** Python value → JSON text.
**Decode (deserialize):** JSON text → a new Python value.

| Working with | Encode | Decode |
| --- | --- | --- |
| A `str` in memory | `json.dumps(value)` | `json.loads(text)` |
| An open text file | `json.dump(value, file)` | `json.load(file)` |

The `s` suffix means **string**. `dump` and `load` work with a file object;
`dumps` and `loads` work with a `str`.

```python
import json

tasks = [{"title": "plan", "done": False}]
text = json.dumps(tasks)
restored = json.loads(text)
assert restored == tasks
assert restored is not tasks
```

To persist data, open a text file with UTF-8 encoding and use `json.dump` or
`json.load`. `with` closes the file after the block:

```python
with path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)

with path.open("r", encoding="utf-8") as file:
    loaded_tasks = json.load(file)
```

`"w"` creates or replaces the file; `"r"` reads an existing file. Saving a
modified task list requires loading it first, changing the Python value, then
writing the whole list back.

## Common failures

- Missing file when reading: `FileNotFoundError`.
- Empty or malformed JSON text: `json.JSONDecodeError`.
- Unsupported Python value such as a `set` when encoding: `TypeError`.

Reference after the examples: [Python `json` documentation](https://docs.python.org/3.14/library/json.html).

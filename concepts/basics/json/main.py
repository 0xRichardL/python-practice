"""Demonstrate JSON text conversion and a file round trip."""

import json
from pathlib import Path


def json_str() -> None:
  print("Case 1: JSON <-> string:")
  tasks = [{"title": "plan", "done": False}]

  text = json.dumps(tasks, indent=2)
  print("JSON text:")
  print(text)

  restored = json.loads(text)
  print("Decoded Python value:", restored)
  print("Equal value, separate object:", restored == tasks, restored is not tasks)


def json_file() -> None:
  print("\nCase 2: JSON <-> file:")
  tasks = []
  path = Path(__file__).with_name("example_tasks.json")

  try:
    with path.open("r", encoding="utf-8") as file:
      tasks = json.load(file)
  except FileNotFoundError:
    print("File not found, skipped.")
  except json.JSONDecodeError:
    print("Failed to decode file's JSON.")
    return
  else:
    print("Loaded from file:", tasks)

  tasks.append({"title": "write", "done": False})

  with path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)


if __name__ == "__main__":
  json_str()
  json_file()

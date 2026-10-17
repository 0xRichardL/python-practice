import argparse
import json
from pathlib import Path


def _load_tasks(path: Path):
  tasks = []
  try:
    with path.open("r", encoding="utf-8") as file:
      tasks = json.load(file)
  except FileNotFoundError:
    print("Data file not found; start fresh.")
  except json.JSONDecodeError:
    raise SystemExit("Failed to decode file's JSON.") from None

  return tasks


def _persist_tasks(path: Path, tasks: list):
  with path.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)


def add_task(path: Path, title: str):
  tasks = _load_tasks(path)
  tasks.append({"title": title, "done": False})
  _persist_tasks(path, tasks)


def list_tasks(path: Path):
  tasks = _load_tasks(path)
  for i, task in enumerate(tasks, start=1):
    print(f"Task: {i}", json.dumps(task, indent=2))


def done_task(path: Path, number: int):
  tasks = _load_tasks(path)
  if not 1 <= number <= len(tasks):
    raise ValueError("task number is out of range.")
  tasks[number - 1]["done"] = True
  _persist_tasks(path, tasks)


def main() -> None:
  path = Path(__file__).with_name("tasks.json")
  parser = argparse.ArgumentParser(description="Add task")
  parser.add_argument(
    "command", choices=["add", "list", "done"], help="Operations to perform"
  )
  parser.add_argument("value", nargs="?")
  args = parser.parse_args()

  command = args.command

  if command in ("add", "done") and args.value is None:
    parser.error(f"{command} command needs a value")
  if command == "list" and args.value is not None:
    parser.error("list takes no value")

  value = args.value

  if command == "add":
    if not isinstance(value, str):
      parser.error("title is missing")
    add_task(path, value)

  if command == "list":
    list_tasks(path)

  if command == "done":
    if not isinstance(value, str):
      parser.error("number is missing")
    try:
      number = int(value)
    except ValueError:
      parser.error(f"invalid task number {value!r}: expected an integer")

    try:
      done_task(path, number)
    except ValueError as error:
      parser.error(str(error))


if __name__ == "__main__":
  main()

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


def main() -> None:
  path = Path(__file__).with_name("tasks.json")
  parser = argparse.ArgumentParser(description="Add task")
  parser.add_argument("command", choices=["add"], help="Operations to perform")
  parser.add_argument("title", help="Title of the new task")

  args = parser.parse_args()
  if args.command == "add":
    add_task(path, args.title)


if __name__ == "__main__":
  main()

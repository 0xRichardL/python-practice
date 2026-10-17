import json

import main
import pytest


def test_done_task_raises_out_of_range_number(tmp_path):
  path = tmp_path / "tasks.json"
  main.add_task(path, "T1")
  origin = json.loads(path.read_text(encoding="utf-8"))
  with pytest.raises(ValueError):
    main.done_task(path, 0)
  with pytest.raises(ValueError):
    main.done_task(path, 3)
  assert json.loads(path.read_text(encoding="utf-8")) == origin


def test_done_task_persists_only_selected_task(tmp_path):
  path = tmp_path / "tasks.json"

  main.add_task(path, "T1")
  main.add_task(path, "T2")
  main.done_task(path, 2)

  saved = json.loads(path.read_text(encoding="utf-8"))
  assert saved == [
    {"title": "T1", "done": False},
    {"title": "T2", "done": True},
  ]


def test_malformed_json_does_not_overwrite_file(tmp_path):
  path = tmp_path / "tasks.json"
  bad_json = "[{invalid"
  path.write_text(bad_json, encoding="utf-8")

  with pytest.raises(SystemExit):
    main.add_task(path, "T2")

  assert path.read_text(encoding="utf-8") == bad_json

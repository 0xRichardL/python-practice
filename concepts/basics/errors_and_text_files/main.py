from pathlib import Path


def read_number(path: Path) -> int:
  with path.open("r", encoding="utf-8") as file:
    return int(file.read().strip())


if __name__ == "__main__":
  directory = Path(__file__).parent
  for name in ("number.txt", "missing.txt", "bad_number.txt"):
    path = directory / name
    try:
      print(f"{name}: {read_number(path)}")
    except FileNotFoundError:
      print(f"Missing file: {path}")
    except UnicodeDecodeError:
      print(f"Cannot decode file: {path}")
    except ValueError:
      print(f"Expected one integer in: {path}")

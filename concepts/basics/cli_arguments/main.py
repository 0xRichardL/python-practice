"""Demonstrate a positional argument, a flag, and restricted choices."""

import argparse


def main() -> None:
  parser = argparse.ArgumentParser(description="Greet one person")
  parser.add_argument("name")
  parser.add_argument("--upper", action="store_true")
  parser.add_argument("--greeting", choices=["Hello", "Hi"], default="Hello")
  args = parser.parse_args()

  message = f"{args.greeting}, {args.name}"
  print(message.upper() if args.upper else message)


if __name__ == "__main__":
  main()

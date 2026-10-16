"""Demonstrate one positional argument and one optional flag."""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Greet one person")
    parser.add_argument("name")
    parser.add_argument("--upper", action="store_true")
    args = parser.parse_args()

    message = f"Hello, {args.name}"
    print(message.upper() if args.upper else message)


if __name__ == "__main__":
    main()

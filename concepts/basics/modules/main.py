"""Show how a module's name changes when run or imported."""


def module_name() -> str:
    return __name__


def main() -> None:
    print("This module's name:", module_name())


if __name__ == "__main__":
    main()

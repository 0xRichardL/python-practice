# This default list is created once, so calls that omit items share it.
def remember_with_shared_default(
    item: str,
    items: list[str] = [],  # noqa: B006 - intentional example
) -> list[str]:
    items.append(item)
    return items


shared_first = remember_with_shared_default("read")
shared_second = remember_with_shared_default("write")

print("Shared default list:")
print(f"{shared_first=}")
print(f"{shared_second=}")
print(f"same list: {shared_first is shared_second}")


def remember_with_fresh_list(item: str, items: list[str] | None = None) -> list[str]:
    # None means no list was supplied; create one for this call.
    if items is None:
        items = []
    items.append(item)
    return items


fresh_first = remember_with_fresh_list("read")
fresh_second = remember_with_fresh_list("write")

print("Fresh list per call:")
print(f"{fresh_first=}")
print(f"{fresh_second=}")
print(f"same list: {fresh_first is fresh_second}")

supplied = ["plan"]
returned = remember_with_fresh_list("write", supplied)
print(f"supplied list: {supplied}")
print(f"returned the supplied list: {returned is supplied}")

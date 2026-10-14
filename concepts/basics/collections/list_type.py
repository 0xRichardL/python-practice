"""List order, indexing, slicing, iteration, and shallow copies."""

names = ["plan", "write", "review"]
print("first and last:", names[0], names[-1])
print("first two:", names[:2])

names.append("test")
print("\nafter append:", names)
print("numbered:", list(enumerate(names, start=1)))
print("long names:", [name for name in names if len(name) > 4])

priorities = [2, 1, 3, 2]
print("\npaired:", list(zip(names, priorities, strict=True)))

tasks = [{"title": "plan", "done": False}]
copied = tasks[:]
copied[0]["done"] = True
print("\nnew outer list:", copied is not tasks)
print("shared inner dictionary:", tasks[0])

copied.append({"title": "write", "done": False})
print("task keeps it own list:", tasks)
print("only copied list changed:", copied)

# Search task dictionaries by title, then update the matching object.
search_tasks = [
    {"title": "plan", "done": False},
    {"title": "write", "done": False},
    {"title": "review", "done": True},
]
found = False
for task in search_tasks:
    if task["title"] == "write":
        found = True
        task["done"] = True
        break

print("after search and update:", search_tasks)
if not found:
    print("not found")

unfinished = [task["title"] for task in search_tasks if not task["done"]]

print("unfinished tasks:", unfinished)

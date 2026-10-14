"""Dictionary fields, key lookup, updates, and missing keys."""

task = {"title": "plan", "done": False}
print("title:", task["title"])
task["done"] = True
task["priority"] = 2
print("updated task:", task)

print("optional field:", task.get("owner"))
print("optional field with default:", task.get("owner", "unassigned"))

try:
    print(task["owner"])
except KeyError as error:
    print("missing key:", type(error).__name__)

task["owner"] = "Richard"
print("Key lookup and get are the same value:", task["owner"] == task.get("owner"))

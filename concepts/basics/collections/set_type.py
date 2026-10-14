"""A set stores unique hashable values for membership checks."""

labels = {"work", "home"}
print("unique labels:", labels)
print("contains work:", "work" in labels)
labels.add("work")
print("size after adding work again:", len(labels))
labels.add("urgent")
print("after add:", labels)

try:
    labels.add({"title": "plan", "done": False})
except TypeError as error:
    print("dictionary cannot be a set item:", type(error).__name__)

labels.add("home")
print("size after adding home doesn't change:", len(labels))

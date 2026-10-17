"""A tuple has fixed item slots, even when an item is mutable."""

pair = ("plan", 2)
print("pair:", pair)
print("first item:", pair[0])

try:
  pair[0] = "write"
except TypeError as error:
  print("cannot replace a tuple item:", type(error).__name__)

with_list = (["plan"], 2)
with_list[0].append("write")
print("mutable item inside tuple:", with_list)

try:
  with_list[0] = ["write"]
except TypeError as error:
  print("cannot replace a tuple item:", type(error).__name__)

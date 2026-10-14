"""None means a value is absent, not zero or empty."""

missing = None
zero = 0
empty_text = ""
false_value = False

# None is the sole NoneType object. Identity checks distinguish it from other values.
print("\nCase 01: identity and type")
print("  type:", type(missing).__name__)
print("  None is None:", missing is None)
print("  zero is None:", zero is None)
print("  empty text is None:", empty_text is None)

# All three values are false in conditions, but they have different meanings.
print("\nCase 02: truthiness and equality")
print("  bool(None):", bool(missing))
print("  bool(0):", bool(zero))
print("  bool(''):", bool(empty_text))
print("  None == 0:", missing == zero)
print("  None == False:", missing == false_value)


def no_explicit_return():
    # Reaching the end of a function is equivalent to returning None.
    pass


print("\nCase 03: implicit return")
print("  function result is None:", no_explicit_return() is None)

items = ["read"]
# append changes the existing list and returns None, not the changed list.
append_result = items.append("write")
print("\nCase 04: a mutating method's return value")
print("  list after append:", items)
print("  append result:", append_result)

# These try/except blocks let the demo report an expected error and continue.
print("\nCase 05: unsupported ordering")
try:
    comparison = missing < zero
except TypeError as error:
    print("  None < 0 raises:", type(error).__name__)

# Try: replace `missing` with 0. Which printed checks change?

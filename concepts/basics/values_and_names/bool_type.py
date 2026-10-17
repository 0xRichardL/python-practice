"""Booleans, truthiness, and short-circuit operators."""

yes = True
no = False
one = 1
empty_text = ""
fallback = "fallback"
empty_list = []

# bool(x) asks whether x is truthy; nonempty text is true regardless of its words.
print("\nCase 01: Boolean values and truthiness")
print("  True type:", type(yes).__name__)
print("  False type:", type(no).__name__)
print("  bool(None):", bool(None))
print("  bool(0):", bool(0))
print("  bool(0.0):", bool(0.0))
print("  bool(''):", bool(""))
print("  bool([]):", bool([]))
print("  bool('False'):", bool("False"))

# bool subclasses int. Equal keys such as True and 1 refer to one dictionary entry.
keys = {yes: "yes", one: "one"}
print("\nCase 02: Boolean and integer overlap")
print("  isinstance(True, int):", isinstance(yes, int))
print("  True == 1:", yes == one)
print("  True + True:", yes + yes)
print("  dictionary key count:", len(keys))
print("  dictionary value at True:", keys[yes])

# and/or return one of their inputs; they do not force a bool result.
print("\nCase 03: and/or return operands")
print("  '' or 'fallback':", empty_text or fallback)
print("  [] and ['unused']:", empty_list and ["unused"])


def would_fail():
  raise RuntimeError("This function should not run")


# The right side is skipped once the left side determines the result.
print("\nCase 04: short circuit")
print("  False and would_fail():", no and would_fail())
print("  True or would_fail():", yes or would_fail())

# Unlike and/or, not always produces exactly True or False.
print("\nCase 05: not returns bool")
print("  not 'hello':", not "hello")

# Try: replace False with True in the first short-circuit example.

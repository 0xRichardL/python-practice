"""Integers, conversion, division, and boundary cases."""

whole = 12
# int has arbitrary precision; base 2 and decimal text both convert to int.
print("\nCase 01: integer values and conversion")
print("  type of 12:", type(whole).__name__)
print("  1_000_000:", 1_000_000)
print("  2**100:", 2**100)
print("  int('-12'):", int("-12"))
print("  int('  +12  '):", int("  +12  "))
print("  int('101', 2):", int("101", 2))
print("  int(-3.9):", int(-3.9))

# / produces float. // floors toward negative infinity, not toward zero.
print("\nCase 02: true division and floor division")
print("  5 / 2:", 5 / 2)
print("  type of 5 / 2:", type(5 / 2).__name__)
print("  4 / 2:", 4 / 2)
print("  type of 4 / 2:", type(4 / 2).__name__)
print("  5 // 2:", 5 // 2)
print("  -5 // 2:", -5 // 2)
print("  int(-5 / 2):", int(-5 / 2))

# For integers, a == b * (a // b) + (a % b), including negative a or b.
print("\nCase 03: remainders")
print("  5 % 2:", 5 % 2)
print("  -5 % 2:", -5 % 2)
print("  5 % -2:", 5 % -2)
print("  2 * (-5 // 2) + (-5 % 2):", 2 * (-5 // 2) + (-5 % 2))

# int() accepts whole-number text, but not a decimal point in text.
print("\nCase 04: zero and invalid integer text")
print("  bool(0):", bool(0))

try:
  int("12.5")
except ValueError as error:
  print("  int('12.5') raises:", type(error).__name__)

# The expected exception is caught so the rest of this script remains runnable.
print("\nCase 05: division by zero")
try:
  numerator = 5
  denominator = 0
  result = numerator // denominator
except ZeroDivisionError as error:
  print("  5 // 0 raises:", type(error).__name__)

# Try: change -5 // 2 to -5 // 3 and compare it with int(-5 / 3).

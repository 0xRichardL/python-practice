"""Floating-point approximation and special values."""

import math

# Many decimal fractions are approximations in binary floating point.
sum_value = 0.1 + 0.2
print("\nCase 01: approximation and tolerance")
print("  0.1 + 0.2:", repr(sum_value))
print("  equals 0.3:", sum_value == 0.3)
print("  math.isclose to 0.3:", math.isclose(sum_value, 0.3))
# Relative tolerance scales with the compared values; near zero, choose abs_tol.
print("  1e-12 close to zero by default:", math.isclose(1e-12, 0.0))
print("  with abs_tol=1e-9:", math.isclose(1e-12, 0.0, abs_tol=1e-9))

# This interpreter's float cannot distinguish all adjacent large integers.
large_integer = 2**53
print("\nCase 02: rounding and precision limits")
# An exact halfway value rounds to the nearest even integer.
print("  round(2.5):", round(2.5))
print("  round(3.5):", round(3.5))
print("  adjacent large integers become the same float:")
print("   ", float(large_integer) == float(large_integer + 1))

positive_infinity = float("inf")
not_a_number = float("nan")
same_nan = not_a_number
# NaN fails equality even with itself; use math.isnan or math.isfinite.
print("\nCase 03: infinity and NaN")
print("  infinity:", positive_infinity)
print("  math.isinf(infinity):", math.isinf(positive_infinity))
print("  math.isfinite(infinity):", math.isfinite(positive_infinity))
print("  NaN equals itself:", not_a_number == same_nan)
print("  math.isnan(NaN):", math.isnan(not_a_number))
print("  bool(NaN):", bool(not_a_number))
print("  math.isfinite(NaN):", math.isfinite(not_a_number))

# Positive and negative zero compare equal, though their sign bits differ.
print("\nCase 04: signed zero")
print("  0.0 == -0.0:", 0.0 == -0.0)
print("  sign of 0.0:", math.copysign(1.0, 0.0))
print("  sign of -0.0:", math.copysign(1.0, -0.0))

# Python raises for division by zero and text that is not a float literal.
print("\nCase 05: invalid operations and input")
try:
    numerator = 1.0
    denominator = 0.0
    result = numerator / denominator
except ZeroDivisionError as error:
    print("  1.0 / 0.0 raises:", type(error).__name__)

try:
    float("not a number")
except ValueError as error:
    print("  invalid float text raises:", type(error).__name__)

# Try: compare 0.1 + 0.2 with 0.3 using a chosen abs_tol in math.isclose.

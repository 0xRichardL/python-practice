"""Unicode text, indexing, immutability, and formatting."""

import unicodedata

# str is immutable Unicode text; indexing gives a one-code-point str.
text = "café"
print("\nCase 01: text, indexing, slicing, and truthiness")
print("  text:", repr(text))
print("  type:", type(text).__name__)
print("  first character:", text[0])
print("  last character:", text[-1])
print("  first two characters:", text[:2])
# A slice beyond the end is empty; a single index beyond the end raises later.
print("  out-of-range slice:", repr(text[99:]))
print("  bool(''):", bool(""))
print("  bool('0'):", bool("0"))
print("  bool(' '):", bool(" "))

spaced = "  hello  "
spaced_words = " a  b "
csv_text = "a,,b"
parts = ["a", "b"]
# Default split collapses whitespace; an explicit comma retains empty fields.
print("\nCase 02: text helpers and formatting")
print("  strip ends:", repr(spaced.strip()))
print("  split with comma:", csv_text.split(","))
print("  split on whitespace:", spaced_words.split())
print("  join strings:", ",".join(parts))
print("  f-string with padding:", f"{7:03d}")

composed = "é"
decomposed = "e\u0301"
# These look alike but contain different Unicode code point sequences.
print("\nCase 03: Unicode code points")
print("  composed length:", len(composed))
print("  decomposed length:", len(decomposed))
print("  equal before normalization:", composed == decomposed)
print(
  "  equal after NFC normalization:",
  composed == unicodedata.normalize("NFC", decomposed),
)
print("  casefold match:", "Straße".casefold() == "STRASSE".casefold())
print("  escaped newline shown with repr:", repr("a\nb"))

# The expected errors are caught to keep the demonstration running.
print("\nCase 04: immutable text and incompatible types")
try:
  text[0] = "C"
except TypeError as error:
  print("  assigning text[0] raises:", type(error).__name__)

try:
  text + 1
except TypeError as error:
  print("  text + 1 raises:", type(error).__name__)

# join can combine only str items; convert non-text values first if needed.
print("\nCase 05: indexing and join failures")
try:
  text[99]
except IndexError as error:
  print("  text[99] raises:", type(error).__name__)

try:
  mixed_parts = ["a", 1]
  ",".join(mixed_parts)
except TypeError as error:
  print("  join with an int raises:", type(error).__name__)

# Try: compare `str(1) + text` with `f"{1}{text}"`.

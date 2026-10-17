"""Encoded bytes, indexing, decoding, and invalid input."""

text = "café"
# UTF-8 encodes one non-ASCII character using more than one byte.
encoded = text.encode("utf-8")
print("\nCase 01: encode and decode")
print("  text:", repr(text))
print("  encoded bytes:", repr(encoded))
print("  encoded type:", type(encoded).__name__)
print("  text code points:", len(text))
print("  UTF-8 byte count:", len(encoded))
print("  decoded text:", repr(encoded.decode("utf-8")))

# Indexing gives an integer 0..255; slicing preserves the bytes type.
print("\nCase 02: indexing and byte values")
print("  first byte:", encoded[0])
print("  first byte type:", type(encoded[0]).__name__)
print("  first-byte slice:", repr(encoded[:1]))
print("  bytes from [0, 65, 255]:", repr(bytes([0, 65, 255])))
print("  bytes(3):", repr(bytes(3)))

# str(encoded) shows a representation; decode() reconstructs text.
print("\nCase 03: truthiness and text mismatch")
print("  bool(b''):", bool(b""))
print("  bytes equal text:", encoded == text)
print("  str(encoded):", str(encoded))

# Strict decoding reports invalid UTF-8. Replacement continues but loses data.
print("\nCase 04: decoding failure and replacement")
try:
  b"\xff".decode("utf-8")
except UnicodeDecodeError as error:
  print("  invalid UTF-8 raises:", type(error).__name__)
print(
  "  decoding with errors='replace':",
  b"\xff".decode("utf-8", errors="replace"),
)

# bytes cannot be mixed with str directly or changed in place.
print("\nCase 05: incompatible types and values")
try:
  encoded + "!"
except TypeError as error:
  print("  bytes + str raises:", type(error).__name__)

try:
  encoded[0] = 65
except TypeError as error:
  print("  changing encoded[0] raises:", type(error).__name__)

try:
  bytes([256])
except ValueError as error:
  print("  bytes([256]) raises:", type(error).__name__)

# ASCII cannot encode é; UTF-8 can.
print("\nCase 06: encoding failure")
try:
  text.encode("ascii")
except UnicodeEncodeError as error:
  print("  encoding café as ASCII raises:", type(error).__name__)

# Try: decode b"\xff" with errors="replace". What information is lost?
# A bytes literal may contain ASCII characters or escapes, but not literal "é".

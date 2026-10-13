items = ["read", "write", "test"]

# A plain for loop binds each value to the target name in turn.
print("1. Direct list iteration:")
for item in items:
    print(item)

# Strings are iterable too: this visits one character at a time.
print("\n2. String iteration:")
for letter in "Py":
    print(letter)

# Use range when the loop needs a sequence of integers.
print("\n3. Numeric repetition:")
for number in range(1, 4):
    print(number)

# enumerate pairs each item with a number.
print("\n4. Numbered items:")
for number, item in enumerate(items, start=1):
    print(f"{number}. {item}")

# An empty iterable skips the body; execution continues after the loop.
print("\n5. Empty iterable:")
for item in []:
    print(item)  # This line does not run.
print("After the empty loop")

# break ends the loop immediately, so later items are not visited.
print("\n6. Break:")
for item in items:
    print(item)
    break
print("After the break")

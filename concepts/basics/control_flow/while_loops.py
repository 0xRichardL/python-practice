"""Two core stopping patterns for while loops."""

# Check a changing condition before each pass; the body may run zero times.
print("1. Check before each pass:")
guesses = [2, 5, 7, 9]
target = 5
index = 0
while index < len(guesses):
  if guesses[index] == target:
    print(f"Matched at attempt {index + 1} with value: {guesses[index]}")
    break
  index += 1

# Enter the body, then decide when to stop with break.
print("\n2. Stop inside the body:")
attempt = 0
while True:
  attempt += 1
  print(f"Attempt {attempt}")
  if attempt == 2:
    break

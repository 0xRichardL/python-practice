# Change the range arguments in each case to produce the target list.
# list(...) is used here only to display the numbers from each range.

# Case 1: range(stop). Target: [0, 1, 2, 3, 4]
print("1. Stop only:", list(range(5)))

# Case 2: range(start, stop). Target: [3, 4, 5, 6]
print("2. Start and stop:", list(range(3, 7)))

# Case 3: positive step. Target: [1, 4, 7, 10]
print("3. Positive step:", list(range(1, 11, 3)))

# Case 4: negative step. Target: [10, 7, 4, 1]
print("4. Negative step:", list(range(10, 0, -3)))

# Case 5: empty range. Target: []
print("5. Empty range:", list(range(3, 3)))

# Case 6: Produce one attempt number for each guess, starting at 1.
# These are positions, not the guess values. The result must adjust if the
# number of guesses changes: four guesses -> [1, 2, 3, 4], one -> [1], none -> [].
guesses = [2, 5, 7, 9]
print("6. Attempt numbers:", list(range(1, len(guesses) + 1)))

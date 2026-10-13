score = 101

# Replace this placeholder with an if/elif/else chain that classifies score.
# Scores outside 0–100 are invalid. The other labels are "needs work",
# "pass", and "strong" at the boundaries in the lesson.
label = "unclassified"

if score < 0:
    label = "invalid"
elif score < 60:
    label = "needs work"
elif score < 80:
    label = "pass"
elif score <= 100:
    label = "strong"
else:
    label = "invalid"

print(f"{score}: {label}")

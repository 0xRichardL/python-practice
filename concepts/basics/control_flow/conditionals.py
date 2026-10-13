score = 80


def get_label(score: int) -> str:
    if score < 0:
        return "invalid"
    elif score < 60:
        return "needs work"
    elif score < 80:
        return "pass"
    elif score <= 100:
        return "strong"
    else:
        return "invalid"


def describe(score: int, label: str) -> str:
    return f"{score}: {label}"


print(describe(score, get_label(score)))

# Same function call but the order of keyword arguments is changed.
print(describe(label=get_label(score), score=score))

print(describe(score, label=get_label(score)))

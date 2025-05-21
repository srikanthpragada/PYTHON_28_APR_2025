
def has_upper(s: str) -> bool:
    for c in s:
        if c.isupper():
            return True

    return False


def count_digits(s: str) -> int:
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


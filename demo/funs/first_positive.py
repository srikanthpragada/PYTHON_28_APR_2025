# Return first positive number from the list, if not found return -1
def first_positive(lst):
    for v in lst:
        if v >= 0:
            return v

    return -1


print(first_positive([ -10, -20, 5, -30, 10]))
print(first_positive([ -10, -20, -30]))


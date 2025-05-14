def find_upper(st):
    for idx, c in enumerate(st):
        if c.isupper():
            return idx

    return -1


print(find_upper('abDEf'))
print(find_upper('abc'))

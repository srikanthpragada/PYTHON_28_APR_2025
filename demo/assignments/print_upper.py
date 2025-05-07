st = "How Do You Do"

for c in st:
    code = ord(c)
    if 65 <= code <= 90:
        print(c)

for c in st:
    if c >= 'A' and c <= 'Z':
        print(c)

for c in st:
    if c.isupper():
        print(c)
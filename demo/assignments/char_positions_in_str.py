st = "how do you do"

chars = {}

for idx,c in enumerate(st):
    positions = chars.get(c, [])
    positions.append(idx)
    chars[c] = positions

print(chars)



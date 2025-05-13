st = "how are you"

chars = {}

for c in set(st):
    chars[c] = st.find(c)


print(chars)

st = "how are you"

chars = {c: st.count(c) for c in set(st)}
print(chars)

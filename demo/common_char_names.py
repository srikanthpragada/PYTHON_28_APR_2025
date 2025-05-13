
names  = ["abcd", "def", "cbd", "adef"]

chars = set(names[0])
for name in names[1:]:
    chars = chars & set(name)

print(sorted(chars))



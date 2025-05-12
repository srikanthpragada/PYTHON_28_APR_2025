
names  = ['Python', 'C#', 'Java', 'JavaScript', 'SQL']

chars = set()
for name in names:
    chars = chars | set(name)

print(sorted(chars))



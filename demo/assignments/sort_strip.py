names = ["Abc", " xy", "  ade", "Pqr"]

for name in sorted(names):
    print(name)

for name in sorted(names, key=str.strip):   # key = lambda n : n.strip()
    print(name)

for name in sorted(names, key=lambda n: n.lower().strip()):
    print(name)

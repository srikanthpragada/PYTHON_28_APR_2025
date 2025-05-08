names = []

while True:
    name = input("Enter name [end to stop] ")
    if name == "end":
        break
    names.append(name)

print(names[::-1])

for name in names[::-1]:
    print(name)

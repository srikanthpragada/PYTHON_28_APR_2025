names = []

while True:
    name = input("Enter name [end to stop] : ")
    if name == "end":
        break
    if name not in names:
        names.append(name)

print(names[::-1])

for name in names[::-1]:
    print(name)

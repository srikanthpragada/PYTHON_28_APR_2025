names = []

while True:
    name = input("Enter name [end to stop] : ")
    if name == "end":
        break

    # check whether name is already present
    for n in names:
        if n.upper() == name.upper():
            print("Duplicate Name!")
            break
    else:
        names.append(name)


for name in names[::-1]:
    print(name)

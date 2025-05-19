def firstletter(name):
    return name[0]

names = ["Andy", "Jack", "Larry", "Belinda", "Arnold"]

# print("".join( map(firstletter, names) ))

print("".join( map(lambda n : n[0], names) ))
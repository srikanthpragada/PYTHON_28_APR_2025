
names = ['Jack', "Scott", "Larry", "Marshall", "Richards"]

with open("names.txt", "wt") as f:
    for n in names:
        f.write(n + "\n")





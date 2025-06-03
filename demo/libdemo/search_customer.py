name = input("Enter name :")

f = open("customers.txt", "rt")

while True:
    line = f.readline()
    if line == "":   # EOF
        print("Sorry! Name Not Found!")
        break

    parts = line.split(",")
    if parts[0] == name:  # found name
        print("Mobile : ", parts[1])
        break

f.close()

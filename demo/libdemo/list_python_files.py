import os

start = r"c:\classroom\python\demo"
g = os.walk(start)
count = 0
for (dirname, folders, files) in g:
    for f in files:
        if f.endswith(".py"):
            print( dirname + "\\" + f)
            count += 1

print("Count = ", count)


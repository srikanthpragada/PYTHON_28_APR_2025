
with  open("students.txt", "rt") as f:
    for line in f.readlines():
        parts = line.split(",")
        if len(parts) < 2:
            continue

        name = parts[0]
        marks = parts[1:]

        total = sum(map(int, marks))
        print(f"{name:20} {total:3}")




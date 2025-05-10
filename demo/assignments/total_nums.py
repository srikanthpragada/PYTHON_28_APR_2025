data = "10,88,15 ,a, 30,40"

parts = data.split(",")
print(parts)

total = 0
for n in parts:
    if n.strip().isdigit():
        total += int(n)

print(total)

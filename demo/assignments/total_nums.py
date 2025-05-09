data = "90,88,75,a, 34,45"

parts = data.split(",")
print(parts)

total = 0
for n in parts:
    total += int(n)

print(total)




# Check whether number is perfect

num = int(input("Enter a number :"))

total = 1
for n in range(2, num // 2  + 1):
    if num % n == 0:
        total += n

print(total)

if total == num:
    print("Perfect")
else:
    print("Not perfect")

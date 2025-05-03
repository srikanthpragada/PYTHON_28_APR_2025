# Print even numbers from 1 to the given number

num = int(input("Enter a number :"))

for n in range(1, num + 1):
    if n % 2 == 0:
        print(n)

for n in range(2, num + 1, 2):
    print(n)

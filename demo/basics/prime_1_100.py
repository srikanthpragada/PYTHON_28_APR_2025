# Program to print all prime numbers from 5 to 100

for num in range(5, 100, 2):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            break
    else:
        print(num, end =  ' ')



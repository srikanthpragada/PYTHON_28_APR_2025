# Perfect numbers from 1 to 999

for n in range(1, 1000):
    total = 1
    for i in range(2, n//2 + 1):
        if n % i == 0:
            total += i  # add factor

    if total == n:
        print(n, end = ' ')


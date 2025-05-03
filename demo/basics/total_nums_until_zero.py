total = 0

while True:    # infinite loop
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num > 0:
        total += num

print(f'Total = {total}')



total = 0

for i in range(10):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break   # terminate loop
    total += num    # total = total + num


print(f'Total = {total}')


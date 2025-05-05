total = count = 0

while True:    # infinite loop
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if num < 0:
        continue

    total += num
    count += 1

print(f'Total = {total}, Average = {total/count}')



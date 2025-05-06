# Find out largest of all positive and negative numbers

largest = None
while True:
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break

    if largest is None:  # first number
        largest = num
    elif num > largest:
        largest = num

print('Largest = ', largest)

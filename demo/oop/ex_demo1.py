#

st = input("Enter a number :")
try:
    n = int(st)
    print(100 / n)
except ValueError:
    print("Sorry! Invalid Number!")
except ZeroDivisionError:
    print("Sorry! Number cannot be zero!")

print('The End')

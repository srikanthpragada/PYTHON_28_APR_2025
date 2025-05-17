
def iseven(num):
    return num % 2 == 0


nums = [10, 11, 15, 20, 25, 33]

for n in filter(iseven, nums):
    print(n)

# for n in filter(print, nums):
#     print(n)
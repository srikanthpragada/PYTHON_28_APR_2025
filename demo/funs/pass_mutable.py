
def increment(num):
    print(id(num))
    num += 1
    print(id(num))


a = 100
print(id(a))
increment(a)
print(a)



a = 10
b = a

print(id(a), id(b))

def fun():
    print("Hello")

fun2 = fun

print(id(fun), id(fun2))
fun()
fun2()



g = 100  # global variable


def f1():
    print('f1')
    a = 1

    def f2():
        print('f2')
        nonlocal a
        a = 10
        b = 2
        print(g, a, b)  # enclosing variable & local variable

    f2()
    print(a)


f1()

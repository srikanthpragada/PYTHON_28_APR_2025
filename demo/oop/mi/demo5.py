class A:
    def process(self):
        print("Process in A")


class B(A):
    pass


class C(A):
    def process(self):
        print("Process in C")


class D(C, B):
    pass


obj = D()
obj.process()

print(D.mro())


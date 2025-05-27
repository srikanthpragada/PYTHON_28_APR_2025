class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f"{self.length} X {self.width}"

    def __eq__(self, other):
        # print('__eq__')
        return self.length == other.length and self.width == other.width

    def __gt__(self, other):
        a1 = self.length * self.width
        a2 = other.length * other.width
        return a1 > a2

    def __add__(self, other):
        return Rectangle(self.length + other.length, self.width + other.width)


r1 = Rectangle(10, 20)
r2 = Rectangle(10, 20)
r3 = Rectangle(10, 30)
print(r1)
print(str(r1))
print(r1.__str__())
print(r1 == r2)  # r1.__eq__(r2)
print(r1 != r2)
print(r3 > r1)
print(r1 + r2)

#print(r1 * 2)

rects = [r1, r2, r3, Rectangle(40, 20)]

for r in sorted(rects):
    print(r)

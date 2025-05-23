class Counter:
    def __init__(self, start=0):
        # Object attribute
        self.value = start

    # Method
    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value


# create an object of Counter
c = Counter(100)
c.increment()
c.increment()
c.decrement()
print(c.getvalue())

c2 = Counter(start = 10)
c2.decrement()
print(c2.getvalue())


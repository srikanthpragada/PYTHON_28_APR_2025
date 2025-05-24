class Counter:
    def __init__(self, start=0):
        # Object attribute
        self.value = start
        self.start = start

    # Method
    def increment(self, step = 1):
        self.value += step

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.start


# create an object of Counter
c = Counter(100)
c.increment(10)
c.increment()
c.decrement()
print(c.getvalue())

c2 = Counter(start = 10)
c2.decrement()
print(c2.getvalue())


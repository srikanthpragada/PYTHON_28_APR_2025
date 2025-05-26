class Course:
    taxrate = 18

    @staticmethod
    def settaxrate(newrate):
        Course.taxrate = newrate

    def __init__(self, title, duration, fee = -1):
        self.title = title
        self.duration = duration
        self.fee = fee if fee >= 0 else duration * 200

    def show(self):
        print('Title    : ', self.title)
        print('Duration : ', self.duration)
        print('Fee      : ', self.fee)

    def getnetfee(self):
        return self.fee + self.fee * Course.taxrate /  100

c = Course("Generative AI", 18, 10000)
print(c.getnetfee())
Course.settaxrate(12)
print(c.getnetfee())


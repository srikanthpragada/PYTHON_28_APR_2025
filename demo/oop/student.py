class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print(self.name)
        print(self.email)


class Student(Person):
    def __init__(self, name, email, course):
        super().__init__(name, email)
        self.course = course

    # Overriding
    def show(self):
        super().show()
        print(self.course)

s = Student("Richards", "richards@gmail.com", "MSCS")
s.show()



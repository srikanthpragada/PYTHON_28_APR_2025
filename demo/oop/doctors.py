from abc import abstractmethod, ABC


# Abstract class
class Doctor(ABC):
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, mobile, salary):
        super().__init__(name, mobile)
        self.salary = salary

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, mobile, visits, charge):
        super().__init__(name, mobile)
        self.visits = visits
        self.charge = charge

    def getsalary(self):
        return self.visits * self.charge


r = ResidentDoctor("Dr. Jack", "393943943", 400000)
c = Consultant("Dr. Kim", "3934934343", 10, 2000)

print(r.getsalary())
print(c.getsalary())

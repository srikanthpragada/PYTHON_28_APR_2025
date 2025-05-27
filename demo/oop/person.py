class Person:
    def __init__(self, name, email):
        self.name = name
        self.__email = email  # private attribute


    @property
    def fullname(self):
        return self.name

    def getemail(self):
        return self.__email

    def setemail(self, newemail):
        self.__email = newemail


p = Person("James", "james@microsoft.com")
print(p.fullname)  # Use Property

#print(p.__email)
print(p.getemail())
print(p.__dict__)

print(p._Person__email)





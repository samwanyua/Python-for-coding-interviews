# Property decorators -  used to define methods in a class that behave like attributes
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        # self.email = (first + '.' + last + '@gmail.com').lower()
        self.pay = pay
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com".lower()

    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    def __str__(self):
        return f"Meet {self.first} {self.last}, he earns {self.pay}. Contact:  {self.email}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted')
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith", 345000)
print(emp_1.__str__())
emp_1.first = "Jim"
print(emp_1.__str__())
print(emp_1.fullname)

emp_1.fullname = "Barrack Obama"
print(emp_1.fullname)
print(emp_1.__str__())

del emp_1.fullname

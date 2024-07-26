# Property decorators
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = (first + '.' + last + '@gmail.com').lower()
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    def __str__(self):
        return f"Meet {self.first} {self.last}, he earns {self.pay}. Contact:  {self.email}"


emp_1 = Employee("John", "Smith", 345000)
print(emp_1.__str__())

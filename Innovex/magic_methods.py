class Employee:
    raise_amount = 1.04  # class attribute
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


employee_1 = Employee("Sam", "Tim", 30000)
employee_2 = Employee("Rey", "Yatch", 37000)

print(employee_1.fullname())
print(employee_2.pay)
employee_2.apply_raise()
print(employee_2.pay)

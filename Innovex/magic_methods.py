# Special methods/magic/dunder methods
"""
- are predefined methods that you can define in your classes
 to provide specific behavior to instances of those classes.

- surrounded by underscores ex. `__init__`, `__str__`
- they allow you to emulate built-in types, implement operator overloading,
and provide additional functionality
"""


class Employee:
    raise_amount = 1.04  # class attribute

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = (first + '.' + last + '@gmail.com').lower()
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # `__repr__` is used to unambiguously represent objects - used for debugging and logging
    def __repr__(self):
        return f"Employee({self.first} {self.last} {self.pay})"

    # `__str__` is used for readable representation of objects, meant for enduser
    def __str__(self):
        return f"{self.email}  {self.pay}"

    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())


employee_1 = Employee("Sam", "Tim", 30000)
employee_2 = Employee("Rey", "John", 37000)

print(employee_1.fullname())
print(employee_2.pay)
employee_2.apply_raise()
print(employee_2.pay)
# print(employee_2)

print(repr(employee_2))
print(str(employee_1))
# alternatively
print(employee_2.__str__())
print(employee_1.__repr__())

# other dunder methods
print(int.__add__(453, 234))
print(str.__add__('sam', 'hopper'))

print(employee_2 + employee_1)
# checking length using a dunder method
print([34, 23, 43, 32, 54, 54, 34, 23, 43, 43, 65, 5, 443, 345, 34].__len__())
print(len(employee_2))  # same as print(employee_2.__len__()

# Object - instance of a class
# Class - blueprint for creating objects
# instance - is an individual object created from a class

class Dog:
    # self param - is a reference to current instance of a  class.
    # Used to access and modify instance attributes and methods
    def __init__(self, name, age):  # it is automatically called when a new instance of a class is created.
        self.name = name  # this is an attribute
        self.age = age
        print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def add(self, x):
        return x + 100

    def bark(self):
        print("bark")


d = Dog("Will", 24)  # instantiating - creating new instance of a class
print(type(d))
d.bark()  # bark
print(d.add(45))
print(d.name)
print(d.get_name())
print(d.get_age())


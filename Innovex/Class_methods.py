# Class methods and attributes
'''
Class attributes - attributes shared by all instances of a class
Defined inside a class but outside any instance methods
Instance attributes - are unique to each object created from the class
Class attributes are the same for all instances

Instance methods:
    - bound to the instance of the class,
    - 'self' calls the method
    - can access/modify instance attributes
    - called on an instance

Class methods:
    - bound to the class itself
    - 'cls' class itself
    - can access/modify class attributes
    - called on the class or an instance
'''


class Person:
    number_of_people = 0  # class attribute

    def __init__(self, name):
        self.name = name


person1 = Person("Sam")
person2 = Person("Jim")

Person.number_of_people = 89  # accessing and modifying a class attribute
print(Person.number_of_people)


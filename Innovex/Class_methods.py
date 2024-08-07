# Class methods and attributes
'''
Class attributes - attributes shared by all instances of a class
Defined inside a class but outside any instance methods
Instance attributes - are unique to each object created from the class
class attributes are the same for all instances

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
    number_of_people = 0  # class attribute - specific to the class
    GRAVITY = -9.8  # CONSTANTS
    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()

    @classmethod
    def number_of_persons(cls):
        return cls.number_of_people
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


person1 = Person("Sam")
person2 = Person("Jim")
print(Person.number_of_persons())

# Person.number_of_people = 89  # accessing and modifying a class attribute
# print(Person.number_of_people)
# print(person1.number_of_people)




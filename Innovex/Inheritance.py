# Inheritance
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old")

    def sound(self):
        print("I don't know what I speak")
class Cat(Pet):
    def sound(self):
        print("Meow!")


class Dog(Pet):
    def sound(self):
        print("Barks!")


class Fish(Pet):
    pass

pet = Pet("Tim", 32)
pet.show()

cat = Cat("Mews", 4)
cat.show()
cat.sound()

dog = Dog("Rot", 23)
dog.show()
dog.sound()

fish = Fish("Salmon", 3)
fish.sound()

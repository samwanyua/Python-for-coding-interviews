# Inheritance
class Pet:  # parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, and I am {self.age} years old")

    def sound(self):
        print("I don't know what I speak")


class Cat(Pet):
    # adding more attributes
    def __init__(self, name, age, color):
        super().__init__(name, age)  # super references the parent class
        self.color = color
    def sound(self):
        print("Meow!")

    def show(self):
        print(f"I am {self.name} and I am {self.color} and {self.age} years old!")


class Dog(Pet):
    def sound(self):
        print("Barks!")


class Fish(Pet):
    pass


pet = Pet("Tim", 32)
pet.show()

cat = Cat("Mews", 4, "White with dots")
cat.show()
cat.sound()

dog = Dog("Rot", 23)
dog.show()
dog.sound()

fish = Fish("Salmon", 3)
fish.sound()

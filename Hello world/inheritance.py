class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    def miyau(self):
        print("Miyau")


class Dog(Mammal):
    def bark(self):
        print("bark")


animal = Dog()
animal.bark()
animal.walk()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance) of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling methods
print(person1.name)  # Accessing an attribute
person1.say_hello()  # Calling a method

# Inheritance in Python
#
# Inheritance allows a class (child/derived class) to inherit attributes and methods from another class (parent/base class).
# This promotes code reuse and enables the creation of hierarchical relationships.
#
# Syntax: class ChildClass(ParentClass):
#
# Example:
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")

dog = Dog('Buddy')
cat = Cat('Whiskers')
dog.speak()  # Output: Buddy barks.
cat.speak()  # Output: Whiskers meows.

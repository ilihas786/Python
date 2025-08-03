#########  The self Parameter in Python ##########################

# In Python, self is a reference to the current instance of the class.
# It is used to access variables and methods associated with the current object.
# self must be the first parameter of instance methods in a class (but is not a keyword).
# When you call a method on an object, Python automatically passes the object as the first argument to the method (as self).
#
# Example:
class Person:
    def __init__(self, name):
        self.name = name  # self refers to the instance

    def greet(self):
        print('Hello, my name is', self.name)

p = Person('Alice')
p.greet()  # Output: Hello, my name is Alice

# You can also access other methods using self inside the class:
class Calculator:
    def add(self, x, y):
        return x + y

    def double_sum(self, a, b):
        # Call another method using self
        return 2 * self.add(a, b)

calc = Calculator()
print(calc.double_sum(3, 4))  # Output: 14

############# Class Variables vs Instance Variables #########################################

# Class variable: Shared by all instances of the class. Defined directly inside the class, outside any method.
# Instance variable: Unique to each instance. Defined using self inside methods (usually __init__).
#
# Example:
class Dog:
    species = 'Canine'  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog('Buddy')
dog2 = Dog('Max')
print(dog1.name)      # Output: Buddy (instance variable)
print(dog2.name)      # Output: Max (instance variable)
print(dog1.species)   # Output: Canine (class variable)
print(dog2.species)   # Output: Canine (class variable)

# Changing class variable affects all instances:
Dog.species = 'Wolf'
print(dog1.species)   # Output: Wolf
print(dog2.species)   # Output: Wolf

# Changing instance variable only affects that instance:
dog1.name = 'Charlie'
print(dog1.name)      # Output: Charlie
print(dog2.name)      # Output: Max

# Here name is an instance variable, and self allows us to access it within the class methods.

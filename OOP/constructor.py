# Constructors in Python
#
# A constructor is a special method used to initialize objects of a class.
# In Python, the constructor method is called __init__.
# It is automatically called when a new object of the class is created.
# The __init__ method can take arguments to set up initial state (attributes) of the object.
#
# Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student('Bob', 21)
s1.display()  # Output: Name: Bob, Age: 21

# Types of Constructors in Python
#
# 1. Default Constructor: A constructor with no arguments (other than self). Sets default values.
class DefaultExample:
    def __init__(self):
        self.msg = "Default constructor called"
    def show(self):
        print(self.msg)
de = DefaultExample()
de.show()  # Output: Default constructor called

# 2. Parameterized Constructor: A constructor that takes arguments to initialize attributes (already shown above).
# Example: See Student class above.

# 3. Class/Static Constructor: Used to initialize class-level data. In Python, use @classmethod with __init_subclass__ or a custom method.
class ClassLevel:
    count = 0
    def __init__(self):
        ClassLevel.count += 1
    @classmethod
    def show_count(cls):
        print(f"Number of objects created: {cls.count}")
c1 = ClassLevel()
c2 = ClassLevel()
ClassLevel.show_count()  # Output: Number of objects created: 2

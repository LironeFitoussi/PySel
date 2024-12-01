# --------------- Class and Object ---------------
# 1. Class
# Class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# For example - Calculator class
# Sum, Multiply, Add, Divide, Subtract
# Methods, Class Variables, Instance Variables, Constructor
# --------------- Class and Object ---------------

# Calculator class
class Calculator:
    # Class Variables
    name = "Calculator"
    version = "1.0"

    # # Constructor
    # def __init__(self, name, version):
    #     # Instance Variables
    #     self.name = name
    #     self.version = version

    # Methods
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b 
    
# Create an object of Calculator class
calc = Calculator()
print(calc.add(5, 3))
print(calc.name) 
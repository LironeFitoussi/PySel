# --------------------------------------- Dictionary ---------------------------------------
# A dictionary is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object that you can create in Python as a value in a dictionary.

# Creating a dictionary
my_dict = {'name': 'John', 'age': 25, 'is_student': False, 5: 'hello'}

# Accessing elements in a dictionary
print("Name:", my_dict['name']) # Name: John

# Modifying elements in a dictionary
my_dict['age'] = 26

# Adding new key-value pairs
my_dict['address'] = 'Downtown'

# Data types that can be used as keys: strings, numbers, and tuples 
# (when all the elements of the tuple are immutable)
my_dict[(0, 1)] = 'a tuple'
print(my_dict[(0, 1)]) # a tuple

# Removing key-value pairs
del my_dict['is_student']

# Print full dictionary
print("Dictionary:", my_dict) # Dictionary: {'name': 'John', 'age': 26, 'address': 'Downtown'}


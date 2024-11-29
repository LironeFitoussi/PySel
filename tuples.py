# tuples.py

# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Accessing elements in a tuple
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuples are immutable, so you cannot change their elements
# my_tuple[0] = 10  # This will raise a TypeError

# Tuples can contain different data types
mixed_tuple = (1, "hello", 3.14, True)
print("Mixed tuple:", mixed_tuple) # Mixed tuple: (1, 'hello', 3.14, True)

# Tuples can be nested
nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested tuple:", nested_tuple) # Nested tuple: (1, (2, 3), (4, 5, 6))

# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e) # Unpacked values: 1 2 3 4 5

# Using tuples to return multiple values from a function
def min_max(numbers):
    return min(numbers), max(numbers)

test_tuple = (1, 2, 3, 4, 5)
min_val, max_val = min_max(test_tuple) # Unpacked values: 1 5

print("Min value:", min_val) # Min value: 1
print("Max value:", max_val) # Max value: 5

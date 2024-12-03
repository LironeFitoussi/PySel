# List in Python is a Data Type that is used to store multiple values in a single variable. like an array in other programming languages.
values = [1, 2, "Liron", 4, 5]

# Print First Value
print(values[0])  # 1

# Print Last Value
print(values[-1])  # 5

# Print Second Last Value
print(values[-2])  # 4

# Print a Index Value
print(values[2])  # Liron

# Print all values
print(values)  # [1, 2, 'Liron', 4, 5]

# Print a range of values
# Slicing in Python (Prining a range of values)
print(values[1:4])  # [2, 'Liron', 4]

# Print a range of values from start to a index
print(values[:4])  # [1, 2, 'Liron', 4]

# Print a range of values from a index to end
print(values[2:])  # ['Liron', 4, 5]

# Print a range of values from a index to end
print(values[2:-1])  # ['Liron', 4]

# Insert a value at a specific index
values.insert(2, "Python")
print(values)  # [1, 2, 'Python', 'Liron', 4, 5]

# Append a value at the end
values.append("End")
print(values)  # [1, 2, 'Python', 'Liron', 4, 5, 'End']

# Update a value at a specific index
values[2] = "Updated" # Like in JavaScript
print(values)  # [1, 2, 'Updated', 'Liron', 4, 5, 'End']

# Delete a value at a specific index
del values[2]
print(values)  # [1, 2, 'Liron', 4, 5, 'End']

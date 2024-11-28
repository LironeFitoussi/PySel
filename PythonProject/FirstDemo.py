print("hello")

# here is a comment in python

a = 3
print(a)

Str = "Hello World!"
print(Str)

b, c, f = 5, 6.4, "Great"

# print(b)
# print(c)
# print(f)

# print("value is "+b)
# First Option: using format method
print("{} {}".format("Value is", b))

# Second Option: using f-string
print(f"hello {b}")
# NOTE: In Python you cannot concatenate string with integer. You have to convert integer to string first.
# But in case of f-string, you can directly concatenate string with integer.

# Getting the data type
print(type(b)) # <class 'int'>
print(type(c)) # <class 'float'>
print(type(f)) # <class 'str'>



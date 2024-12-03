str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str2 = "RahulShetty"

print(str[1]) # a
print(str[0:5]) # Rahul

print(str[0:5] + str1) # RahulConsulting firm

# Check if a string is present in another string
print(str2 in str) # True

# Split the string
var = str.split(".")
print(var) # ['RahulShettyAcademy', 'com']
print(var[0]) # RahulShettyAcademy

# Remove white spaces
str3 = "    Hello World    "
print(str3.strip()) # Hello World

# left strip
print(str3.lstrip()) # Hello World

# right strip
print(str3.rstrip()) #     Hello World
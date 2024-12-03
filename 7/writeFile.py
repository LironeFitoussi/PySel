# # Write to a file by using the "w" mode. 
# # If the file does not exist, it will be created. 
# # If the file exists, it will be overwritten.
# with open('test.txt', "w") as file:
#     file.write("\nThis is a new line")
    
# # Write to a file by using the "a" mode.
# # If the file does not exist, it will be created.
# # If the file exists, the new data will be appended to the end of the file.
# with open('test.txt', "a") as file:
#     file.write("\nThis is another line")

# Instructor Version
with open('test.txt', "r") as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.txt', "w") as writer:
        for line in content:
            writer.write(line)


# My Version
# Reverse the content of the file
with open('test.txt', "r") as file:
    content = file.readlines()
    content.reverse()
    with open('test.txt', "w") as file:
        file.write(''.join(content))
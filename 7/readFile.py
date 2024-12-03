
# file = open("./test.txt")
# print(file.read())

# file.close()

with open("./test.txt", "r") as file:
    # Read the Entire File
    print("Read the Entire File: ")
    print(file.read())
    
    print("--------------------")
    file.seek(0)
    
    # Read the First 10 Characters
    print("Read the First 10 Characters: ")
    print(file.read(10))
    
    print("--------------------")
    
    # Read the Next 5 Characters
    print("Read Next 5 Characters: ")
    print(file.read(5))
    
    print("--------------------")
    file.seek(0)
    
    # Read line by line
    print("Read line by line: ")
    print("First Line: ")
    print(file.readline())
    
    print("Second Line: ")
    print(file.readline())
    
    print("Third Line: ")
    print(file.readline())
    
    print("--------------------")
    file.seek(0)
    
    # Read all lines
    print("Read all lines: ")
    print(file.readlines())
    file.seek(0)

    lines = file.readlines()

    for line in lines:
        if line != "\n":
            print(line)
        else:
            print("Empty Line")
    
    print("--------------------")
    # Check if the file is closed
    print(file.closed)

print(file.closed)
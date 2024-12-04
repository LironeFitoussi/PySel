# Try Except Mechanism
# Without try catch, the program will crash if the file is not found
#! with open('file.txt', 'r') as file:
#!         print(file.read())
# FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
# Program will crash: "Process finished with exit code 1"


# With try catch, the program will not crash if the file is not found
try:
    with open('file.txt', 'r') as file:
        print(file.read())

# Except block will catch the error and print the error message
except Exception as e:
    print('Error Occurred: ', e)

# Finally block will always run, regardless of the error
finally: 
    print('Program Completed')
    
# File Not Found
# Program will not crash: "Process finished with exit code 0"
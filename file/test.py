with open("test.txt","w") as f:
    f.write("Hello, this is a test file.\n")
    f.write("This file is used for testing file operations in Python.\n")
    f.write("We can write multiple lines to this file.\n")
    f.write("This is the last line of the test file.\n")

with open("test.txt", "a") as f:
    f.write("This line is appended to the test file.\n")
    f.write("Appending allows us to add content without overwriting existing data.\n")

with open("test.txt", "r") as f:
    print("Reading the entire content of the test file:")
    print(f.read())

with open("test.txt", "r") as f:
    print(f.read(5))

try:
    name = input("Enter your name: ")
except TypeError:
    print("Invalid input. Please enter a valid name.")
else:
    print("Correct")
finally:
    print("Execution completed.") 
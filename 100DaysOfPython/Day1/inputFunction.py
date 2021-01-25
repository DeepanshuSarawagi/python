"""
We are going to use the input function inside the print function
"""
name = input("What is your name? ")
if name == "deepanshu":
    print("Hello " + name)
else:
    print("Enter your valid first name")

print("Hello Mr. " + input("What is your last name? "))

# Day 1 Exercise 3 - Print the number of characters in a String

name = input("Please enter your username: ")
print(len(name))

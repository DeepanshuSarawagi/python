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

# Exercise 4 - Interchange the values of a and b using variables

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Band Name generator

print("Welcome to the band name generator")
city = input("Which city did you grow up in?\n")
pet = input("What is the name of your pet?\n")
band_name = city + " " + pet
print("Your band name could be {}".format(band_name))

__author__ = 'Dev'
name = input("Please enter your name: ")
# If you want to change the input data type to a certain type, then add the respective data type and assign it to the
# variable.
age = int(input("How old are you, {0}? ".format(name)))
print(age)

# Simple if..else program

if age >= 18:
    print("You are eligible to cast your vote, {}.".format(name))
else:
    print("Please come back after {} years, {}".format(18 - age, name))

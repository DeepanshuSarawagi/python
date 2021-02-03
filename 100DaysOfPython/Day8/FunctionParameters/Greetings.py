# In this lesson we are going to review the basics of Functions

# Difference between parameter and argument
# Parameter is the name of the data that is passed in
# Argument is the actual data that is passed while calling a function

def greet():
    print("Hello!")
    print("Welcome to the coders club!")
    print("Have a great day!")


greet()


def greet_with_name(name, location):
    print("Hello {}".format(name))
    print("How are you doing, {}?".format(name))
    print("How is the weather today in {}?".format(location))


greet_with_name(name=input("Enter your name: "), location="Chennai")

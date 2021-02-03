# In this lesson we are going to review the basics of Functions

def greet():
    print("Hello!")
    print("Welcome to the coders club!")
    print("Have a great day!")


greet()

def greet_with_name(name):
    print("Hello {}".format(name))
    print("How are you doing, {}?".format(name))


greet_with_name(name=input("Enter your name: "))

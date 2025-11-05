activity = input("What would you like to do today? ")
if "cinema" not in activity.casefold():
    print("I want to go to cinema!")

# Challenge

name = str(input("What is your name? "))
age = int(input("What is your age? "))

if 18 <= age < 31:
    print("Enjoy your holiday, {}!".format(name))
else:
    print("Sorry! But the holiday packages are not available.!")
day = "Monday"
temperature = 30
raining = False

if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

if 0:               # O, empty sequences except string are evaluated to False
    print("True")
else:
    print("False")

name = input("What is your name? ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")
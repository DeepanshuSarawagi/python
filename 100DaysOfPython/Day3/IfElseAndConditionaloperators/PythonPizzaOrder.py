print("Welcome to Python Pizza Deliveries!")
size = input("What size of Pizza would you like to have? S, M or L? ")
add_pepperoni = input("Would you like to add Pepperoni? Y or N? ")
extra_cheese = input("Would you like to have extra cheese? Y or N? ")

bill = 0
pepperoni = 0
cheese = 0
if size.upper() == "L":
    bill = 25
    if add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1
    print("Your final bill is {}".format(bill))
elif size.upper() == "M":
    bill = 20
    if add_pepperoni.upper() == "Y":
        bill += 3
    if extra_cheese.upper() == "Y":
        bill += 1
    print("Your final bill is {}".format(bill))
elif size.upper() == "S":
    bill = 15
    if add_pepperoni.upper() == "Y":
        bill += 2
    if extra_cheese.upper() == "Y":
        bill += 1
    print("Your final bill is {}".format(bill))
else:
    print("Please order a valid pizza! Let's start again")

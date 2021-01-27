# We are going to use If-Else statement here

print("Welcome to the Jumbo Roller Coaster")
height = int(input("What is your height in cm?\n"))
# if height >= 120:
#     print("Welcome aboard!")
# else:
#     print("Sorry! You cannot take the ride due to safety concerns!")

# Day 3 Exercise 1 - To find out if a number is odd or even

# num = int(input("Enter a number of your choice: "))
# if num % 2 == 0:
#     print("{} is an even number".format(num))
# else:
#     print("{} is an odd number".format(num))

# Nested if-else statement

bill = 0
if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("Please enter your age: "))
    if age > 18:
        bill = 12
        print("Adult tickets are $12 per ride. Enjoy!!")
    elif 12 <= age <= 18:
        bill = 7
        print("Youth tickets are $7 per ride. Enjoy!!")
    else:
        bill = 5
        print("Child tickets are $5 per ride. Enjoy!!")
    wants_photos = input("Do you want a photo taken? Y or N? ")
    if wants_photos.upper() == "Y":
        # Add $3 to the bill
        bill += 3
    print("Your bill for the ride is ${}.".format(bill))
else:
    print("Sorry! You cannot take the ride due to safety measures!")

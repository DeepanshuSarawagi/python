# We are going to use If-Else statement here

print("Welcome to the Jumbo Roller Coaster")
height = int(input("What is your height in cm?\n"))
if height >= 120:
    print("Welcome aboard!")
else:
    print("Sorry! You cannot take the ride due to safety concerns!")

# Day 3 Exercise 1 - To find out if a number is odd or even

num = int(input("Enter a number of your choice: "))
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

# Nested if-else statement

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("Please enter your age: "))
    if age > 18:
        print("Please pay $12 for the ride. Enjoy!!")
    elif 12 <= age <= 18:
        print("Please pay $7 for the ride. Enjoy!!")
    else:
        print("Please pay $5 for the ride. Enjoy!!")
else:
    print("Sorry! You cannot take the ride due to safety measures!")

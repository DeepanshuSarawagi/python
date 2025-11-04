import random

age = int(input("What is your age? "))

if 16 <= age <= 65:
    print("Have a good day at work!")
else:
    print("Sorry, you are not old enough to do that")

answer = 5
guess = 6
while guess != answer:
    guess = random.randint(1, 11)
    print("New random number is:", guess)
    if guess == answer:
        print("You guessed the number")
    else:
        print("Keep guessing the number")

if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("Have a good day at work!")
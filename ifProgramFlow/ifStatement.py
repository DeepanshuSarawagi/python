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

print()

guess = int(input("Please guess a number between 1 to 10: "))
# if guess < 5:
#     print("Please guess a higher number")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it correctly")
#     else:
#         print("Sorry you got it wrong this time")
# elif guess > 5:
#     print("Please guess a lower number")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it correctly")
#     else:
#         print("Sorry you got it wrong this time")
# else:
#     print("Well done, you got it right first time")

# The above block of code can be simplified like below avoiding the repetition.

if guess != 5:
    if guess < 5:
        print("Please guess a higher number")
    else:
        print("Please guess a lower number")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it right")
    else:
        print("Sorry you got it wrong this time")
else:
    print("Well done, you got it right first time")

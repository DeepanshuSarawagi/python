# In this mini project we are going to create a number guessing game
import random


def difficulty_level():
    count = 0
    if difficulty == "easy":
        print("You have 10 attempts to guess the number: ")
        while number_guessing() != True and count < 11:
            number_guessing()
    else:
        print("You have 5 attempts to guess the number: ")
        while number_guessing() != True and count < 6:
            number_guessing()


def number_guessing():
    choice = int(input("Make a guess: "))
    if choice < num:
        print("Too low. Try again.")
    elif choice > num:
        print("Too high. Try again.")
    else:
        print("Awesome!! You got it right!!")
        return True


print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)

difficulty = input("Choose the difficult to guess the number. Type 'easy' or 'hard': ").lower()

guess = int(input("Make a guess: "))

difficulty_level()
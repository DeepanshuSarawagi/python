# In this mini project we are going to create a number guessing game
import random

print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)

difficulty = input("Choose the difficult to guess the number. Type 'easy' or 'hard': ").lower()

guess = int(input("Make a guess: "))


def number_guessing():
    count = 0
    if difficulty == "easy":
        print("You have 10 attempts to guess the number: ")
    else:
        print("You have 5 attempts to guess the number: ")


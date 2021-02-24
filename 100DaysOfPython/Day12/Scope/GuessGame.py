import random


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("You got it right. The answer was {}".format(answer))


print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)

guess = int(input("Make a guess: "))


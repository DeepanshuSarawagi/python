import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print("You got it right. The answer was {}".format(answer))


def set_difficulty():
    level = input("Choose a difficult 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print("Welcome to the guessing game!")
print("I'm thinking of a number between 1 and 100")

answer = random.randint(1, 100)
guess = int(input("Make a guess: "))
turns = set_difficulty()

print("Pssssst!! The answer is {}".format(answer))


print("You have {} attempts remaining to guess the number.".format(turns))

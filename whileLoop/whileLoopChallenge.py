import random
highest = 100
guess = 0
no_of_guess = 0
answer = random.randint(1, highest)
print(f"Please guess a number between 1 and {highest}: ")

while guess != answer:
    guess = int(input())
    no_of_guess += 1
    if guess == 0:
        print("You cannot guess 0")
        break
    if no_of_guess > 20 and guess != answer:
        print("You cannot have more than 20 guesses")
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print(f"You have got it right in {no_of_guess} guesses")

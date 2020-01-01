import random
highest = 10
guess = 0
answer = random.randint(1, highest)
print(f"Please guess a number between 1 and {highest}: ")

while guess != answer:
    guess = int(input())
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    else:
        print("You have got it right this time")

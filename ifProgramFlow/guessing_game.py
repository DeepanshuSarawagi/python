import random

answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())
# guess = random.randint(1, 11)
# print(guess)
if guess < answer:
    print("Your guess is too low")
elif guess > answer:
    print("Your guess is too high")
else:
    print("You guessed correctly")
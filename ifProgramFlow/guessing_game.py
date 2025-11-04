import random

answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())
# guess = random.randint(1, 11)
# print(guess)
# if guess < answer:
#     print("Your guess is too low")
#     guess = int(input("Please guess higher: "))
#     if guess == answer:
#         print("Well done, you guessed correctly!")
#     else:
#         print("Sorry! You have not guessed correctly")
# elif guess > answer:
#     print("Your guess is too high")
#     guess = int(input("Please guess lower: "))
#     if guess == answer:
#         print("Well done, you guessed correctly!")
#     else:
#         print("Sorry! You have not guessed correctly")
# else:
#     print("You guessed correctly")
if guess == answer:
    print("You guessed the number")
else:
    if guess < answer:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    guess = int(input())
    if guess == answer:
        print("Well done!, you guessed the number")
    else:
        print("Sorry! you have not guessed the number")
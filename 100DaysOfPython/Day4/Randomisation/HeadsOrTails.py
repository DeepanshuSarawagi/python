import random

print("Welcome to the virtual coin toss program")
for i in range(0, 10):
    toss = random.randint(0, 1)
    if toss == 1:
        print("You got Heads this time")
    else:
        print("You got Tails this time")

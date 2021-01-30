import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rpsl = [rock, paper, scissors]
choice = int(input("Type what you choose? 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer = random.choice(rpsl)

print("You chose: \n " + rpsl[choice])
print("Computer chose: \n" + computer)
if rpsl[choice] == computer:
    print("It is a draw")
elif rpsl[choice] == rock:
    if computer == scissors:
        print("You win")
    else:
        print("You lose")
elif rpsl[choice] == paper:
    if computer == rock:
        print("You win")
    else:
        print("You lose")
elif rpsl[choice] == scissors:
    if computer == paper:
        print("You win")
    else:
        print("You lose")

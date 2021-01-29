print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
left_right = input("You are at a cross road. Which way would you want to go? Left or Right? ")
if left_right.lower() == "left":
    lake = input("There is a lake ahead of you! Would you like to take boat or swim? Wait? Swim? ")
    if lake.lower() == "wait":
        door = input("You are now at the cave? Which color would you choose? Blue? Red? Yellow? ")
        if door.lower() == "red":
            print("Fire broke out. GAME OVER!!")
        elif door.lower() == "blue":
            print("AARRGGGGGHHH!! You got eaten by beasts. GAME OVER!!")
        elif door.lower() == "yellow":
            print("Yayyy!! You found the treasure. You WIN!!")
        else:
            print("You cannot choose this door! GAME OVER!!")
    else:
        print("Whoooossshhh!! You chose to swim and got attacked by a crocodile. GAME OVER!!")
else:
    print("Sorry! You fell into hole by going right. GAME OVER!!")

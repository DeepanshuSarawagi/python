import game_data
import random

first_random = random.choice(game_data.data)
first_item = list(first_random.values())
second_random = random.choice(game_data.data)
second_item = list(second_random.values())
if first_item[0] == second_item[0]:
    second_random = random.choice(game_data.data)
    second_item = list(second_random.values())


score = 0
got_it_right = True


def compare(first_item, second_item):
    if first_item[1] > second_item[1]:
        return True
    else:
        return False


def play_game():
    global first_item
    global second_item
    global score
    global got_it_right
    print("Compare {}: {}, {}, {}, {}".format("A", first_item[0], first_item[1], first_item[2], first_item[3]))
    print("Compare {}: {}, {}, {}, {}".format("B", second_item[0], second_item[1], second_item[2], second_item[3]))
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == "A":
        if compare(first_item=first_item, second_item=second_item):
            score += 1
            print("You got it right. Current score: {}".format(score))
        else:
            print("Sorry you got it wrong! Final score: {}".format(score))
            got_it_right = False
    elif choice == "B":
        if compare(first_item=first_item, second_item=second_item):
            print("Sorry you got it wrong! Final score: {}".format(score))
            got_it_right = False
        else:
            score += 1
            print("You got it right. Current score: {}".format(score))
    first_item = second_item
    second_item = list(random.choice(game_data.data).values())
    if second_item == first_item:
        second_item = list(random.choice(game_data.data).values())


while got_it_right:
    play_game()
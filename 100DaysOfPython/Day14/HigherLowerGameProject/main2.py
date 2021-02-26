# This is the proposed solution by the instructor

from game_data import data
import random


def format_data(account):

    account_name = account["name"]
    account_decr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_decr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)
    print("Compare A: {}".format(format_data(account_a)))
    print("Compare B: {}".format(format_data(account_b)))

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess=guess, a_followers=a_follower_count, b_followers=b_follower_count)

    if is_correct:
        score += 1
        print("You got it right! Current score: {}".format(score))
    else:
        game_should_continue = False
        print("Sorry! You got it wrong. Final score: {}".format(score))

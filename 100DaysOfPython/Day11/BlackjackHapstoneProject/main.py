# This is how instructor completed the project
import random


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def deal_card():
    """Returns a random card from the deck."""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print("Your cards: {}. Your score is {}.".format(user_cards, user_score))
    print("Computer's first card: {}".format(computer_cards[0]))

    if user_score == 0 or computer_score == 0 or computer_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Do you want to deal another card or fold? Type 'y' or 'n': ").lower()
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
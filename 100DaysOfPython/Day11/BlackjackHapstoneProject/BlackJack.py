# In this project we are going to create a BlackJack command line game

import os
import random

cards = {
    "A of Hearts": 1,
    "2 of Hearts": 2,
    "3 of Hearts": 3,
    "4 of Hearts": 4,
    "5 of Hearts": 5,
    "6 of Hearts": 6,
    "7 of Hearts": 7,
    "8 of Hearts": 8,
    "9 of Hearts": 9,
    "10 of Hearts": 10,
    "Jack of Hearts": 10,
    "Queen of Hearts": 10,
    "King of Hearts": 10,
    "A of Diamonds": 1,
    "2 of Diamonds": 2,
    "3 of Diamonds": 3,
    "4 of Diamonds": 4,
    "5 of Diamonds": 5,
    "6 of Diamonds": 6,
    "7 of Diamonds": 7,
    "8 of Diamonds": 8,
    "9 of Diamonds": 9,
    "10 of Diamonds": 10,
    "Jack of Diamonds": 10,
    "Queen of Diamonds": 10,
    "King of Diamonds": 10,
    "A of Spades": 1,
    "2 of Spades": 2,
    "3 of Spades": 3,
    "4 of Spades": 4,
    "5 of Spades": 5,
    "6 of Spades": 6,
    "7 of Spades": 7,
    "8 of Spades": 8,
    "9 of Spades": 9,
    "10 of Spades": 10,
    "Jack of Spades": 10,
    "Queen of Spades": 10,
    "King of Spades": 10,
    "A of Clubs": 1,
    "2 of Clubs": 2,
    "3 of Clubs": 3,
    "4 of Clubs": 4,
    "5 of Clubs": 5,
    "6 of Clubs": 6,
    "7 of Clubs": 7,
    "8 of Clubs": 8,
    "9 of Clubs": 9,
    "10 of Clubs": 10,
    "Jack of Clubs": 10,
    "Queen of Clubs": 10,
    "King of Clubs": 10
}

players_hand = []
dealers_hand = []

game_deck = cards.copy()

player_score = 0
dealer_score = 0


def initial_game():
    global player_score
    global dealer_score
    for i in range(2):
        card = random.choice(list(game_deck.keys()))
        if card not in players_hand:
            players_hand.append(card)
            game_deck.pop(card)

    display_hands(players_hand)
    player_score = calculate_score(players_hand)

    print(player_score)

    card = random.choice(list(game_deck.keys()))
    if card not in dealers_hand:
        dealers_hand.append(card)
        game_deck.pop(card)

    display_hands(dealers_hand)
    dealer_score = calculate_score(dealers_hand)
    print(dealer_score)


def calculate_score(hands):
    score = 0
    for card in hands:
        score += cards[card]
    if ("A of Hearts" in hands or "A of Diamonds" in hands or "A of Spades" in hands or "A of Clubs" in hands) \
            and (score < 22):
        return score + 10
    else:
        return score


def display_hands(hands):
    for hand in hands:
        print(hand, end="\t")
    print()


want_to_play = True


def deal_player():
    card = random.choice(list(game_deck.keys()))
    if card not in players_hand:
        players_hand.append(card)
        game_deck.pop(card)


def deal_dealer():
    card = random.choice(list(game_deck.keys()))
    if card not in dealers_hand:
        dealers_hand.append(card)
        game_deck.pop(card)


def declare_winner():
    if player_score == dealer_score:
        print("Player score is {}. Dealer score is {}. It is a draw".format(player_score, dealer_score))
    elif player_score == 21 or dealer_score > 21:
        print("Yon win!")
    elif dealer_score < player_score < 22:
        print("You win")
    elif player_score > 21:
        print("You lost!")
    else:
        print("You lost!")


def final_game():
    global dealer_score
    global player_score
    initial_game()
    continue_dealing = True
    while continue_dealing:
        choice = input("Do you still want to deal or fold? Type 'y' to deal or type 'n' to fold: ").lower()
        if choice == "y":
            deal_player()
            display_hands(players_hand)
            player_score = calculate_score(players_hand)
            print(player_score)
        else:
            while dealer_score < 17:
                deal_dealer()
                dealer_score = calculate_score(dealers_hand)

            dealer_score = calculate_score(dealers_hand)
            display_hands(dealers_hand)
            print(dealer_score)
            declare_winner()
            continue_dealing = False


while want_to_play is True:
    dealers_hand.clear()
    players_hand.clear()
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game == "y":
        os.system("clear")
        final_game()
    else:
        want_to_play = False

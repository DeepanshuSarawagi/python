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
ace = 11

hands_of_ace = ["A of Hearts", "A of Diamonds", "A of Spades", "A of Clubs"]


def calculate_score(hands):
    score = 0
    for card in hands:
        # if (("A of Hearts" in hands) or ("A of Diamonds" in hands) or ("A of Spades" in hands) or
        #     ("A of Clubs" in hands)) and (score + ace < 22):
        if card in hands_of_ace and score + ace < 22:
            score += ace
        else:
            score += cards[card]
    return score


def display_hands(player_hand, dealer_hand):
    print("Player's hands: {}".format(player_hand))
    print("Player's score: {}".format(player_score))
    print("Dealer's hands: {}".format(dealer_hand))
    print("Dealer's score: {}".format(dealer_score))


def initial_game():
    global player_score
    global dealer_score
    for i in range(2):
        card = random.choice(list(game_deck.keys()))
        if card not in players_hand:
            players_hand.append(card)
            game_deck.pop(card)

    player_score = calculate_score(hands=players_hand)
    display_hands(player_hand=players_hand, dealer_hand=dealers_hand)

    card = random.choice(list(game_deck.keys()))
    if card not in dealers_hand:
        dealers_hand.append(card)
        game_deck.pop(card)

    dealer_score = calculate_score(dealers_hand)
    display_hands(player_hand=players_hand, dealer_hand=dealers_hand)


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


def declare_winner(player_score, dealer_score):
    if player_score > 21:
        print("You lost!")
    elif dealer_score > 21:
        print("You win!")
    elif player_score == dealer_score:
        print("Player score is {}. Dealer score is {}. It is a draw".format(player_score, dealer_score))
    elif player_score == 21 or dealer_score > 21:
        print("Yon win!")
    elif dealer_score < player_score < 22:
        print("You win")
    elif player_score > 21:
        print("You lost!")
    else:
        print("You lost!")


def is_game_over():
    global player_score
    global dealer_score
    if player_score == 21 or dealer_score == 21:
        return True
    elif player_score > 21 or dealer_score > 21:
        return True
    else:
        return False


def final_game():
    global dealer_score
    global player_score
    initial_game()
    continue_dealing = True
    while continue_dealing:
        if not is_game_over():
            choice = input("Do you still want to deal or fold? Type 'y' to deal or type 'n' to fold: ").lower()
            if choice == "y":
                deal_player()
                player_score = calculate_score(players_hand)
                display_hands(player_hand=players_hand, dealer_hand=dealers_hand)
            else:
                while dealer_score < 17:
                    deal_dealer()
                    dealer_score = calculate_score(dealers_hand)

                dealer_score = calculate_score(dealers_hand)
                display_hands(player_hand=players_hand, dealer_hand=dealers_hand)
                declare_winner(player_score=player_score, dealer_score=dealer_score)
                continue_dealing = False
        else:
            declare_winner(player_score=player_score, dealer_score=dealer_score)
            continue_dealing = False


while want_to_play is True:
    dealers_hand.clear()
    players_hand.clear()
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game == "y":
        os.system("clear")
        player_score = 0
        dealer_score = 0
        final_game()
    else:
        want_to_play = False

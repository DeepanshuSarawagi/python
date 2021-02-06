# In this project we are going to create secret bidder program

import os

bidder_list = {}
is_bidder = True


def add_bidder_to_list():
    name = input("Enter your name: ")
    bid_amount = int(input("Enter the amount you want to bid: $"))
    bidder_list[name] = bid_amount


add_bidder_to_list()

while is_bidder:
    choice = input("Is there anyone else who wants to bid? Type 'yes' or 'no'. ").lower()
    if choice == "yes":
        os.system("clear")
        add_bidder_to_list()
    else:
        os.system("clear")
        is_bidder = False
        highest = 0
        highest_bidder = ""
        for bidder in bidder_list:
            if bidder_list[bidder] > highest:
                highest = bidder_list[bidder]
                highest_bidder = bidder
        print("The winner in the auction is {} with the bid amount is ${}.".format(highest_bidder, highest))

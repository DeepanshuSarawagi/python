import tkinter
import random

# Create a function to load card images


def load_images(card_image):
    # load images for each suit
    suits = ['club', 'diamond', 'spade', 'heart']
    face_cards = ['jack', 'king', 'queen']
    # check the tkinter version for extension support
    if tkinter.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'
    # for each suit retrieve the image of the cards
    for suit in suits:
        # first the number cards from 1 to 11
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_image.append((card, image,))

    # now retrieve images for face cards
        for card in face_cards:
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            if card == 'jack':
                card_image.append((11, image,))
            if card == 'king':
                card_image.append((13, image,))
            if card == 'queen':
                card_image.append((12, image,))


def _deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    deck.append(next_card)  # Add the card back to the end of deck
    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='sunken').pack(side='left')
    # now return the card's face value
    return next_card


def score_hand(hand):
    # Calculate the total score of all the cards in the list
    # Only one ace can have the value 11 and if we would bust then subtract the value by 10
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        # If we would bust, check if there is an ace and subtract 10 from the score
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


# create a function to display the images in the dealer or player's card frame
def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer Wins")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player Wins")
    elif dealer_score > player_score:
        result_text.set("Dealer Wins")
    else:
        result_text.set("Draw")


def deal_player():
    player_hand.append(_deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins ")

    # global player_score
    # global player_ace
    # card_value = int(deal_card(player_card_frame)[0])
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust check if there is an ace and then subtract
    # if card_value > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Player wins")


def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the dealer card images
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky='ew')
    # embedded frame to hold the player card images
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    result_text.set("")

    dealer_hand = []
    player_hand = []
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


def play():
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    mainWindow.mainloop()


# setup the screen and frames for dealer and player

mainWindow = tkinter.Tk()
mainWindow.title('Black Jack')
mainWindow.geometry('640x480-8-200')
mainWindow.configure(background='green')

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=2, background='green')
card_frame.grid(row=1, column=0, columnspan=3, rowspan=2, sticky='ew')

# dealer score label

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text='dealer', background='green', fg='white').grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background='green', fg='white').grid(row=1, column=0)

# embedded frames to hold the cards
dealer_card_frame = tkinter.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# Player score label
player_score_label = tkinter.IntVar()
# player_score = 0
# player_ace = False
tkinter.Label(card_frame, text='player', background='green', fg='white').grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)

# embedded frames to hold the cards
player_card_frame = tkinter.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Add buttons for dealer and player
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, sticky='w', columnspan=3)

dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=0, column=2)

cards = []
load_images(cards)
print(cards)

# create a deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# just a check if you are loading all the cards
# for deck_card in deck:
#     card_face, suit = deck_card
#     print(f"card is {card_face} and suit is {suit}")
# commented this because its no more required

# create new lists to store dealer`s and player`s hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()

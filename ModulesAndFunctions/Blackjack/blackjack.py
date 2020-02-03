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
            card_image.append((card, image,))


def deal_card(frame):
    # pop the next card off the top of the deck
    next_card = deck.pop(0)
    # Add the image to a label and display the label
    tkinter.Label(frame, image=next_card[1], relief='sunken').pack(side='left')
    # now return the card's face value
    return next_card[0]


# create a function to display the images in the dealer or player's card frame
def deal_dealer():
    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)


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

cards = []
load_images(cards)
print(cards)

# create a deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# just a random check if you are loading all the cards
# for deck_card in deck:
#     card_face, suit = deck_card
#     print(f"card is {card_face} and suit is {suit}")
# commented this because its no more required

# create new lists to store dealer`s and player`s hands
dealer_hand = []
player_hand = []

mainWindow.mainloop()

import tkinter
import random

mainWindow = tkinter.Tk()

# setup the screen and frames for dealer and player

mainWindow.title('Black Jack')
mainWindow.geometry('640x480-8-200')

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

dealer_button = tkinter.Button(button_frame, text='Dealer')
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text='Player')
player_button.grid(row=0, column=1)

mainWindow.mainloop()
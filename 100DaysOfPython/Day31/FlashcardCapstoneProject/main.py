from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_fr = {}

window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=card_front)
card_back = PhotoImage(file="images/card_back.png")

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# reading CSV using pandas
data = pandas.read_csv("data/french_words.csv")
# data_dict = {row.French: row.English for index, row in data.iterrows()}
data_dict = data.to_dict(orient="records")
# print(data_dict)

# Creating text in canvas
title = canvas.create_text(400, 150, font=("Ariel", 34, "italic"), text="")
card_word = canvas.create_text(400, 263, font=("Ariel", 48, "bold"), text="")


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_word, text=random_fr["English"], fill="white")


def create_flash_cards():
    # global french
    # canvas.delete(french)
    global random_fr, flip_timer
    window.after_cancel(flip_timer)
    random_fr = random.choice(data_dict)
    # french = canvas.create_text(400, 263, font=("Ariel", 48, "bold"), text=random_fr["French"])
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_word, text=random_fr["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def is_know():
    data_dict.remove(random_fr)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    create_flash_cards()


flip_timer = window.after(3000, func=flip_card)

right_button = Button(image=right_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1, pady=50)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=create_flash_cards)
wrong_button.grid(row=1, column=0, pady=50)

create_flash_cards()

window.mainloop()

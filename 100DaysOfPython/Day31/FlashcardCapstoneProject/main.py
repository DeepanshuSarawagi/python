from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card Project")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# reading CSV using pandas
data = pandas.read_csv("data/french_words.csv")
# data_dict = {row.French: row.English for index, row in data.iterrows()}
data_dict = data.to_dict(orient="records")
# print(data_dict)

# Creating text in canvas
title = canvas.create_text(400, 150, font=("Ariel", 34, "italic"), text="French")
french = canvas.create_text(400, 263, font=("Ariel", 48, "bold"), text="")


def create_flash_cards():
    global french
    canvas.delete(french)
    random_fr = random.choice(data_dict)
    french = canvas.create_text(400, 263, font=("Ariel", 48, "bold"), text=random_fr["French"])


right_button = Button(image=right_image, highlightthickness=0, command=create_flash_cards)
right_button.grid(row=1, column=1, pady=50)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=create_flash_cards)
wrong_button.grid(row=1, column=0, pady=50)

create_flash_cards()

window.mainloop()

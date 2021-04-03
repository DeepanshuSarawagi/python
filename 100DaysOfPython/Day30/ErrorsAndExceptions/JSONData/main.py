from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
characters = ["a", "b", "c", "d", "f", "g", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q",
              "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
special_symbols = ["@", "!", "$", "^"]


def gen_random_character():
    char = random.choice(characters)
    choice = random.randint(0, 1)
    if choice == 1:
        char = char.upper()
    return char


def generate_password():
    password_list = []
    password = ""
    while len(password_list) < 8:
        char = gen_random_character()
        if char not in password_list:
            password_list.append(char)
        else:
            continue

    for _ in range(2):
        number = random.choice(numbers)
        password_list.append(number)
    for _ in range(2):
        char = random.choice(special_symbols)
        password_list.append(char)

    random.shuffle(password_list)
    for p in range(0, len(password_list)):
        password += password_list[p]
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_list.clear()


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    add_password_button.focus()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"Email: {email}\n Password: {password}\n "
                                                                f"Is it ok to save? ")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    # Loading the data from the JSON file
                    data = json.load(file)
                    # Updating the data with new data
                    data.update(new_data)
                    # Writing the data to the JSON file
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(row=2, column=0)
email_user_entry = Entry(width=35)
email_user_entry.insert(0, "example@email.com")
email_user_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add Password", width=36, command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

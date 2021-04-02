from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(row=2, column=0)
email_user_entry = Entry(width=35)
email_user_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add Password", width=36)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

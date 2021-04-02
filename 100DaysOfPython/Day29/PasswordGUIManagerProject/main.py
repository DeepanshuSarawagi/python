from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():

    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    add_password_button.focus()
    with open("passwords.txt", "a") as file:
        final_string = "{} | {} | {}\n".format(website, email, password)
        file.writelines(final_string)
    website_entry.delete(0, "end")
    email_user_entry.delete(0, "end")
    password_entry.delete(0, "end")
    website_entry.focus()
    email_user_entry.insert(0, "example@email.com")


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

gen_password_button = Button(text="Generate Password")
gen_password_button.grid(row=3, column=2)

add_password_button = Button(text="Add Password", width=36, command=add_password)
add_password_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

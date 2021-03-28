from tkinter import *


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

# We will now create a label inside the tkinter window
my_label = Label(text="My first label", font=("Arial", 24))
my_label.pack()  # We need to call this method so that the label becomes visible in the tkinter window

# choices = [num for num in range(0, 100)]
# choicesvar = tkinter.StringVar(value=choices)
# l = tkinter.Listbox(window, listvariable=choicesvar)
# l.pack()
#
# messagebox1 = messagebox.showinfo(title="Example", message="information")


def button_clicked():
    print("I got clicked")
    text_message = input.get()
    my_label.config(text=text_message)


button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=30)
input.insert(END, string="Some text to begin with")
input.pack()

text = Text(height=5, width=30)
text.focus()  # To have the cursor at starting point in text box
text.insert(END, chars="Some multiline text to begin with in a text box")
print(text.get(1.0, END))
text.pack()


def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=50, command=scale_used)
scale.pack()


def checkButton_used():
    print(checked_state.get())


checked_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=checked_state, command=checkButton_used, state="normal")
check_button.pack()

window.mainloop()

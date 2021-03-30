from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button2 = Button(text="Click Me Please!", command=button_clicked)
button2.grid(column=2, row=0)

input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)


window.mainloop()

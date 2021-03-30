from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=10)
print(input.get())
input.pack()


window.mainloop()

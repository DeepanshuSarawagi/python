from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="I Am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.pack()

window.mainloop()
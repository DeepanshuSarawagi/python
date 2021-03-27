import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# We will now create a label inside the tkinter window
my_label = tkinter.Label(text="My first label", font=("Arial", 24))
my_label.pack()  # We need to call this method so that the label becomes visible in the tkinter window
choices = [num for num in range(0, 100)]
choicesvar = tkinter.StringVar(value=choices)
l = tkinter.Listbox(window, listvariable=choicesvar)
l.pack()

messagebox1 = tkinter.messagebox.showinfo(title="Example", message="information")
messagebox1.pack()

window.mainloop()

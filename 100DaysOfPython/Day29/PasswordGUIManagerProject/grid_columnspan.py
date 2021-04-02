from tkinter import *

window = Tk()
window.title("Grid basics")
r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0, columnspan=1)

b = Label(bg="blue", width=20, height=5)
b.grid(row=1, column=1, columnspan=1)

g = Label(bg="green", width=40, height=5)
g.grid(row=2, column=0, columnspan=2)

window.mainloop()

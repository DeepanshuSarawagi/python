import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# We will now create a label inside the tkinter window
my_label = tkinter.Label(text="My first label")
my_label.pack()  # We need to call this method so that the label becomes visible in the tkinter window

window.mainloop()

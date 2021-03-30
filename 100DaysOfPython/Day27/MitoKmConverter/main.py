from tkinter import *


def mile_to_km():
    mile = int(user_input.get())
    km = float(mile * 1.60934)
    converted_label.config(text="{:.2f}".format(km))


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

user_input = Entry(width=10)
user_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(row=0, column=2)

equal_to_label = Label(text="is equal to ", font=("Arial", 20, "bold"))
equal_to_label.grid(row=1, column=0)

converted_label = Label(text="", font=("Arial", 20, "bold"))
converted_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=mile_to_km, font=("Arial", 18, "bold"))
button.grid(row=2, column=1)

window.mainloop()

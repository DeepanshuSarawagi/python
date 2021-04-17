from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", padx=20, pady=20)
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas()
        self.canvas.configure(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.window.mainloop()

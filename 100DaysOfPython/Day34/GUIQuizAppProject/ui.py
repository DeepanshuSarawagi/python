from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):  # Add the datatype of quiz parameter as Class QuizBrain
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.configure(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some input text",
                                                     fill=THEME_COLOR, font=("Arial", 20, "bold"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.get_next_question)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.get_next_question)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text, justify="center")

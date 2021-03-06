from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(-30, 280)
        self.write(f"Score = {self.score}", font=("Arial", 12, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f"Score = {score}", font=("Arial", 12, "normal"))

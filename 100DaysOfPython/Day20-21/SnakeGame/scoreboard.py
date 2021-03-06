from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.setposition(0, 280)

    def update_score(self, score):
        self.clear()
        self.write(f"Score = {score}", font=("Arial", 12, "normal"))

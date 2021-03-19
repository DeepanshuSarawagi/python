from turtle import Turtle

FILE_LOCATION = "/Users/deepanshusarawagi/Desktop/Learning/python/100DaysOfPython/Day24/FilesDirectoriesPaths"


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open(f"{FILE_LOCATION}/highscore.txt", "r") as file:
            data = file.read()
        self.high_score = int(data)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(-30, 280)
        self.write(f"Score = {self.score} High Score = {self.high_score}", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", font=("Arial", 20, "normal"))

    # def game_over(self):
    #     self.color("red")
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(f"{FILE_LOCATION}/highscore.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.setposition((0, 0))
        self.speed("fast")

    def move_ball(self):
        x_pos = random.randint(-350, 350)
        y_pos = random.randint(-300, 300)
        self.setposition((x_pos, y_pos))

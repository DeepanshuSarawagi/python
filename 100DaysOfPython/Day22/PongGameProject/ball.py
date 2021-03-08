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
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self):
        self.y_move *= -1

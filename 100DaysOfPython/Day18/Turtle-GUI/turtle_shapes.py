from turtle import Turtle
from turtle import Screen
import random

screen = Screen()

screen.colormode(255)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")


def draw_shapes(distance, n):
    angle = round(360 / n, 2)
    R = random.randrange(0, 257, 10)
    G = random.randrange(0, 257, 10)
    B = random.randrange(0, 257, 10)
    timmy.color(R, G, B)
    for _ in range(n):
        timmy.forward(distance)
        timmy.right(angle)


for i in range(3, 11):
    draw_shapes(100, i)

screen.exitonclick()

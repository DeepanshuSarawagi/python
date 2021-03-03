# In this challenge we are going to draw a spirograph

from turtle import Turtle
from turtle import Screen
import random


timmy = Turtle()
timmy.speed("fastest")
timmy.hideturtle()
screen = Screen()
screen.colormode(255)

for _ in range(0, 361, 4):
    R = random.randrange(0, 255, 50)
    G = random.randrange(0, 255, 50)
    B = random.randrange(0, 255, 50)
    timmy.color(R, G, B)
    timmy.circle(radius=100)
    timmy.left(4)


screen.exitonclick()

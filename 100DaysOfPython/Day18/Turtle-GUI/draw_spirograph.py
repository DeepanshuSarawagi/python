# In this challenge we are going to draw a spirograph

from turtle import Turtle
from turtle import Screen
import random


timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)

for _ in range(0, 361, 5):
    R = random.randint(0, 255)
    B = random.randint(0, 255)
    G = random.randint(0, 255)
    timmy.color(R, B, G)
    timmy.circle(radius=100)
    timmy.left(5)


screen.exitonclick()

from turtle import Turtle
from turtle import Screen
import random

screen = Screen()
timmy = Turtle()
timmy.width(10)
screen.colormode(255)
direction = [timmy.forward]
side = [0, 90, 180, 270]
timmy.speed("fast")


def move():
    for _ in range(200):
        R = random.randrange(0, 257, 10)
        B = random.randrange(0, 257, 10)
        G = random.randrange(0, 257, 10)
        timmy.color(R, B, G)
        random_direction = random.choice(direction)
        dist = random.randint(20, 30)
        random_direction(distance=dist)
        random_side = random.choice(side)
        timmy.setheading(random_side)


move()

screen.exitonclick()
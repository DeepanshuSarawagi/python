from turtle import Screen
import turtle
import random

screen = Screen()
screen.colormode(255)
timmy = turtle.Turtle()
timmy.penup()


def draw_dot():
    for _ in range(10):
        R = random.randrange(0, 255, 10)
        G = random.randrange(0, 255, 10)
        B = random.randrange(0, 255, 10)
        timmy.dot(20, (R, G, B))
        timmy.forward(50)


for i in range(0, 500, 50):
    timmy.setposition(-300.0, (-300 + i))
    draw_dot()


screen.exitonclick()

from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("tomato")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.left(90)

for i in range(10):
    timmy.forward(15)
    timmy.penup()
    timmy.forward(15)
    timmy.pendown()


def parallel():
    timmy.forward(100)
    timmy.rt(90)
    timmy.pu()
    timmy.forward(10)
    timmy.rt(90)
    timmy.pendown()
    timmy.forward(100)
    timmy.left(90)
    timmy.penup()
    timmy.forward(10)
    timmy.left(90)
    timmy.pendown()


for _ in range(5):
    parallel()

screen = Screen()
screen.exitonclick()

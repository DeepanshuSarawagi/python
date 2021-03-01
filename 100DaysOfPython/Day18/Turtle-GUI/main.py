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


screen = Screen()
screen.exitonclick()

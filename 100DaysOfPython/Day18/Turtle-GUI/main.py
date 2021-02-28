from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("tomato")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()

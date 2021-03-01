from turtle import Turtle
from turtle import Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange")


def triangle():
    timmy.forward(100)
    timmy.right(120)


def square():
    timmy.forward(100)
    timmy.right(90)


def pentagon():
    timmy.forward(100)
    timmy.right(72)


def hexagon():
    timmy.forward(100)
    timmy.right(60)


def heptagon():
    timmy.forward(100)
    timmy.right(51.42)


def octagon():
    timmy.forward(100)
    timmy.right(45)


def nonagon():
    timmy.forward(100)
    timmy.right(40)


def decagon():
    timmy.forward(100)
    timmy.right(36)


for _ in range(3):
    triangle()
for _ in range(4):
    square()
for _ in range(5):
    pentagon()
for _ in range(6):
    hexagon()
for _ in range(7):
    heptagon()
for _ in range(8):
    octagon()
for _ in range(9):
    nonagon()
for _ in range(10):
    decagon()

screen = Screen()
screen.exitonclick()


from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput("Turtle Race", "Which color turtle will win the race?")
print(choice)
screen.exitonclick()

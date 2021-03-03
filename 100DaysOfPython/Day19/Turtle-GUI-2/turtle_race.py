from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput("Turtle Race", "Which color turtle will win the race?")

tim = Turtle()
tim.penup()
tim.setposition(x=-240, y=0)
current_color = tim.color()
print(current_color)
screen.exitonclick()

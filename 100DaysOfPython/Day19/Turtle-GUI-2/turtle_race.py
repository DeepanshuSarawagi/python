from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
guess = screen.textinput("Turtle Race", "Which color turtle will win the race?")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]

tim1 = Turtle(shape="turtle")
tim1.penup()
tim1.setposition(x=-240, y=0)
tim1.color(colors[0])

tim2 = Turtle(shape="turtle")
tim2.penup()
tim2.setposition(x=-240, y=50)
tim2.color(colors[1])

tim3 = Turtle(shape="turtle")
tim3.penup()
tim3.setposition(x=-240, y=100)
tim3.color(colors[2])

tim4 = Turtle(shape="turtle")
tim4.penup()
tim4.setposition(x=-240, y=150)
tim4.color(colors[3])

tim5 = Turtle(shape="turtle")
tim5.penup()
tim5.setposition(x=-240, y=-50)
tim5.color(colors[4])

tim6 = Turtle(shape="turtle")
tim6.penup()
tim6.setposition(x=-240, y=-100)
tim6.color(colors[5])

current_color = tim1.color()
print(current_color)
screen.exitonclick()
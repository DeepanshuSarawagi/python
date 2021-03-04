from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
all_turtles = []

for _ in range(3):
    timmy = Turtle()
    timmy.color("white")
    timmy.shape("square")
    all_turtles.append(timmy)


for i in range(len(all_turtles)):
    if i == 0:
        continue
    else:
        previous_turtle = all_turtles[i-1]
        turtle = all_turtles[i]
        turtle.setx(previous_turtle.position()[0] - 20)

screen.exitonclick()

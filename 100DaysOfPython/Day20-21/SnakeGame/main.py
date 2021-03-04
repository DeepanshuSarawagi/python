from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # We are doing this to turn off the animation and have the screen pause the animation
all_turtles = []

for _ in range(3):
    timmy = Turtle()
    timmy.color("white")
    timmy.shape("square")
    timmy.penup()
    all_turtles.append(timmy)


for i in range(len(all_turtles)):
    if i == 0:
        continue
    else:
        previous_turtle = all_turtles[i-1]
        turtle = all_turtles[i]
        turtle.setx(previous_turtle.position()[0] - 20)

game_is_on = True

while game_is_on:
    screen.update()  # Turning back the animation once all the segments of snake i.e; once all the turtles
    # are created and ready to move
    time.sleep(0.1)
    for turtle in all_turtles:
        turtle.forward(20)


screen.exitonclick()

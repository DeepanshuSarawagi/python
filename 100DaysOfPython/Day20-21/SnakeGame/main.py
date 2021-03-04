from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
all_turtles = []

# timmy = Turtle()
# timmy.color("white")
# timmy.shape("square")
# timmy.setposition(x=0, y=0)
#
# timmy1 = Turtle()
# timmy1.color("white")
# timmy1.shape("square")
# timmy1.setposition(x=timmy.position()[0] - 10, y=0)
#
# timmy2 = Turtle()
# timmy2.color("white")
# timmy2.shape("square")
# timmy2.setposition(x=timmy1.position()[0] - 10, y=0)

for _ in range(3):
    timmy = Turtle()
    timmy.color("white")
    timmy.shape("square")
    all_turtles.append(timmy)

# timmy = all_turtles[0]
# timmy1 = all_turtles[1]
# timmy2 = all_turtles[2]
# timmy1.setx(timmy.position()[0] - 20)
# timmy2.setx(timmy1.position()[0] - 20)

for i in range(len(all_turtles)):
    if i == 0:
        continue
    else:
        previous_turtle = all_turtles[i-1]
        turtle = all_turtles[i]
        turtle.setx(previous_turtle.position()[0] - 20)



screen.exitonclick()

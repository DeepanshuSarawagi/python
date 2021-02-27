import turtle

timmy = turtle.Turtle()  # Constructed a New turtle object of class Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
my_screen = turtle.Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)
my_screen.exitonclick()


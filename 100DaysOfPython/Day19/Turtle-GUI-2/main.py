from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


screen.listen()  # In order for our turtle to listen to the screen events, we need to call this screen method

screen.onkey(fun=move_forward, key="Up")  # The Screen.onkey() method accepts two arguments, 1. Function  and 2. Kwy.
# We need to ensure that when we pass a function as an argument, it is coded without parentheses. Passing the function
# with parentheses calls the function immediately, instead we want it listen to an event and call the function when an
# event occurs. Like for example, in our case, when a key is presses.

screen.exitonclick()

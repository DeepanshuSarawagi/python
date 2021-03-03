from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_screen():
    tim.reset()


def draw_circle():
    tim.circle(radius=100, extent=10)


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="Right", fun=draw_circle)


screen.exitonclick()

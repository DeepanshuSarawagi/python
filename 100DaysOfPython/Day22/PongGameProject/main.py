from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle()
screen.listen()

screen.onkey(key="Up", fun=right_paddle.move_paddle_up)
screen.onkey(key="Down", fun=right_paddle.move_paddle_down)

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()

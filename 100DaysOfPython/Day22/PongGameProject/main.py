from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

screen.listen()

screen.onkey(key="Up", fun=right_paddle.move_paddle_up)
screen.onkey(key="Down", fun=right_paddle.move_paddle_down)
screen.onkey(key="w", fun=left_paddle.move_paddle_up)
screen.onkey(key="s", fun=left_paddle.move_paddle_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

screen.exitonclick()

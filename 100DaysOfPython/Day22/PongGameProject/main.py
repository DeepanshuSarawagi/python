from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=right_paddle.move_paddle_up)
screen.onkey(key="Down", fun=right_paddle.move_paddle_down)
screen.onkey(key="w", fun=left_paddle.move_paddle_up)
screen.onkey(key="s", fun=left_paddle.move_paddle_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320 or ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()

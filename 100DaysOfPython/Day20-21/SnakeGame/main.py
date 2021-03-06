from turtle import Screen
import time
import snake
import food


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # We are doing this to turn off the animation and have the screen pause the animation
snake = snake.Snake()
food = food.Food()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True

while game_is_on:
    screen.update()  # Turning back the animation once all the segments of snake i.e; once all the turtles
    # are created and ready to move
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

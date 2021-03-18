from turtle import Screen
import time
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)  # We are doing this to turn off the animation and have the screen pause the animation
snake = snake.Snake()
food = food.Food()
s = scoreboard.Scoreboard()
score = s.score

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

game_is_on = True

while game_is_on:
    screen.update()  # Turning back the animation once all the segments of snake i.e; once all the turtles
    # are created and ready to move
    if len(snake.all_snakes) < 7:
        time.sleep(0.3)
        snake.move()
    elif len(snake.all_snakes) < 12:
        time.sleep(0.2)
        snake.move()
    elif len(snake.all_snakes) < 15:
        time.sleep(0.1)
        snake.move()
    else:
        time.sleep(0.09)
        snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        # score += 1
        s.increase_score()
        food.refresh()
        snake.extend_snake()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 298 or snake.head.ycor() < -298:
        # s.game_over()
        # game_is_on = False
        s.reset()
        snake.reset()

    # Detect collision with snake's tail
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 15:
            # s.game_over()
            # game_is_on = False
            s.reset()
            snake.reset()


screen.exitonclick()

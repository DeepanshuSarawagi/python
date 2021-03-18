from turtle import Turtle

MOVE_DISTANCE = 20
ANGLE = 90
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.all_snakes = []
        self.initialise_snake_body()
        self.head = self.all_snakes[0]

    def create_snake_body(self):
        for _ in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.shape("square")
            timmy.penup()
            self.all_snakes.append(timmy)

    def snake_position(self):

        for i in range(len(self.all_snakes)):
            if i == 0:
                continue
            else:
                previous_turtle = self.all_snakes[i - 1]
                turtle = self.all_snakes[i]
                turtle.setx(previous_turtle.position()[0] - 20)

    def initialise_snake_body(self):
        self.create_snake_body()
        self.snake_position()

    def extend_snake(self):
        last_segment = self.all_snakes[-1]
        position = last_segment.position()
        timmy = Turtle()
        timmy.color("white")
        timmy.shape("square")
        timmy.penup()
        timmy.goto(position)
        self.all_snakes.append(timmy)

    def move(self):

        for turtle_num in range(len(self.all_snakes) - 1, 0, -1):
            new_x = self.all_snakes[turtle_num - 1].xcor()
            new_y = self.all_snakes[turtle_num - 1].ycor()
            self.all_snakes[turtle_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for snake in self.all_snakes:
            snake.goto(1000, 1000)
        self.all_snakes.clear()
        self.initialise_snake_body()
        self.head = self.all_snakes[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

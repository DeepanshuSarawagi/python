from turtle import Turtle


class Snake:

    def __init__(self):
        self.all_turtles = []

    def create_snake_body(self):
        for _ in range(3):
            timmy = Turtle()
            timmy.color("white")
            timmy.shape("square")
            timmy.penup()
            self.all_turtles.append(timmy)
        print(self.all_turtles)

    def snake_position(self):

        for i in range(len(self.all_turtles)):
            if i == 0:
                continue
            else:
                previous_turtle = self.all_turtles[i - 1]
                turtle = self.all_turtles[i]
                turtle.setx(previous_turtle.position()[0] - 20)

    def move(self):
        for turtle_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[turtle_num - 1].xcor()
            new_y = self.all_turtles[turtle_num - 1].ycor()
            self.all_turtles[turtle_num].goto(new_x, new_y)

        self.all_turtles[0].forward(20)

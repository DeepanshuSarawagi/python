from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5.0, stretch_len=1.0)
        self.penup()
        self.setposition(x_cor, y_cor)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        if self.ycor() < 230:
            self.goto(self.xcor(), new_y)

    def move_paddle_down(self):
        new_y = self.ycor() - 20
        if self.ycor() > -230:
            self.goto(self.xcor(), new_y)

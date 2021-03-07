from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1.0, stretch_len=5.0)
        self.penup()
        self.setheading(90)
        self.setposition(350, 0)

    def move_paddle_up(self):
        # y_cor = self.ycor()
        if self.ycor() < 250:
            self.forward(20)

    def move_paddle_down(self):
        # y_cor = self.ycor()
        if self.ycor() > -250:
            self.backward(20)

import pandas
import turtle

screen = turtle.Screen()
screen.title("Indian States Game")
image = "IndianStates.gif"
screen.addshape(image)
turtle.shape(image)


def get_on_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_on_click_coor)

turtle.mainloop()

import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

count = 0
answer_state = screen.textinput(title=f"{count}/50 Guess the state", prompt="What is the state name?").title()
print(answer_state)

states_data = pandas.read_csv("50_states.csv")

list_of_states = states_data.state.to_list()
print(list_of_states)

turtle.mainloop()

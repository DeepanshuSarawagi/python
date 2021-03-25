import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
answer_turtle = turtle.Turtle()
answer_turtle.hideturtle()
answer_turtle.penup()

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

states_data = pandas.read_csv("50_states.csv")

list_of_states = states_data.state.to_list()
guessed_states = []
count = 0


def print_state_on_map(state):
    answer_turtle.goto(x_pos, y_pos)
    answer_turtle.write(f"{state}", font=("Arial", 10, "normal"))


while count < 51:
    answer_state = screen.textinput(title=f"{count}/50 Guess the state", prompt="What is the state name?").title()
    print(answer_state)
    if (answer_state in list_of_states) and (answer_state not in guessed_states):
        guessed_states.append(answer_state)
        state_data = states_data[states_data.state == answer_state]
        x_pos = float(state_data.x)
        y_pos = float(state_data.y)
        print_state_on_map(answer_state)
        count += 1

turtle.mainloop()

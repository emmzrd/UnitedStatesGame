from turtle import Turtle, Screen
# from state import State
import pandas


tim = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
score = 0


def add_correct_state():
    new_state = Turtle()
    new_state.hideturtle()
    new_state.penup()
    new_state.color("Black")
    new_state.goto(x_axis, y_axis)
    new_state.write(answer_state)

def win():
    winner = Turtle()
    winner.hideturtle()
    winner.penup()
    winner.color("Black")
    winner.goto(0, 0)
    winner.write("You Win!")


data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()

game_is_on = True

while game_is_on:

    answer_state = screen.textinput(title="Guess the State." f" Score: {score}/50", prompt="What's another state's name?").title()
    print(answer_state)

    state_row = data[data.state == answer_state]
    state_row_dataframe = state_row.values.tolist()
    x_axis = int(state_row_dataframe[0][1])
    y_axis = int(state_row_dataframe[0][2])

    new_list = []
    for state in state_list:
        if state == answer_state:
            add_correct_state()
            score += 1
            state_list.remove(state)
            if score == 50:
                win()
                game_is_on = False

screen.exitonclick()

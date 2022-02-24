import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        state_data = data[data.state == answer]
        name.goto(int(state_data.x), int(state_data.y))
        name.write(answer)




from turtle import *
import pandas
loc = Turtle()
screen = Screen()
screen.title("US State Game")
image = "blank_states_img copy.gif"
screen.addshape(image)
screen.setup(800,800)
loc.shape(image)
score = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed = []
while len(guessed) < 50:
    answer_state = screen.textinput(f"{score}/50 States Correct","What's another state name").title()

    if answer_state == "Exit":
            missing_state = [state for state in all_states if state not in guessed]
            new_data = pandas.DataFrame(missing_state)
            new_data.to_csv("states_to_learn.csv")
            break
    if answer_state in all_states:
            guessed.append(answer_state)
            score += 1
            loc.penup()
            loc.hideturtle()
            state_data=data[data.state == answer_state]
            loc.goto(int(state_data.x), int(state_data.y))
            loc.write(answer_state)
            loc.pendown()
            loc.showturtle()

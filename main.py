
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"



data = pandas.read_csv('50_states.csv')




screen.addshape(image)
turtle.shape(image)

# a = data[data.state == 'Montana']
# print(a.state)
# print(a.state.item())
# print(a.state.to_list()[0])
guessed_states = []
count = 0
state_list = data.state.to_list()
while True:
    answer_state = screen.textinput(title=f"{count}/{len(data.state)} States Correct", prompt="What's  another state?")
    if answer_state == "Exit" or answer_state is None:
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        data_dict = {
            "You didn't know this states": missing_states,
        }
        df = pandas.DataFrame(data_dict)
        df.to_csv("states.csv")
        break
    elif answer_state.title() in state_list:
        guessed_states.append(answer_state.title())
        count +=1
        a = data[data['state'] == answer_state.title()]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        # t.goto(float(a.x),float(a.y))
        t.goto(a.x.item(), a.y.item())
        # t.write(a.state.to_list()[0])
        # t.goto(a.x.iloc[0], a.y.iloc[0])

        t.write(a.state.item())


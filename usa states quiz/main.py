import turtle
import pandas
file=pandas.read_csv('50_states.csv')
states=file['state'].to_list()
x=file['x'].to_list()
y=file['y'].to_list()
writer=turtle.Turtle()
writer.up()
writer.hideturtle()

writer.color('green')
writer.speed('fastest')
image = "D:/roadway to ml , all py topics/python basic to adv/25.quiz/img.gif"
screen = turtle.Screen()

screen.addshape(image)
turtle.shape(image)
for i in range(len(file['state'].to_list())):

    user_input = screen.textinput(" ", "state name:")
    if user_input is None:
        break
    user_input = user_input.title()
    for u in states:
        if user_input==u:
            ind=states.index(u)
            writer.goto(x[ind],y[ind])
            writer.write(user_input,font=('Arial',9,'normal'),align='left')
    if user_input=='Exit':
        break

            
turtle.hideturtle()

turtle.done()
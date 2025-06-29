import turtle as t
import random
screen=t.Screen()
screen.setup(width=1000,height=600)
red=t.Turtle(shape='turtle')
green=t.Turtle(shape='turtle')
blue=t.Turtle(shape='turtle')
black=t.Turtle(shape='turtle')
grey=t.Turtle(shape='turtle')
magenta=t.Turtle(shape='turtle')
red.color('red')
green.color('green')
blue.color('blue')
black.color('black')
grey.color('grey')
magenta.color('magenta')
red.up()
green.up()
blue.up()
black.up()
grey.up()
magenta.up()
bet=screen.textinput(title='place your bet' , prompt='which turtle do you want to bet on ? ,(red,green,blue,black,grey,magenta): ')
red.goto(-450,-250)
green.goto(-450,-150)
blue.goto(-450,-50)
black.goto(-450,50)
grey.goto(-450,150)
magenta.goto(-450,250)
xred=-450
xgreen=-450
xblue=-450
xblack=-450
xgrey=-450
xmagenta=-450
while True:
    red.goto(xred,-250)
    green.goto(xgreen,-150)
    blue.goto(xblue,-50)
    black.goto(xblack,50)
    grey.goto(xgrey,150)
    magenta.goto(xmagenta,250)
    xred+=random.randint(5,20)
    xgreen+=random.randint(5,20)
    xblue+=random.randint(5,20)
    xblack+=random.randint(5,20)
    xgrey+=random.randint(5,20)
    xmagenta+=random.randint(5,20)
    if red.pos()[0]>450:
        print('red won !!')
        break
    elif green.pos()[0]>450:
        print('green won !!')
        break
    elif blue.pos()[0]>450:
        print('blue won !!')
        break
    elif black.pos()[0]>450:
        print('black won !!')
        break
    elif grey.pos()[0]>450:
        print('grey won !!')
        break
    elif magenta.pos()[0]>450:
        print('magenta won !!')
        break
screen.exitonclick()
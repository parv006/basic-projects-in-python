import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
tim.speed('fastest')
for i in range(-10,11):

    for j in range(-10,11):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        tim.up()
        tim.setpos(40*j,40*i)
        tim.down()
        tim.dot(30,(r,g,b))
t.Screen()

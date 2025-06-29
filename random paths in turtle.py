import turtle as t
import random
tim=t.Turtle()
t.colormode(255)
tim.speed('fastest')
tim.pensize(8)
for i in range(900):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    mul=random.randint(1,4)
    tim.color(r,g,b)
    tim.forward(20)
    tim.right(90*mul)
import turtle as t
import random
tim=t.Turtle()
tim.pensize(1)
t.colormode(255)
tim.speed('fastest')
for i in range(360):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tim.color(r,g,b)
    tim.circle(200)
    tim.left(2)
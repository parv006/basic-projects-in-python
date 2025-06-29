from turtle import Turtle
import random
tim=Turtle()
n=3
clis=['blue','green','red','yellow','coral','brown','skyblue','black','darkgreen']
while True:
    tim.color(random.choice(clis))
    for i in range(n):
        tim.forward(10)
        tim.right(360/n)
    n+=1
    if n==100:
        break    
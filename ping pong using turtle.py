from turtle import Turtle , Screen
import random
import time
import math

class bat(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color('white')
        self.shape('square')
        self.up()
        self.shapesize(stretch_len=5)
        self.setheading(90)
        self.goto(-550,0)
        
class ball(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color('green')
        self.shape('circle')
        self.up()
        self.goto(0,0)

class side_line(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color('red')
        self.hideturtle()
        self.pensize(8)
        self.up()
        self.goto(580,380)
        self.down()
        self.color('white')
        self.goto(-580,380)
        self.color('red')
        self.goto(-580,-380)
        self.color('white')
        self.goto(580,-380)
        self.color('red')
        self.goto(580,380)
        self.up()

class midline(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.color('white')
        self.hideturtle()
        self.pensize(7)
        self.up()
        for i in range(-9,11,2):
            self.goto(0,38*i)
            self.down()
            self.goto(0,38*(i-1))
            self.up()
def predict_y(ballx, bally, angle_deg, target_x):
    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)

    if dx == 0:
        return bally  
    t = (target_x - ballx) / dx

    # y = y0 + v_y * t
    predicted_y = bally + dy * t
    predicted_y = max(-340, min(340, predicted_y)) 
    return predicted_y
def forw():             #for later mode change(easy hard etc)
    ball1.forward(5)
    

def new_theta(old_theta):
    theta_rad = math.radians(old_theta)
    val = math.cos(theta_rad) - 2 * math.sin(theta_rad)
    inner = 1 - val ** 2

    if inner < 0:
        inner = 0

    denominator = math.sqrt(inner)

    if denominator == 0:
        return (old_theta + 180) % 360 

    numerator = val * math.sin(theta_rad)
    result = math.atan(numerator / denominator)
    return math.degrees(result)
screen=Screen()
screen.bgcolor('black')
screen.setup(1200,800)
screen.tracer(0)
bat1=bat()
bat1.color('blue')
bat2=bat()
bat2.goto(550,0)
ball1=ball()
sideline1=side_line()
midline1=midline()
screen.update()

def bat2_up():
    y = bat2.ycor()
    if y < 340:
        bat2.sety(y + 20)

def bat2_down():
    y = bat2.ycor()
    if y > -340:
        bat2.sety(y - 20)
screen.listen()
screen.onkeypress(bat2_up, "Up")
screen.onkeypress(bat2_down, "Down")
thetai=random.randint(1,4)
if thetai==0:
    thetai=random.randint(1,4)
for rounds in range(1,6):
    ball1.setheading(thetai)
    old_theta=thetai
    score1=0
    score2=0
    while True:
        forw()
        if ball1.ycor()>=380 or ball1.ycor()<=-380:
            ball1.setheading(-1*ball1.heading())
            old_theta=ball1.heading()
            predicted_y = predict_y(ball1.xcor(), ball1.ycor(), old_theta, -550)
            bat1.sety(predicted_y)
            screen.update()
        if -560 < ball1.xcor() < -540:
            if abs(bat1.ycor() - ball1.ycor()) < 55:
                # ball hits bat1 (left bat)
                
                angle = new_theta(old_theta)
                 # reflect horizontally
                ball1.setheading(angle + (bat1.ycor() - ball1.ycor()))
                old_theta = ball1.heading()
                
            else:
                score2 += 1
                print('bot +1')
                break
        if 540 < ball1.xcor() < 560:
            if abs(bat2.ycor() - ball1.ycor()) < 55:
                # ball hits bat2
                angle = new_theta(old_theta)
                if ball1.xcor() > 0:
                    angle=((180-angle))
                ball1.setheading(angle + (bat2.ycor() - ball1.ycor()))
                old_theta = ball1.heading()
                predicted_y = predict_y(ball1.xcor(), ball1.ycor(), old_theta, -550)
                bat1.sety(predicted_y)
            else:
             
                score1 += 1
                print('bot +1')
                break
       
        screen.update()
        time.sleep(0.005)
    
screen.mainloop()

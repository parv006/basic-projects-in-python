import turtle as t
tim=t.Turtle()
screen=t.Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def rotate_clockwise():
    tim.right(5)
def rotate_counterclockwise():
    tim.left(5)       
def clearall():
    tim.clear()
    tim.home()    
def draw_arc():
    tim.circle(100,50,100)
tim.speed('fastest')    
screen.listen()
screen.onkey(key='w' , fun=move_forward)
screen.onkey(key='s' , fun=move_backward)
screen.onkeypress(key='w',fun=move_forward)
screen.onkeypress(key='d',fun=rotate_clockwise)
screen.onkeypress(key='a',fun=rotate_counterclockwise)
screen.onkeypress(key='s',fun=move_backward)
screen.onkey(key='c',fun=clearall)
screen.onkey(key='o', fun=draw_arc)


screen.exitonclick()
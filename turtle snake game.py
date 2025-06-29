import turtle as t
import random
import time
screen=t.Screen()
screen.setup(1300,1000)
screen.bgcolor('black')
screen.tracer(0)
coord=[(0,0),(-10,0),(-20,0)]
seg=[]
for f in coord:
    newseg=t.Turtle(shape='square')
    newseg.color("white")
    newseg.up()
    newseg.goto(x=f,y=None)
    newseg.speed('slowest')
    seg.append(newseg)
   
screen.update()
def move_foreward():
    for i in seg:
        i.forward(10)

       
segh=[]
for iter2 in seg:
    segh.append(iter2.heading())  
def move_right():
    global segh  
    global iter3
    for _ in seg:
        for iter1 in segh:
            _.setheading(iter1+90)            
        move_foreward()
        screen.update()
        time.sleep(0.07)
    for iter3 in range(len(segh)):
        segh[iter3]+=90
        
    
def move_left():
    global segh 
    global iter5
    for __ in seg:
        for iter4 in segh:
            __.setheading(iter4-90)            
        move_foreward()
        screen.update()
        time.sleep(0.07)
    for iter5 in range(len(segh)):
        segh[iter5]-=90


foodt=t.Turtle(shape='circle')  
foodt.color('blue')
foodt.up()
foodt.goto(random.randint(-500,500),random.randint(-400,400))
screen.update()
mouth=seg[0]
foodp=list(foodt.pos())
score=0

def foodseg():
    global seg
    global foodt
    global score
    global food_seg
    global segh
    global foodp
    global food
    food=True
    seg1_coord=list(mouth.pos())
    # print('yes')
    if int(abs(seg1_coord[0]-list(foodt.pos())[0]))<30 and (abs(seg1_coord[1]-list(foodt.pos())[1]))<30:
        score+=1
        print('ate')
        food=False
    if food==False:
        foodp=foodt.goto(random.randint(-500,500),random.randint(-400,400))
        print(foodt.pos())
        food_seg=t.Turtle(shape='square')
        food_seg.color('white')
        food_seg.up()
        print(food_seg.pos(),seg[-1].pos())
        if seg[-1].heading()==0 or seg[-1].heading()%360==0:
            food_seg.goto(list(seg[-1].pos())[0]-10,list(seg[-1].pos())[1])
        elif seg[-1].heading()%90==0 and seg[-1].heading()%180!=0 and seg[-1].heading()%270!=0 and seg[-1].heading()%360!=0:
            food_seg.goto(list(seg[-1].pos())[0],list(seg[-1].pos())[1]-10)
        elif seg[-1].heading()%180==0 and seg[-1].heading()%270!=0 and seg[-1].heading()%360!=0:
            food_seg.goto(list(seg[-1].pos())[0]+10,list(seg[-1].pos())[1])
        elif seg[-1].heading()%270==0 and seg[-1].heading()%360!=0:
            food_seg.goto(list(seg[-1].pos())[0],list(seg[-1].pos())[1]+10)
        food_seg.setheading(seg[-1].heading())
        seg.append(food_seg)
        print(food_seg.pos(),seg[-1].pos())
        segh.append(seg[-1].heading())
        screen.update()

writer = t.Turtle()
writer.hideturtle()      
writer.penup()         
is_lost=False
def game_over():
    global is_lost
    
    if list(seg[0].pos())[0]<-600 or list(seg[0].pos())[0]>600 or list(seg[0].pos())[1]<-500 or list(seg[0].pos())[1]>500:
        writer.goto(0, 450)      
        writer.clear()  
        writer.color("red")  
        writer.write(f"you lost :( ", align="center", font=("Arial", 24, "normal"))
        screen.update()
        is_lost=True  
          
        
def score_update():
    if food==False:    
        writer.clear()  
        writer.goto(0, 450)      
        writer.color("lightgreen")  
        writer.write(f"score: {score}", align="center", font=("Arial", 24, "normal"))
        screen.update()
gamemodeemh=input('which gamemode do you want ? easy medium or hard : ')  
gamemodeemh=gamemodeemh.title()   
tick=0.05   
if gamemodeemh=='Easy':
    tick=0.08
elif gamemodeemh=='Medium':
    tick=0.05
elif gamemodeemh=='Hard':
    tick=0.03        

while True:
    if is_lost==True:
        game_over()
        break
    screen.listen()
    move_foreward()
    foodseg()
    score_update()
    screen.update()
    if is_lost==True:
        game_over()
        break
    screen.onkey(key='d',fun=move_right)
    foodseg()
    score_update()
    screen.update()
    if is_lost==True:
        game_over()
        break
    screen.onkey(key='a',fun=move_left)
    foodseg()
    score_update()
    screen.update()
    if is_lost==True:
        game_over()
        break
    time.sleep(tick)

screen.exitonclick()
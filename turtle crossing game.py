import turtle as t
import random
import time

screen=t.Screen()
screen.setup(1200,800)
screen.tracer(0)
screen.bgcolor('lightblue')
draw=t.Turtle()
draw.color('black')
draw.pensize(10)
draw.hideturtle()
draw.up()
draw.goto(550,300)
draw.down()

draw.goto(-600,300)
draw.goto(-550,300)
draw.goto(-550,400)
draw.goto(-550,-400)
draw.goto(-550,-300)
draw.goto(-600,-300)
draw.goto(600,-300)
draw.goto(550,-300)
draw.goto(550,-400)
draw.goto(550,400)
draw.goto(550,300)
draw.goto(600,300)
col=['blue','green','red','magenta','yellow','darkblue','grey','violet','purple']

lanes_y = [250, 150, 50, -50, -150, -250]  # 6 lanes, evenly spaced
cars = []
num_cars_per_lane = 6  # Fewer cars for more space between

# Create cars for each lane with more spacing for turtle crossing
for lane in lanes_y:
    x_positions = [600 - i * (1200 // (num_cars_per_lane - 1)) for i in range(num_cars_per_lane)]
    for start_x in x_positions:
        car = t.Turtle()
        car.color(random.choice(col))
        car.up()
        car.shape('square')
        car.shapesize(stretch_len=2)
        car.hideturtle()
        car.goto(start_x, lane)
        car.showturtle()
        cars.append(car)

screen.update()
screen.tracer(0)

# Player turtle setup
player = t.Turtle()
player.shape('turtle')
player.color('black')
player.up()
player.goto(0, -350)
player.setheading(90)

# Scoreboard setup
score = 0
score_writer = t.Turtle()
score_writer.hideturtle()
score_writer.up()
score_writer.color('black')
score_writer.goto(-580, 350)
score_writer.write(f"Score: {score}", font=("Arial", 24, "bold"))

def update_scoreboard():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 24, "bold"))

def move_up():
    if player.ycor() < 380:
        player.sety(player.ycor() + 40)

screen.listen()
screen.onkeypress(move_up, "Up")

# Collision detection function
def is_collision(t1, t2):
    return t1.distance(t2) < 35

car_speed = 2  # Initial car speed

# Main game loop
while True:
    for car in cars:
        x, y = car.position()
        car.setx(x - random.uniform(car_speed, car_speed + 2))
        if car.xcor() < -600:
            car.setx(random.randint(600, 1200))
        # Collision detection
        if is_collision(player, car):
            player.goto(0, -350)
            score = 0
            car_speed = 2  # Reset speed on collision
            update_scoreboard()
            time.sleep(0.5)
    # Check if player reached the top
    if player.ycor() > 290:
        score += 1
        car_speed += 0.3  # Increase car speed
        update_scoreboard()
        player.goto(0, -350)
        time.sleep(0.3)
    screen.update()
    time.sleep(0.003)

screen.mainloop()
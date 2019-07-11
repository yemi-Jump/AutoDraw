import turtle
import math
import ast
import numpy as np


with open('output.txt', 'r') as f:
    data = ast.literal_eval(f.read()) # turns text into data type

storage = []
strt_speed = 5.5  # speed of straight line
tlt_speed = 6 # speed of titlted line

playground = turtle.Screen()

playground.bgcolor("black")
playground.screensize(4000, 4000)
playground.title("Auto Draw Test")

tony = turtle.Turtle() # me ;)
tony.color("white", "cyan")


# predicts the angle between two points because straight lines are too fast and cant be picked up in time
def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    between = round(np.rad2deg((ang1 - ang2) % (2 * np.pi)))
    print("Angle between: ", between)

    if between == 0:
        tony.speed(tlt_speed)
        print("straight")
    elif 10 > between > 0:
        tony.speed(strt_speed)
        print("straight")
    elif 95 > between > 85:
        tony.speed(strt_speed)
        print("straight")
    elif 185 > between > 175:
        tony.speed(strt_speed)
        print("straight")
    elif between == 360:
        tony.speed(strt_speed)
        print("straight")
    elif 360 > between > 355:
        tony.speed(strt_speed)
        print("straight")
    else:
        tony.speed(tlt_speed)
        print("not straight at: ", between)


# add position coordinates to storage list
def save_pos():
    storage.append(tony.pos())


# checks storage every 100 milliseconds
def check_storage():
    if len(storage) % 2 == 0 < 3:
        angle_between(storage[0], storage[1])
    elif len(storage) == 3:
        del storage[0], storage[1]
    elif len(storage) >= 4:
        del storage[:]
    elif len(storage) == 0:
        pass

# checks whether tony is at a position in data
def on_canvas():
    position = tony.pos()
    if position in data:
        tony.pendown()
    else:
        tony.penup()


for z in data:
    playground.ontimer(on_canvas, 1) # change after detecting straight lines
    playground.ontimer(save_pos, 100)
    playground.ontimer(check_storage, 100)
    tony.goto(z) # sends tony to location in data

turtle.done()

# if going in a straight line slow down so that program can catch up
# add feature that writes words
# add GUI
# tweak angle detection
# scale image based on size

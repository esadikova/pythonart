import turtle
import random

colors = ['DarkCyan','BlueViolet', 'dark slate blue', 'salmon', 'medium spring green', 'cyan', 'deep pink']

t=turtle.Pen()
t.speed(0)

turtle.bgcolor('black')

for i in range(15):
    x= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    y= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    size=random.randint(10,160)
    color = random.choice(colors)

    t.penup()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color)
    t.begin_fill()
    t.pendown()

    for j in range(4):
        t.forward(size)
        t.left(200)
        t.forward(size)
        t.left(70)
        
    t.end_fill()

turtle.clearscreen() 

from turtle import *
from random import randint

colors = ['DarkCyan','BlueViolet', 'firebrick', 'salmon']

t=Turtle()
t.screen.bgcolor("black")
t.hideturtle()

x = 1
t.speed(0)
while x < 60:
 t.color(random.choice(colors))
 t.fd(50 + x)
 t.rt(95)
 x = x+1
 
turtle.clearscreen()

t=Turtle()
t.screen.bgcolor("black")
t.speed(0)
t.width(10)
 
def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(colors))
        random.choice([right,left])
        t.fd(distance)
 
 
 
random_drawing(100,random.randint(0,100))



import turtle 
import random

colors = ['white', 'white smoke', 'gainsboro', 'light gray', 'dark gray','gray']

t=turtle.Pen()

t.screen.bgcolor("black")
t.speed(0)
t.hideturtle()

for i in range(150):
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

    for j in range(7):
        t.forward(size)
        t.left(random.randint(0,360))
        t.forward(size)
        t.left(random.randint(0,360))
        
    t.end_fill()
#end of background

colors2 = ['medium blue', 'medium violet red', 'cornflower blue', 'deep pink', 'spring green', 'salmon']

def mycircle(red, green, blue):
	t.color(random.choice(colors2))
	t.begin_fill()
	x = random.randint(10,100)
	t.circle(x) # draw a circle of random radius
	t.end_fill()
	t.up() # pick up pen
	y = random.randint(0,360)
	t.seth(y) # set heading to random direction
	# t.xcor() is turtle's x; t.ycor() is turtle's y
	if t.xcor() < -300 or t.xcor() > 300:
		t.goto(0, 0) # this is the center 
	elif t.ycor() < -300 or t.ycor() > 300:
		t.goto(0, 0) # this is the center 
	z = random.randint(100,300)
	t.forward(z) # move a random number of pixels
	t.down() # pen down

for i in range(0, 15):
	a = random.randint(0,100)/100.0
	b = random.randint(0,100)/100.0
	c = random.randint(0,100)/100.0
	mycircle(a, b, c) # feed a random color to the function

#stars
for i in range(15):
    x= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    y= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    size=random.randint(10,160)
    color2 = random.choice(colors2)

    t.penup()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color2)
    t.begin_fill()
    t.pendown()

    for j in range(4):
        t.forward(size)
        t.left(200)
        t.forward(size)
        t.left(70)
        
    t.end_fill()


    
"""
dots
t.speed(0)
t.hideturtle()

dot_distance = 25
width = 3
height = 3

colors2 = ['medium blue', 'medium violet red', 'cornflower blue', 'deep pink', 'spring green']

#t.penup()
#t.left(90)
#t.forward(300)
#t.left(90)
#t.forward(320)
#t.left(180)

for y in range(height):
    for i in range(width):
        t.dot(20,random.choice(colors2))
        t.forward(dot_distance)
    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)
   
turtle.done()

#spiralbelow

from turtle import *
from random import randint

colors2 = ['medium blue','deep sky blue', 'dark slate blue', 'light cyan']

t=Turtle()
t.screen.bgcolor("black")
t.pensize(1)

x = 1
t.speed(0)
while x < 400:
 t.color(random.choice(colors2))
 t.fd(50 + x)
 t.rt(91)
 x = x+1


#stars I'm pretty sure
colors2 = ['DarkCyan','BlueViolet', 'dark slate blue', 'salmon', 'medium spring green', 'cyan', 'deep pink']

t=turtle.Pen()
t.speed(0)

turtle.bgcolor('black')

for i in range(15):
    x= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    y= random.randrange(-turtle.window_width()/2, turtle.window_width()/2)
    size=random.randint(10,160)
    color2 = random.choice(colors2)

    t.penup()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color2)
    t.begin_fill()
    t.pendown()

    for j in range(4):
        t.forward(size)
        t.left(200)
        t.forward(size)
        t.left(70)
        
    t.end_fill()

def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(colors))
        random.choice([right,left])
        t.fd(100)

    t.penup()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color)
    t.begin_fill()
    t.pendown()
 
random_drawing(100,100)
 

for i in range(150):
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

#random lines

def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(colors2))
        random.choice([right,left])
        t.fd(100)

    t.penup()
    t.setpos(x,y)
    t.left(random.randint(0,360))
    t.color(color)
    t.begin_fill()
    t.pendown()
 
random_drawing(100,100)
"""

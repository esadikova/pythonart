import turtle 
import random

colors = ['DarkCyan','BlueViolet', 'firebrick', 'dark slate blue', 'salmon', 'medium spring green', 'cyan', 'white smoke', 'deep pink']

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

    for j in range(4):
        t.forward(size)
        t.left(random.randint(0,360))
        t.forward(size)
        t.left(random.randint(0,360))
        
    t.end_fill()


"""
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
"""

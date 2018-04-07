import turtle
import random


colors=['white', 'white smoke', 'gainsboro', 'light gray', 'dark gray','gray']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range (360) :
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

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

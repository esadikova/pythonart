import turtle 
import random

painter = turtle.Turtle()

t=turtle.Pen()

t.screen.bgcolor("black")
t.speed(0)
t.hideturtle()

painter.pencolor("blue")
for i in range(50):
    painter.forward(150)
    painter.left(123) 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()

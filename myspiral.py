import turtle
import random

from turtle import *
from random import randint

colors = ['DarkCyan','BlueViolet', 'firebrick', 'salmon']

t=Turtle()
t.screen.bgcolor("black")
t.pensize(5)

x = 1
t.speed(0)
while x < 400:
 t.color(random.choice(colors))
 t.fd(50 + x)
 t.rt(95)
 x = x+1
 
exitonclick()

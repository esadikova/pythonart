from turtle import Turtle
import random

def isInScreen(w, t):
    if random.random() > 0.1:
        return True
    else:
        return False

colors = ['DarkCyan','BlueViolet', 'firebrick', 'dark slate blue', 'salmon', 'medium spring green', 'cyan', 'white smoke', 'deep pink']

t=Turtle()
t.screen.bgcolor("black")
t.speed(0)
t.width(7)
 
def random_drawing(turns,distance):
    for x in range(turns):
        right=t.right(random.randint(0,360))
        left=t.left(random.randint(0,360))
        t.color(random.choice(colors))
        random.choice([right,left])
        t.fd(distance)
 
 
 
random_drawing(100,random.randint(0,100))

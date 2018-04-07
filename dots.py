import turtle 

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

turtle.bgcolor('black')

dot_distance = 25
width = 26
height = 25

t.penup()
t.left(90)
t.forward(300)
t.left(90)
t.forward(320)
t.left(180)

for y in range(height):
    for i in range(width):
        t.dot(20,'cyan')
        t.forward(dot_distance)
    t.backward(dot_distance * width)
    t.right(90)
    t.forward(dot_distance)
    t.left(90)

turtle.clearscreen()    
turtle.done()

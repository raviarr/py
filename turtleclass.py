from turtle import Turtle, Screen

import turtle
loadWindow = turtle.Screen()
turtle.speed(11)

for i in range(50):
    turtle.circle(1*i)
    turtle.circle(-1*i)
    turtle.left(i)

turtle.exitonclick()    

import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(280):
    t.pencolor(colors[x%6])
    t.width(x//100 + 1)
    t.forward(x)
    t.left(59)

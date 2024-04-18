from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(150)
timmy.left(60)
timmy.forward(150)
timmy.left(60)
timmy.forward(150)
timmy.left(60)
timmy.forward(150)
timmy.left(60)
timmy.forward(150)
timmy.left(60)
timmy.forward(150)

tommy = Turtle()
tommy.shape("circle")
tommy.color("blue")
tommy.forward(100)
tommy.left(90)
tommy.forward(100)
tommy.left(90)
tommy.forward(100)
tommy.left(90)
tommy.forward(100)
tommy.left(90)


newScreen = Screen()
print(newScreen.canvheight)
newScreen.exitonclick()

import turtle 
star = turtle.Turtle()

star.right(75)
star.forward(100)

for i in range(4):
    star.right(144)
    star.forward(100)

turtle.done()    


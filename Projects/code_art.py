#Beginning

import turtle
import time

#Setting up the turtle

t1 = turtle
t1.penup()
t1.speed(0)
t1.width(4)
t1.goto(-65,-50)
t1.pendown()

#Shape making below this message

#Moving and rotating the pentagon

colors = ["blue","cyan","black"]
for i in range(200):
    t1.color(colors[i % 3])
    t1.forward(100+i)
    t1.left(73)
    t1.left(90)
    t1.forward(100)
    t1.forward(-100)
    t1.left(270)
t1.penup()

#Cool logo

t1.goto (-10,60)
t1.pendown()
for i in range(4):
    t1.color("grey")
    t1.forward(50)
    t1.left(45)
    t1.forward(20)
    t1.left(45)
    t1.left(90)
    t1.forward(60)
    t1.forward(-50)
    t1.left(270)

#Writing CT8

t1.penup()
t1.goto(-50,0)
t1.pendown()
t1.color("red")
t1.write("CT8",font = ("Arial", 25, "normal"))

#End
t1.penup()
t1.goto(9999999,9999999999)
t1.exitonclick()

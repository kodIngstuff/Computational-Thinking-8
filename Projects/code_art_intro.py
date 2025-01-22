# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()

for i in range (5) :
    t.forward(100)
    t.left(72)
t.pendown()

t.penup()
t.goto(100,100)
t.color("green")
t.pendown()
for i in range (4) :
    t.forward(100)
    t.left(90)

t.penup()
t.goto(0,0)
t.color("yellow")
t.pendown()
for i in range (3) :
    t.forward(200)
    t.left(120)

t.penup()
t.goto(-200,-200)
t.color("purple")
t.pendown()
for i in range (6) :
    t.forward(50)
    t.left(60)

t.penup()
t.goto(-150,150)
t.color("purple")
t.pendown()
t. forward (50)
for i in range (2):
    t. left(90)
    t. forward (100)
    t. left (90)

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
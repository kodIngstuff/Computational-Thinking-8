import turtle
t = turtle.Turtle()

# setup
t.speed(0)
turtle.Screen().bgcolor("light blue")
height=50


# stripes

# move to stripe 1
t.penup()
t.goto(-250, -100)

# stripe 1
t.pendown()
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()
t.penup()


# move to stripe 2
t.goto(-250, -50)

# stripe 2
t.pendown()
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()
t.penup()

# move to stripe 3
t.goto(-250, 0)

# stripe 3
t.pendown()
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()
t.penup()

# move to stripe 4
t.goto(-250, 50)

# stripe 4
t.pendown()
t.color("white")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()
t.penup()

# move to stripe 5
t.goto(-250, 100)

# stripe 5
t.pendown()
t.color("red")
t.begin_fill()
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.forward(500)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()
t.penup()


# blue square
t.pendown()
t.goto(-250, 50)
t.color("blue")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()
t.penup()

# star
t.setheading(180)
t.goto(-175,105)
t.pendown()
t.color("white")
t.begin_fill
for i in range (5):
    t.forward(50)
    t.left(145)
t.end_fill
t.penup()
t.goto(999,999)
turtle.exitonclick()


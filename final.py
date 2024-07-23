import turtle

# Setup turtle
turtle.speed(0)
turtle.pensize(5)
turtle.colormode(255)

# Ask the user how many layers of art there should be
layers = int(input("How many layers should there be? (1-6): "))

# Initial values
radius = 80
step = 3
r, g, b = 255, 0, 0

# Function to draw the shapes in layers
for i in range(layers):
    for j in range(36):
        turtle.penup()
        turtle.color(r, g, b)
        turtle.forward(radius)
        turtle.pendown()
        turtle.circle(20, 360, step)
        turtle.penup()
        turtle.backward(radius)
        turtle.left(10)
    step += 1
    radius += 20
    r = max(0, r - 55)
    g = min(255, g + 20)
    b = min(255, b + 25)

# Draw the number of layers in the center
turtle.penup()
turtle.setheading(90)
turtle.goto(0, -20)

# Functions to draw the numbers
def one():
    turtle.pendown()
    turtle.forward(60)
    turtle.backward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.penup()

def two():
    turtle.pendown()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()

def three():
    turtle.pendown()
    for _ in range(2):
        turtle.forward(30)
        turtle.backward(30)
        turtle.right(90)
        turtle.forward(30)
        turtle.left(90)
    turtle.forward(30)
    turtle.penup()

def four():
    turtle.pendown()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.backward(60)
    turtle.right(90)
    turtle.penup()

def five():
    turtle.pendown()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.penup()

def six():
    turtle.pendown()
    turtle.circle(15, 360, 6)
    turtle.penup()

# Draw the number of layers
if layers == 1:
    one()
elif layers == 2:
    two()
elif layers == 3:
    three()
elif layers == 4:
    four()
elif layers == 5:
    five()
elif layers == 6:
    six()

turtle.hideturtle()
turtle.done()

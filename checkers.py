import turtle

# Function to draw a square and fill it with the current color
def make_square():
    turtle.pendown()
    for _ in range(4):
        turtle.forward(40)
        turtle.right(90)
    turtle.forward(40)

# Function to assign color and draw the square based on color_value
def assign_color(color_value):
    if color_value % 2 == 0:
        turtle.color("black")
    else:
        turtle.color("red")
    turtle.begin_fill()
    make_square()
    turtle.end_fill()

# Function to move the turtle back to the start of the next row
def move_back_to_row():
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(180)

# Setup turtle
turtle.speed(0)
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
color_value = 0

# Loop to draw the grid of squares
for _ in range(10):
    for _ in range(10):
        assign_color(color_value)
        color_value += 1
    move_back_to_row()
    color_value += 1

turtle.hideturtle()
turtle.done()

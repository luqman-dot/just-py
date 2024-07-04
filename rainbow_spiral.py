import turtle
import colorsys

# Setup the turtle
turtle.speed(0)  # Fastest drawing speed
turtle.pensize(2)  # Set pen size to 2
turtle.bgcolor("black")  # Set background color to black

# Function to draw a filled square
def square():
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(400)
        turtle.left(90)
    turtle.end_fill()

# Function to draw a triangle
def triangle(size):
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)

# Function to draw a hexagon
def hexagon(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.left(60)

# Function to draw circles in a spiral
def draw_spiral_circles(num):
    for i in range(2000):
        color = colorsys.hsv_to_rgb(i / 2000, 1.0, 1.0)  # Gradient color
        turtle.color(color)
        turtle.circle(i / 1000 + 1, 360, 6)
        turtle.forward(i / 10)
        turtle.right(num)

# Set initial position for the square
turtle.penup()
turtle.setposition(-200, -200)
turtle.pendown()
turtle.color("white")
square()

# Move to the center for drawing patterns
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()

# Draw spiral circles
num = 59  # Change this value to see different patterns
draw_spiral_circles(num)

# Draw additional shapes
turtle.penup()
turtle.setposition(100, 100)
turtle.pendown()
turtle.color("cyan")
triangle(100)

turtle.penup()
turtle.setposition(-150, -150)
turtle.pendown()
turtle.color("magenta")
hexagon(100)

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()

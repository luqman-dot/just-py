import turtle

# Setup the turtle
turtle.speed(0)  # Fastest drawing speed
turtle.pensize(3)  # Set pen size to 3

# Function to draw a filled square
def square():
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(400)
        turtle.left(90)
    turtle.end_fill()

# Colors to use in the pattern
colors = ("red", "purple", "blue", "green", "yellow", "orange")
num = 59  # Change this value to see different patterns

# Draw the background square
turtle.penup()
turtle.setposition(-200, -200)
turtle.pendown()
square()

# Move to the center for circle drawing
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown()

# Draw circles in a spiral pattern
for i in range(2000):
    turtle.color(colors[i % len(colors)])
    turtle.circle(i / 1000 + 1, 360, 6)
    turtle.forward(i / 10)
    turtle.right(num)

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()

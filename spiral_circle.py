import turtle
import random

# Setup the turtle
turtle.speed(0)  # Fastest drawing speed
turtle.bgcolor("black")  # Set background color to black

# List of colors to use in the spiral
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Set the initial position
turtle.penup()
turtle.setposition(0, 0)
turtle.pendown() # Start drawing

# Initialize parameters for the spiral
radius = 10
angle = 10
num_circles = 100

# Draw spiral circles in a loop
for i in range(num_circles):
    turtle.color(random.choice(colors))  # Change color for each circle
    turtle.circle(radius, 360)  # Draw a full circle
    turtle.right(angle)         # Change direction
    radius += 2                 # Increment radius for spiral effect

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()

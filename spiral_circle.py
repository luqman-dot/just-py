import turtle
import random

# Setup the turtle
turtle.speed(0)  # Fastest drawing speed
turtle.penup()   # Lift the pen to move without drawing

# Set the initial position
turtle.setposition(10, -10)
turtle.pendown() # Start drawing

# Draw different types of circles in a loop
for i in range(1000):
    radius = random.randint(50, 200)      # Random radius between 50 and 200
    extent = random.uniform(30, 360)      # Random extent between 30 and 360 degrees
    steps = random.randint(3, 20)         # Random number of steps between 3 and 20
    turtle.circle(radius, extent, steps)  # Draw part of a circle

# Lift the pen and move to a new position
turtle.penup()
turtle.setposition(-10, -40)

# Hide the turtle and display the result
turtle.hideturtle()
turtle.done()

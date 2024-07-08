import turtle
import random

def draw_circle(x, y, radius, color_fill, pen_size=1, pen_color="black"):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(pen_color)
    turtle.pensize(pen_size)
    if color_fill:
        turtle.begin_fill()
    turtle.circle(radius)
    if color_fill:
        turtle.end_fill()

def draw_snowman():
    turtle.speed(0)

    # Draw snowman body
    draw_circle(0, -200, 75, True, pen_color="snow")
    draw_circle(0, -50, 50, True, pen_color="snow")
    draw_circle(0, 50, 30, True, pen_color="snow")

    # Draw buttons
    turtle.right(90)
    turtle.color("black")
    turtle.pensize(3)
    for i in range(3):
        draw_circle(0, 50 - (i * 25), 2, True)

    # Draw arms
    def draw_arm(x, y, angle):
        turtle.penup()
        turtle.setposition(x, y)
        turtle.setheading(angle)
        turtle.pendown()
        turtle.color("saddlebrown")
        turtle.pensize(5)
        turtle.forward(75)
        turtle.backward(20)
        turtle.left(45)
        turtle.forward(15)
        turtle.backward(15)
        turtle.right(90)
        turtle.forward(15)
    
    draw_arm(50, 0, 150)
    draw_arm(-50, 0, 30)

    # Draw eyes
    turtle.pensize(4)
    draw_circle(10, 85, 2, True)
    draw_circle(-10, 85, 2, True)

    # Draw nose
    turtle.color("orange")
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(0, 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(25)
    turtle.left(155)
    turtle.forward(25)
    turtle.left(102)
    turtle.forward(12)
    turtle.end_fill()

    # Draw top hat
    turtle.penup()
    turtle.setposition(-25, 110)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

    # Draw scarf
    turtle.penup()
    turtle.setposition(0, 45)
    turtle.setheading(0)
    turtle.color("red")
    turtle.pendown()
    turtle.pensize(10)
    turtle.forward(30)
    turtle.backward(60)
    turtle.left(135)
    turtle.forward(45)
    turtle.right(45)

def draw_snowflakes():
    for _ in range(50):
        x = random.randint(-300, 300)
        y = random.randint(-200, 200)
        size = random.randint(2, 5)
        draw_circle(x, y, size, True, pen_color='white')

def draw_ground():
    turtle.penup()
    turtle.setposition(-400, -250)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("snow")
    turtle.pensize(20)
    turtle.forward(800)

def draw_tree(x, y):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.color("saddlebrown")
    turtle.pensize(5)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(20)
    
    turtle.color("forestgreen")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(20)
    turtle.end_fill()

def draw_forest():
    tree_positions = [(-150, -180), (-200, -150), (200, -180), (150, -150), (-100, -200)]
    for pos in tree_positions:
        draw_tree(pos[0], pos[1])

# Setup turtle
turtle.speed(0)
turtle.bgcolor("deepskyblue")

# Draw the scene
draw_ground()
draw_snowman()
draw_forest()
draw_snowflakes()

turtle.hideturtle()
turtle.done()

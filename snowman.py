import turtle

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
    turtle.bgcolor("deepskyblue")

    # Draw snowman body
    turtle.color("snow")
    turtle.begin_fill()
    draw_circle(0, -200, 75, False)
    draw_circle(0, -50, 50, False)
    draw_circle(0, 50, 30, False)
    turtle.end_fill()

    # Draw buttons
    turtle.right(90)
    turtle.color("black")
    turtle.pensize(3)
    for i in range(3):
        draw_circle(0, 50 - (i * 25), 2, False)

    # Draw arms
    def draw_arm(x, y, angle):
        turtle.penup()
        turtle.setposition(x, y)
        turtle.left(angle)
        turtle.pendown()
        turtle.color("saddlebrown")
        turtle.forward(75)
        turtle.backward(20)
        turtle.left(45)
        turtle.forward(15)
        turtle.backward(15)
        turtle.right(90)
        turtle.forward(15)

    draw_arm(50, 0, 120)
    draw_arm(-50, 0, 145)

    # Draw eyes
    turtle.pensize(4)
    draw_circle(10, 85, 2, False)
    draw_circle(-10, 85, 2, False)

    # Draw nose
    turtle.color("orange")
    turtle.pensize(1)
    turtle.penup()
    turtle.setposition(0, 70)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(155)
    turtle.forward(25)
    turtle.left(102)
    turtle.forward(12)
    turtle.end_fill()

    # Draw top hat
    turtle.penup()
    turtle.setposition(-25, 110)
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
    turtle.color("red")
    turtle.pendown()
    turtle.pensize(10)
    turtle.forward(30)
    turtle.backward(50)
    turtle.left(135)
    turtle.forward(45)

    # Draw ground
    turtle.penup()
    turtle.setposition(-200, -200)
    turtle.pendown()
    turtle.pensize(20)
    turtle.color("snow")
    turtle.right(90)
    turtle.forward(400)

def draw_snowflakes():
    snowflake_positions = [
        (-50, 150), (-140, 140), (50, 150), (140, 140),
        (-100, 100), (100, 100), (-150, 50), (150, 50),
        (-100, -50), (100, -50), (-140, -140), (140, -140)
    ]
    turtle.pensize(3)
    for pos in snowflake_positions:
        draw_circle(pos[0], pos[1], 3, True, pen_color='snow')

turtle.speed(0)
draw_snowman()
draw_snowflakes()
turtle.hideturtle()
turtle.done()

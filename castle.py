import turtle

def setup_turtle():
    turtle.speed(10)
    turtle.pensize(4)
    turtle.penup()
    turtle.setposition(0, -160)
    turtle.pendown()

def draw_base():
    turtle.color("white")
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(60)
    turtle.circle(40, 180)
    turtle.forward(60)
    turtle.end_fill()

def draw_tan_shape():
    turtle.color("tan")
    turtle.penup()
    turtle.setposition(-200, -50)
    turtle.left(180)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.right(90)
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(170)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(170)
    turtle.end_fill()

def draw_lines():
    turtle.penup()
    turtle.setposition(-130, -10)
    turtle.pendown()
    turtle.forward(140)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    for i in range(6):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(5)
        turtle.right(90)

def draw_right_lines():
    turtle.penup()
    turtle.setposition(-50, -10)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(40)
    turtle.forward(10)
    turtle.right(40)
    for i in range(9):
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)

def draw_lightblue_shape():
    turtle.penup()
    turtle.setposition(-200, -115)
    turtle.right(180)
    turtle.pendown()
    turtle.color("lightblue")
    turtle.begin_fill()
    turtle.circle(50, 80)
    turtle.left(10)
    turtle.forward(310)
    turtle.circle(50, 80)
    turtle.right(170)
    turtle.forward(85)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(70)
    turtle.end_fill()

def draw_brown_lines():
    turtle.penup()
    turtle.setposition(-42, -160)
    turtle.right(90)
    for i in range(5):
        turtle.color("tan")
        turtle.forward(85)
        turtle.right(90)
        turtle.penup()
        turtle.forward(4)
        turtle.right(90)
        turtle.pendown()
        turtle.color("brown")
        turtle.forward(85)
        turtle.left(90)
        turtle.penup()
        turtle.forward(4)
        turtle.left(90)
    turtle.setposition(-32, -160)
    turtle.pendown()
    turtle.right(90)
    turtle.color("tan")
    turtle.forward(40)
    turtle.penup()
    turtle.setposition(32, -160)
    turtle.pendown()
    turtle.right(270)
    turtle.right(90)
    turtle.color("tan")
    turtle.forward(40)

def draw_gray_lines():
    turtle.penup()
    turtle.setposition(0, -60)
    turtle.color("gray")
    turtle.pendown()
    turtle.forward(70)
    turtle.penup()
    turtle.setposition(20, -70)
    turtle.pendown()
    turtle.forward(60)
    turtle.penup()
    turtle.setposition(-20, -70)
    turtle.pendown()
    turtle.forward(60)
    turtle.left(90)
    turtle.backward(20)
    turtle.forward(82)
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(82)

def draw_tan_shapes():
    turtle.penup()
    turtle.setposition(-130, 100)
    turtle.pendown()
    turtle.color("gray")
    turtle.left(120)
    turtle.forward(70)
    turtle.color("purple")
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()
    turtle.penup()
    turtle.setposition(-172, 100)
    turtle.pendown()
    turtle.right(120)
    turtle.color("tan")
    turtle.forward(50)
    turtle.penup()
    turtle.setposition(-168, 100)
    turtle.pendown()
    turtle.forward(50)

def main():
    setup_turtle()
    draw_base()
    draw_tan_shape()
    draw_lines()
    draw_right_lines()
    draw_lightblue_shape()
    draw_brown_lines()
    draw_gray_lines()
    draw_tan_shapes()
    turtle.done()

main()

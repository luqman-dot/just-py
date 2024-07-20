import turtle

# Setup turtle
screen = turtle.Screen()
screen.title("Avenger Logos")
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(3)

def black_widow():
    pen.penup()
    pen.setposition(0, -200)
    pen.pendown()
    pen.begin_fill()
    pen.color("black")
    pen.circle(200)
    pen.end_fill()
    
    pen.penup()
    pen.setposition(0, 0)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.circle(100, steps=3)
    pen.end_fill()

    pen.penup()
    pen.setposition(0, 0)
    pen.pendown()
    pen.right(180)
    pen.color("blue")
    pen.begin_fill()
    pen.circle(100, steps=3)
    pen.end_fill()
    
    pen.penup()
    pen.setposition(0, -200)
    pen.pendown()
    pen.right(180)
    pen.pensize(10)
    pen.color("black")
    pen.circle(200)

def cap_am():
    pen.penup()
    pen.setposition(0, -150)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.circle(150)
    pen.end_fill()

    pen.left(90)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.right(90)
    pen.color("white")
    pen.begin_fill()
    pen.circle(125)
    pen.end_fill()

    pen.left(90)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.right(90)
    pen.color("red")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

    pen.left(90)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.right(90)
    pen.color("white")
    pen.begin_fill()
    pen.circle(75)
    pen.end_fill()

    pen.left(90)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.right(90)
    pen.color("blue")
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

    pen.left(90)
    pen.penup()
    pen.forward(25)
    pen.pendown()
    pen.right(90)
    pen.color("white")
    pen.begin_fill()
    for _ in range(5):
        pen.forward(40)
        pen.right(144)
    pen.end_fill()

def hawk_eye():
    circle_radius = 150
    length = 25
    colors = ["plum", "black", "plum"]

    pen.penup()
    pen.setposition(0, -150)
    pen.pendown()

    for color_choice in colors:
        pen.color(color_choice)
        pen.begin_fill()
        pen.circle(circle_radius)
        pen.end_fill()
        
        pen.left(90)
        pen.penup()
        pen.forward(length)
        pen.right(90)
        pen.pendown()
        
        circle_radius -= 25

    pen.penup()
    pen.setposition(0, 30)
    pen.pendown()
    pen.color("dark violet")
    pen.begin_fill()
    pen.left(30)
    pen.forward(60)
    pen.right(120)
    pen.forward(100)
    pen.right(60)
    pen.forward(60)
    pen.right(60)
    pen.forward(60)
    pen.right(60)
    pen.forward(100)
    pen.right(120)
    pen.forward(60)
    pen.end_fill()

# Main program
user_number = int(turtle.textinput("Avenger Logos", "Number (1-3)? "))

if user_number == 1:
    black_widow()
elif user_number == 2:
    cap_am()
elif user_number == 3:
    hawk_eye()
else:
    print("Invalid number")

# Hide turtle and display the window
pen.hideturtle()
turtle.done()

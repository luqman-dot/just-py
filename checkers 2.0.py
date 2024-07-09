import turtle

def make_square(size):
    """Draws a filled square of the given size."""
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size)

def assign_color(color_value):
    """Assigns color based on the color_value and draws the square."""
    if color_value % 2 == 0:
        turtle.color("black")
    else:
        turtle.color("white")
    turtle.begin_fill()
    make_square(40)
    turtle.end_fill()

def move_back_to_row():
    """Moves the turtle back to the start of the next row."""
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(180)

def draw_grid(rows, cols, square_size):
    """Draws a grid of alternating colored squares."""
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(-cols // 2 * square_size, rows // 2 * square_size)
    turtle.pendown()
    
    color_value = 0

    for _ in range(rows):
        for _ in range(cols):
            assign_color(color_value)
            color_value += 1
        move_back_to_row()
        color_value += 1

    turtle.hideturtle()
    turtle.done()

# Draw a 10x10 grid with each square having a size of 40 units
draw_grid(10, 10, 40)

import turtle
import random

# Initialize the turtle module
turtle.speed(0)
turtle.hideturtle()

# Function to draw an X mark
def draw_x(color="red"):
    turtle.pensize(10)
    turtle.color(color)
    for _ in range(4):
        turtle.right(45)
        turtle.forward(50)
        turtle.backward(50)
        turtle.right(45)

# Function to draw the artistic effect
def draw_artistic_effect(inner_color, outer_color, middle_color):
    turtle.pensize(1)
    for x in range(70):
        turtle.color(outer_color)
        turtle.circle(x, 180, 4)
        if x > 40:
            turtle.right(20)
        if x < 40:
            turtle.color(inner_color)
            turtle.circle(180, 360, 4)
            turtle.color(outer_color)
            turtle.right(50)
            turtle.color(middle_color)
            turtle.circle(180)

# Function to draw circles at the end
def draw_final_circles(outer_color):
    turtle.penup()
    turtle.setposition(-20, 10)
    turtle.pendown()
    turtle.color(outer_color)
    for _ in range(80):
        turtle.forward(10)
        turtle.backward(10)
        turtle.right(5)
    
    turtle.penup()
    turtle.setposition(-60, 4)
    turtle.pendown()
    turtle.pensize(10)
    turtle.right(180)
    turtle.forward(35)
    turtle.right(50)
    turtle.forward(40)

# Main script
def main():
    secret_number = random.randint(1, 10)
    
    while True:
        try:
            user_number = int(input("Guess a number from 1 to 10: "))
            if 1 <= user_number <= 10:
                break
            else:
                print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    while user_number != secret_number:
        print("Wrong guess, try again!")
        draw_x("red")
        try:
            user_number = int(input("Guess another number from 1 to 10: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    draw_x("white")
    
    inner_color = input("What color should the inner petal be? (e.g., gold, magenta, pink): ").strip().lower()
    outer_color = input("What color should the outer petal be? (e.g., gold, magenta, pink): ").strip().lower()
    middle_color = input("What color should the circle in the middle be? (e.g., gold, magenta, pink): ").strip().lower()
    
    draw_artistic_effect(inner_color, outer_color, middle_color)
    draw_final_circles(outer_color)
    turtle.done()

if __name__ == "__main__":
    main()

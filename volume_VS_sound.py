import turtle
import random

def random_movement(min_val, max_val):
    turtle.penup()
    turtle.setposition(random.randint(min_val, max_val), random.randint(min_val, max_val))
    turtle.pendown()
    turtle.forward(1)

def draw_square(size):
    turtle.penup()
    turtle.setposition(-size, -size)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size * 2)
        turtle.left(90)
    turtle.penup()

def reset_position():
    turtle.setposition(0, 0)

def particle_demo(size, color, steps, speed):
    turtle.speed(speed)
    reset_position()
    turtle.color(color)
    for _ in range(steps):
        random_movement(-size, size)
        turtle.penup()

def main():
    turtle.speed(10)
    turtle.pensize(4)

    # Draw initial boundary
    turtle.penup()
    turtle.setposition(0, -153)
    turtle.pendown()
    draw_square(150)
    reset_position()

    # Define parameters for each square and run the demo
    sizes = [150, 125, 100, 75, 50, 25, 5]
    colors = ["black", "blue", "purple", "red", "gold", "cyan", "gray"]
    speeds = [10, 9, 8, 7, 6, 5, 4]
    steps_per_size = 300

    for size, color, speed in zip(sizes, colors, speeds):
        draw_square(size)
        particle_demo(size, color, steps_per_size, speed)
        steps_per_size += 300
        turtle.pensize(4)

    # Final message
    print('As the volume of the container decreases, the energy of collisions decreases as well, due to the increased pressure and therefore reduced speed.')
    print('The particles farther out move faster as a result of the decreased pressure, but they are less likely to collide due to the increased space between each particle.')
    print('What do you think would happen if I restricted the movement of each particle to 1 unit by decreasing the volume to 1x1? How would the final box look?')

    turtle.done()

if __name__ == "__main__":
    main()

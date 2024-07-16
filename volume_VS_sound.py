import turtle
import random

def random_movement(min_val, max_val, color):
    turtle.color(color)
    turtle.penup()
    turtle.setposition(random.randint(min_val, max_val), random.randint(min_val, max_val))
    turtle.pendown()
    turtle.dot(6)

def draw_square(size, color):
    turtle.color(color)
    turtle.penup()
    turtle.setposition(-size, -size)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(size * 2)
        turtle.left(90)
    turtle.penup()
    turtle.setposition(0, 0)

def particle_demo(size, color, steps, speed):
    turtle.speed(speed)
    for _ in range(steps):
        random_movement(-size, size, color)

def main():
    turtle.speed(0)
    turtle.hideturtle()
    turtle.title("Particle Movement Simulation")

    # Parameters for each square and particle movement
    sizes = [150, 125, 100, 75, 50, 25, 5]
    colors = ["black", "blue", "purple", "red", "gold", "cyan", "gray"]
    speeds = [10, 9, 8, 7, 6, 5, 4]
    steps_per_size = 50
    increment_steps = 50

    for size, color, speed in zip(sizes, colors, speeds):
        draw_square(size, "black")
        particle_demo(size, color, steps_per_size, speed)
        steps_per_size += increment_steps

    turtle.done()
    print('As the volume of the container decreases, the energy of collisions decreases as well, due to the increased pressure and therefore reduced speed.')
    print('The particles farther out move faster as a result of the decreased pressure, but they are less likely to collide due to the increased space between each particle.')
    print('What do you think would happen if I restricted the movement of each particle to 1 unit by decreasing the volume to 1x1? How would the final box look?')

if __name__ == "__main__":
    main()

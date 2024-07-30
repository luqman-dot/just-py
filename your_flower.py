"""
the set for the real art is  
gold, magenta and pink

This script will have tracy ask the user to guess a number from 1-10, if wrong tracy will create an x Mark
until the user gets it correct, when user gets it correct tracy will ask the user 3 input questions on how
the user wants the colors, tracy will then draw the artistic effect

"""





#this sets tracy speed so the program can run faster
speed (0)


#these codes are so the program can generate a random number from 1-10 everytime so the user can guess
import random
secret_number = random.randrange(1,10)
user_number = int(input("guess a number from 1 to 10 :"))


#this while loop is so tracy knows that everytime the user guesses the number wrong she will draw an X mark
while user_number != secret_number:
    user_number = int(input("guess another number from 1 to 10 :"))
    def x():
        pensize(10)
        color("red")
        for i in range(4):
            right(45)
            forward(50)
            backward(50)
            right(45)
    x()
 
def x2():  #this function is so that when the user gets it correct tracy will draw a white x mark overlaping the red one as a symbol that they got it correct
    pensize(10)
    color("white")
    for i in range(16):
        right(45)
        forward(50)
        backward(50)
        right(45)


#Tracy will then (after user gets number correct) procede to ask the user what colors they would like on the effect


if user_number == secret_number:
    x2()
    color_choiceA = input("What color should the inner petal be?: ")
    color_choiceB = input("What color should the outer petal be?: ")
    color_choiceC = input("What color should the circle in the middle be?: ")
    color("green")
def turn(): #this function makes sure that all correspondiong colors go to each shape so the effect can come to life
    for x in range(70):
        color(color_choiceB)
        circle(x,180,4)
        if x>40:
            right(20)
        if x<40:
            color(color_choiceA)
            circle(180,360,4)
            color(color_choiceB)
            right(50)
            color(color_choiceC)
            
            circle(180)

#These command either call in the function or make sure that at the end in where tracy does a circle all spaces are filled with color
turn()
penup()
setposition(-20,10)
pendown()
color(color_choiceB)
for i in range (80):
    forward(10)
    backward(10)
    right(5)
penup()
setposition(-60,4)
pendown()
color(color_choiceB)
pensize(10)
right(180)
forward(35)
right(50)
forward(40)
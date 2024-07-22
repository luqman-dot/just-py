""" this will create a funciton that asks how many layers the user wants.
it will then create a circle of shapes starting with a triangle and 
increasing one side for each new layer"""

#sets the speed to 0
speed(0)

#puts the pen size to 5
pensize(5)

#asks the user how many layers of art there should be
layers=int(input("how many layers should there be?(1-6)"))

#sets the initial radius of the first circle to 80
radius=80
step=3
r =255
g=0
b=0

#this will as the user which color each layer should be. it also creates the 
#different layers of shapes
for i in range(layers):
    for i in range (37):
        penup()
        color((r,g,b))      
        forward (radius)
        #tracy moves forard
        pendown()
        circle (20,360,step)
        #draws the circle
        penup()
        backward (radius)
        #back to center
        left (10)
    #increases the radius of the next circle 
    step=step+1
    radius=radius+20
    r=r-55
    g=g+20
    b=b+25
    
#makes tracy face north
setheading(90)

#creates the number 1
def one():
    pendown()
    forward(30)
    backward(60)
    
#creates the number 2
def two():
    pendown()
    right(90)
    forward (30)
    left(90)
    forward (30)
    left(90)
    forward(60)
    penup()
    setposition(0,0)
    pendown()
    forward(30)
    left(90)
    forward(30)
    left(90)
    forward(60)
    
#creates the number 3
def three():
    pendown()
    right(90)
    forward (30)
    left(90)
    forward (30)
    left(90)
    forward(60)
    penup()
    setposition(0,0)
    pendown()
    right(180)
    forward(30)
    right(90)
    forward (30)
    right(90)
    forward(60)

#creates the number 4
def four():
    pendown()
    left(90)
    forward(20)
    right(90)
    forward(30)
    penup()
    setposition(0,0)
    pendown()
    right(90)
    forward(20)
    left(90)
    forward(30)
    backward(70)

#creates the number 5     
def five():
    pendown()
    left(90)
    forward (30)
    right(90)
    forward (30)
    right(90)
    forward(60)
    penup()
    setposition(0,0)
    pendown()
    forward(30)
    right(90)
    forward(30)
    right(90)
    forward(60)
 
#creates the number 6   
def six():
    pendown()
    left(90)
    forward (25)
    right(90)
    forward (30)
    right(90)
    forward(30)
    penup()
    setposition(5,0)
    pendown()
    left(180)
    forward (30)
    left(90)
    forward (30)
    left(90)
    forward(50)
    penup()
    setposition(0,0)
    pendown()
    forward(20)
    right(90)
    forward(30)
     
    
#this will draw the number of layers in the center of the circle based on 
#how many layers the user wants 
if layers==1:
    one()
elif layers==2:
    two()
elif layers==3:
    three()
elif layers==4:
    four()
elif layers==5:
    five()
else:
    six()
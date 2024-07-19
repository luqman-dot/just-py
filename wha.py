"""
FALLING SPADES | Cole Heiman | Introductory Programming
-------------------------------------------------------
This program will create a number of cards doing a 
"bounce", (its more of a zigzag now) animation based on a user input
if a specific number of cards is guessed a win animation
will play during the end of the render
and if not the game ends
(TIP: Look at the brightness of the cards to figure out the number!)
IF THE SPADES AT THE END ARE RED YOU FAILED, IF THEY ARE GREEN YOU WIN!

"""
#starting conditions
speed(0)
penup()
bgcolor("black")
winloss = input("Win / loose screen?(y/n): ")
#Lose function
def lose(losheight):
    bgcolor("white")
    clear()
    penup()
    while losheight > -200:
        setposition(-200, losheight)
        for i in range(10):
            color((255,0,0))
            drawSpade()
            forward(100)
        losheight = losheight - 100
    
#Win function
def win(winheight):
    bgcolor("white")
    clear()
    penup()
    while winheight > -200:
        setposition(-200, winheight)
        for i in range(10):
            color((0,255,0))
            drawSpade()
            forward(100)
        winheight = winheight - 100
    
        

#CARDS variable
cards = int(input("Guess how many ace of spades im thinking of?(out of 42): "))

#func for drawing the spade shape
def drawSpade():
    begin_fill()
    left(75)
    circle(15, 210, 2)
    right(60)
    circle(10.2, 180)
    right(90)
    circle(10.2, 180)
    end_fill()
    
    left(45)
    forward(9.5)
    begin_fill()
    for i in range(2):
        forward(9.75)
        left(90)
        forward(25)
        left(90)
    end_fill()
    forward(4.625)
    left(90)
    forward(25)
    left(90)

#variable for brightness of cards
britns = 0

#func for drawing the card
def drawAce(britns, hue):
    pendown()
    begin_fill()
    color((britns-120 + (hue-120), britns-120 + (hue-250), britns-120 + (hue-100)))
    for i in range(2):
        forward(90)
        circle(4, 90)
        forward(140)
        circle(4, 90)
    color((britns, britns, britns))
    end_fill()
    color("black")
    penup()
    forward(85)
    left(90)
    forward(30)
    right(90)
    color((britns-120 + (hue-120), britns-120 + (hue-250), britns-120 + (hue-100)))
    drawSpade()
    left(90)
    forward(110)
    left(90)
    forward(67)
    drawSpade()
    
    left(180)
    forward(27)
    right(90)
    forward(110)
    left(90)

#the order of actions of the program
setposition(-200, -100)


#ascending cards (4)
if cards < 4:
    for i in range(0, cards * 15, 14):
     drawAce(i, i)
     backward(38)
     
else:
    for i in range(0, 56, 14):
     drawAce(i, i)
     backward(38)
    #descending cards (10)
    if cards < 14:
        for i in range(56, cards * 15, 14):
            drawAce(i, i)
            left(90)
            backward(50)
            right(90)
            backward(38)
    else:
        for i in range(56, 196, 14):
            drawAce(i, i)
            left(90)
            backward(50)
            right(90)
            backward(38)
        #re-ascending cards (4)
        if cards < 18:
            for i in range(195, cards * 14, 14):
                drawAce(i,i)
                backward(38)
                
        elif cards == 18:
            for i in range(198, 255, 14):
                drawAce(i,i)
                backward(38)
            speed(1)
            forward(500)
            speed(0)
            if winloss == "y":
                win(500)
        #reascending cards (7)
        elif cards < 22:
            for i in range(195, cards * 14, 14):
                drawAce(i,i)
                backward(38)
            speed(1)
            forward(500)
            speed(0)
            if winloss == "y":
                lose(500)
        
        else:
            for i in range(195, 293, 14):
                drawAce(i,i)
                backward(38)
            #redescending cards x2 (12)
            if cards < 32:
                for i in range(242,228-(14*(cards - 21)), -14):
                    drawAce(i,i)
                    left(90)
                    backward(50)
                    right(90)
                    backward(38)
                speed(1)
                forward(500)
                speed(0)
                if winloss == "y":
                    lose(500)
            #rerereascending cards (10)
            elif cards == 32:
                for i in range(242,74, -14):
                    drawAce(i,i)
                    left(90)
                    backward(50)
                    right(90)
                    backward(38)
            else:
                for i in range(242,74, -14):
                    drawAce(i,i)
                    left(90)
                    backward(50)
                    right(90)
                    backward(38)
                if cards > 32:
                    for i in range(74, 74+14*(cards - 32), 14):
                        drawAce(i,i)
                        backward(38)
                    speed(1)
                    forward(500)
                    speed(0)
                    if winloss == "y":
                        lose(500)
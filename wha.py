import turtle as t

# Starting conditions
t.speed(0)
t.penup()
t.bgcolor("black")

winloss = input("Win/lose screen? (y/n): ")

# Lose function
def lose(losheight):
    t.bgcolor("white")
    t.clear()
    t.penup()
    t.color((255, 0, 0))
    while losheight > -200:
        t.setposition(-200, losheight)
        for i in range(10):
            drawSpade()
            t.forward(100)
        losheight -= 100

# Win function
def win(winheight):
    t.bgcolor("white")
    t.clear()
    t.penup()
    t.color((0, 255, 0))
    while winheight > -200:
        t.setposition(-200, winheight)
        for i in range(10):
            drawSpade()
            t.forward(100)
        winheight -= 100

# Function for drawing the spade shape
def drawSpade():
    t.begin_fill()
    t.left(75)
    t.circle(15, 210, 2)
    t.right(60)
    t.circle(10.2, 180)
    t.right(90)
    t.circle(10.2, 180)
    t.end_fill()
    t.left(45)
    t.forward(9.5)
    t.begin_fill()
    for _ in range(2):
        t.forward(9.75)
        t.left(90)
        t.forward(25)
        t.left(90)
    t.end_fill()
    t.forward(4.625)
    t.left(90)
    t.forward(25)
    t.left(90)

# Function for drawing the card
def drawAce(britns, hue):
    t.pendown()
    t.begin_fill()
    t.color((britns-120 + (hue-120), britns-120 + (hue-250), britns-120 + (hue-100)))
    for _ in range(2):
        t.forward(90)
        t.circle(4, 90)
        t.forward(140)
        t.circle(4, 90)
    t.color((britns, britns, britns))
    t.end_fill()
    t.color("black")
    t.penup()
    t.forward(85)
    t.left(90)
    t.forward(30)
    t.right(90)
    t.color((britns-120 + (hue-120), britns-120 + (hue-250), britns-120 + (hue-100)))
    drawSpade()
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(67)
    drawSpade()
    t.left(180)
    t.forward(27)
    t.right(90)
    t.forward(110)
    t.left(90)

# Main program
cards = int(input("Guess how many ace of spades I'm thinking of? (out of 42): "))
t.setposition(-200, -100)

# Ascending cards (4)
if cards < 4:
    for i in range(0, cards * 15, 14):
        drawAce(i, i)
        t.backward(38)
else:
    for i in range(0, 56, 14):
        drawAce(i, i)
        t.backward(38)
    # Descending cards (10)
    if cards < 14:
        for i in range(56, cards * 15, 14):
            drawAce(i, i)
            t.left(90)
            t.backward(50)
            t.right(90)
            t.backward(38)
    else:
        for i in range(56, 196, 14):
            drawAce(i, i)
            t.left(90)
            t.backward(50)
            t.right(90)
            t.backward(38)
        # Re-ascending cards (4)
        if cards < 18:
            for i in range(195, cards * 14, 14):
                drawAce(i, i)
                t.backward(38)
        elif cards == 18:
            for i in range(198, 255, 14):
                drawAce(i, i)
                t.backward(38)
            t.speed(1)
            t.forward(500)
            t.speed(0)
            if winloss == "y":
                win(500)
        # Reascending cards (7)
        elif cards < 22:
            for i in range(195, cards * 14, 14):
                drawAce(i, i)
                t.backward(38)
            t.speed(1)
            t.forward(500)
            t.speed(0)
            if winloss == "y":
                lose(500)
        else:
            for i in range(195, 293, 14):
                drawAce(i, i)
                t.backward(38)
            # Redescending cards x2 (12)
            if cards < 32:
                for i in range(242, 228 - (14 * (cards - 21)), -14):
                    drawAce(i, i)
                    t.left(90)
                    t.backward(50)
                    t.right(90)
                    t.backward(38)
                t.speed(1)
                t.forward(500)
                t.speed(0)
                if winloss == "y":
                    lose(500)
            # Rerereascending cards (10)
            elif cards == 32:
                for i in range(242, 74, -14):
                    drawAce(i, i)
                    t.left(90)
                    t.backward(50)
                    t.right(90)
                    t.backward(38)
            else:
                for i in range(242, 74, -14):
                    drawAce(i, i)
                    t.left(90)
                    t.backward(50)
                    t.right(90)
                    t.backward(38)
                if cards > 32:
                    for i in range(74, 74 + 14 * (cards - 32), 14):
                        drawAce(i, i)
                        t.backward(38)
                    t.speed(1)
                    t.forward(500)
                    t.speed(0)
                    if winloss == "y":
                        lose(500)

t.done()

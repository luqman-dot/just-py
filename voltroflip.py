import pygame
from pygame import *
from random import choice

# Set odds for value choice
# 1: 8/14  2: 2/14  3: 1/14  Bomb: 3/14
ODDS = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 0, 0, 0]

# Create display window
SCREEN_WIDTH = 524
SCREEN_HEIGHT = 799

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Voltorb Flip')

# Load images
def load_and_scale_image(path, size):
    image = pygame.image.load(path)
    return pygame.transform.scale(image, size).convert()

background = load_and_scale_image('assets/background.png', (SCREEN_WIDTH, SCREEN_HEIGHT))
blankTile = load_and_scale_image('assets/blanktile.png', (48, 48))
flippedTile1 = load_and_scale_image('assets/flippedtile1.png', (48, 48))
flippedTile2 = load_and_scale_image('assets/flippedtile2.png', (48, 48))
flippedTile3 = load_and_scale_image('assets/flippedtile3.png', (48, 48))
hoverTile = load_and_scale_image('assets/tilehover.png', (60, 60))
bombTile = load_and_scale_image('assets/bombtile.png', (48, 48))

boldNums = [load_and_scale_image(f'assets/bold_{i}.png', (15, 20)) for i in range(10)]
bigNums = [load_and_scale_image(f'assets/big_{i}.png', (35, 55)) for i in range(10)]

# Set starting points amount
TOTALMONEY = 0
TOTALDISPLAY = '00000'
MONEY = 1
MONEYDISPLAY = '00000'

def flipCheck():
    global cardGrid
    win = True
    for row in cardGrid:
        for card in row:
            if card.value > 1 and not card.flipped:
                win = False
    return win

class Card():
    def __init__(self, x, y, image, value):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.flipped = False
        self.value = value

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            screen.blit(hoverTile, (self.rect.x - 8, self.rect.y - 8))
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                if not self.flipped:
                    self.flipCard()
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        screen.blit(self.image, self.rect.topleft)

    def flipCard(self):
        global run, MONEY, MONEYDISPLAY
        self.flipped = True
        if self.value == 0:
            self.image = bombTile
            MONEY = 1
            makeBoard()
        elif self.value == 1:
            self.image = flippedTile1
        elif self.value == 2:
            self.image = flippedTile2
        else:
            self.image = flippedTile3
        MONEY *= self.value
        MONEYDISPLAY = str(MONEY).zfill(5)

def makeBoard():
    global cardGrid, horPoints, verPoints, horVoltorbs, verVoltorbs

    cardGrid = []
    for i in range(5):
        row = []
        for t in range(5):
            tempVal = choice(ODDS)
            tempVar = Card(22.4 + (t * 64), 406.4 + (i * 64), blankTile, tempVal)
            row.append(tempVar)
        cardGrid.append(row)

    horPoints = [str(sum(card.value for card in row)).zfill(2) for row in cardGrid]
    verPoints = [str(sum(cardGrid[i][j].value for i in range(5))).zfill(2) for j in range(5)]
    horVoltorbs = [sum(1 for card in row if card.value == 0) for row in cardGrid]
    verVoltorbs = [sum(1 for i in range(5) if cardGrid[i][j].value == 0) for j in range(5)]

makeBoard()

# Game loop
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(30)
    screen.blit(background, (0, 0))

    for i in range(5):
        screen.blit(bigNums[int(TOTALDISPLAY[i])], (344 + (i * 32), 234.4))
        screen.blit(bigNums[int(MONEYDISPLAY[i])], (344 + (i * 32), 314.4))

    for i in range(5):
        screen.blit(boldNums[int(horPoints[i][0])], (359.2, 406.4 + (i * 64)))
        screen.blit(boldNums[int(horPoints[i][1])], (375.2, 406.4 + (i * 64)))
        screen.blit(boldNums[int(verPoints[i][0])], (39.2 + (i * 64), 726.4))
        screen.blit(boldNums[int(verPoints[i][1])], (55.2 + (i * 64), 726.4))
        screen.blit(boldNums[horVoltorbs[i]], (375.2, 434.4 + (i * 64)))
        screen.blit(boldNums[verVoltorbs[i]], (55.2 + (i * 64), 753.6))

    for row in cardGrid:
        for card in row:
            card.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if flipCheck():
        print('You win!')
        pygame.time.delay(3000)
        TOTALMONEY += MONEY
        MONEY = 1
        MONEYDISPLAY = '00000'
        TOTALDISPLAY = str(TOTALMONEY).zfill(5)
        makeBoard()

    pygame.display.update()

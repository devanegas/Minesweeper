import pygame 
import math
import random
from random import sample


global colors
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 30)
colors = font.render(" 0", True, (0,128,0)), font.render(" 1", True, (0,0,255)), font.render(" 2", True, (0,128,0)), font.render(" 3", True, (200,0,0)), font.render(" 4", True, (0,0,0)), font.render(" 5", True, (0,0,0)), font.render(" 6", True, (0,0,0)), font.render(" 7", True, (0,0,0)), font.render(" 8", True, (0,0,0)), font.render(" B", True, (255,0,0))

class cell:
    def __init__(self, x, y):
        self.rect = pygame.Rect(35*x, 35*y, 35, 35)
        self.isClicked = False
        self.isBomb = False
        self.color = font.render("", True, (0,128,128))
        self.connections = 0

    """def countBombs(self, pos):
        print(pos)"""

    def click(self, pos, color):
        if self.rect.collidepoint(pos):
            if self.isBomb == True:
                self.color = colors[9]
                self.isClicked = True
            else:
                self.color = colors[self.connections]
                self.isClicked = True
           
    
    """def draw(self, screen):
        if self.isClicked:
            pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, (128, 128, 128), self.rect, 5)"""

    def draw(self, screen):
        "pygame.draw.rect(screen, self.color, self.rect)"
        screen.blit(self.color, self.rect)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)





def main(xSize, ySize, nBombs):
    pygame.init()

    squareSize = 35
    height = squareSize * (ySize+2)
    width = squareSize * (xSize+2)


    screen = pygame.display.set_mode((height, width))
    squares = [[cell(x, y) for y in range(ySize+2)] for x in range(xSize+2)]


    #for square in sample([i for j in squares for i in j], nBombs):
    #   square.isBomb = True"""

    bombsPlaced = 0
    done = False
    while(not done):
        xRand = random.randint(1, xSize)
        yRand = random.randint(1, ySize)
        if squares[xRand][yRand].isBomb == True:
            done = False
        else:
            squares[xRand][yRand].isBomb = True
            print(xRand, yRand)
            bombsPlaced += 1

        if bombsPlaced == nBombs:
            done = True

    for x in range(1, xSize+1):
        for y in range(1, ySize+1):
            if squares[x][y].isBomb:
                squares[x-1][y-1].connections += 1
                squares[x][y-1].connections += 1
                squares[x+1][y-1].connections += 1
                squares[x-1][y].connections += 1
                squares[x+1][y].connections += 1
                squares[x-1][y+1].connections += 1
                squares[x][y+1].connections += 1
                squares[x+1][y+1].connections += 1
                


    def reveal(x, y):
        if x <= xSize and y <= ySize and x > 0 and y > 0 and squares[x][y].isBomb == False and squares[x][y].isClicked == False:

            squares[x-1][y-1].color = colors[squares[x-1][y-1].connections]
            squares[x][y-1].color = colors[squares[x][y-1].connections]
            squares[x+1][y-1].color = colors[squares[x+1][y-1].connections]
            squares[x-1][y].color = colors[squares[x-1][y].connections]
            squares[x+1][y].color = colors[squares[x+1][y].connections]
            squares[x-1][y+1].color = colors[squares[x-1][y+1].connections]
            squares[x][y+1].color = colors[squares[x][y+1].connections]
            squares[x+1][y+1].color = colors[squares[x+1][y+1].connections]

            squares[x][y].isClicked = True


            if squares[x-1][y-1].connections == 0:
                reveal(x-1, y-1)
            if squares[x][y-1].connections == 0:
                reveal(x, y-1)
            if squares[x+1][y-1].connections == 0:
                reveal(x+1, y-1)
            if squares[x-1][y].connections == 0:
                reveal(x-1, y)
            if squares[x+1][y].connections == 0:
                reveal(x+1, y)
            if squares[x-1][y+1].connections == 0:
                reveal(x-1, y+1)
            if squares[x][y+1].connections == 0:
                reveal(x, y+1)
            if squares[x+1][y+1].connections == 0:
                reveal(x+1, y+1)
        else:
            return



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                xCor, yCor = event.pos
                xReal = math.floor(xCor/35)
                yReal = math.floor(yCor/35)
                if squares[xReal][yReal].connections == 0 and xReal <= xSize and yReal <= ySize and xReal > 0 and yReal > 0 and squares[xReal][yReal].isBomb == False:
                    reveal(xReal, yReal)
                for x in range(1, xSize+1):
                    for y in range(1, ySize+1):
                        squares[x][y].click(event.pos, (75, 77, 79))

                            #print(squares[x][y].connections)
                

                     
            screen.fill((141, 144, 147))

            for x in range(1, xSize+1):
                for y in range (1, ySize+1):
                    squares[x][y].draw(screen)
            
            pygame.display.flip()

main(6, 6, 5)
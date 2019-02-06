import pygame 
import math
from random import sample


global colors
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 30)
colors = font.render(" 0", True, (0,0,0)), font.render(" 1", True, (0,0,0)), font.render(" 2", True, (0,0,0)), font.render(" 3", True, (0,0,0)), font.render(" 4", True, (0,0,0)), font.render(" 5", True, (0,0,0)), font.render(" 6", True, (0,0,0)), font.render(" 7", True, (0,0,0)), font.render(" 8", True, (0,0,0)), font.render(" B", True, (0,0,0))

class cell:
    def __init__(self, x, y):
        self.rect = pygame.Rect(35*x, 35*y, 35, 35)
        self.isClicked = False
        self.isBomb = False
        self.color = font.render("", True, (0,128,0))
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
    height = squareSize * ySize
    width = squareSize * xSize


    screen = pygame.display.set_mode((height, width))
    squares = [[cell(x, y) for y in range(0, ySize)] for x in range(0, xSize)]


    for square in sample([i for j in squares for i in j], nBombs):
        square.isBomb = True


    for x in range(0, xSize):
        for y in range(0, ySize):
            if squares[x][y].isBomb:
                if x-1 <0 and y-1 <0:
                    squares[x+1][y].connections += 1
                    squares[x+1][y+1].connections += 1
                    squares[x][y+1].connections += 1
                elif x+1 >= xSize and y-1 < 0:
                    squares[x-1][y].connections += 1
                    squares[x-1][y+1].connections += 1
                    squares[x][y+1].connections += 1
                elif x+1 >= xSize and y+1 >= ySize:
                    squares[x-1][y].connections += 1
                    squares[x-1][y-1].connections += 1
                    squares[x][y-1].connections += 1
                elif x-1 < 0 and y+1 >= ySize:
                    squares[x+1][y].connections += 1
                    squares[x+1][y-1].connections += 1
                    squares[x][y-1].connections += 1

            #Left Arista
                elif x == 0 and y-1 >= 0 and y+1 < ySize:
                    squares[x+1][y].connections += 1
                    squares[x+1][y+1].connections += 1
                    squares[x][y+1].connections += 1
                    squares[x][y-1].connections += 1
                    squares[x+1][y-1].connections += 1
            #Top Arista
                elif x+1 < xSize and y == 0 and x-1 >= 0:
                    squares[x-1][y].connections += 1
                    squares[x-1][y+1].connections += 1
                    squares[x][y+1].connections += 1
                    squares[x+1][y].connections += 1
                    squares[x+1][y+1].connections += 1
            #Right Arista
                elif x == xSize-1 and y+1 < ySize and y-1 >= 0:
                    squares[x-1][y].connections += 1
                    squares[x-1][y-1].connections += 1
                    squares[x][y-1].connections += 1
                    squares[x-1][y-1].connections += 1
                    squares[x-1][y+1].connections += 1

            #Down Arista
                elif x-1 >= 0 and y == ySize-1 and x+1 < xSize:
                    squares[x+1][y].connections += 1
                    squares[x+1][y-1].connections += 1
                    squares[x][y-1].connections += 1
                    squares[x-1][y].connections += 1
                    squares[x-1][y-1].connections += 1
                
                elif x+1 < xSize and y+1 <ySize and x-1 >= 0 and y-1 >=0:
                    print(x,y)
                    squares[x-1][y-1].connections += 1
                    squares[x][y-1].connections += 1
                    squares[x+1][y-1].connections += 1
                    squares[x-1][y].connections += 1
                    squares[x+1][y].connections += 1
                    squares[x-1][y+1].connections += 1
                    squares[x][y+1].connections += 1
                    squares[x+1][y+1].connections += 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                    for x in range(0, xSize):
                        for y in range(0, ySize):
                            squares[x][y].click(event.pos, (75, 77, 79))
                            #print(squares[x][y].connections)

                        

                            
            screen.fill((141, 144, 147))

            for x in range(0, xSize):
                for y in range (0, ySize):
                    squares[x][y].draw(screen)
            
            pygame.display.flip()

main(16, 16, 40)
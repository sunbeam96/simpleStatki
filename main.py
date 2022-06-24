import pygame
from board import Board
from game import Game

if __name__ == '__main__':

    pygame.init()  

    isRunning = True
    cellSize = 30
    screen = pygame.display.set_mode((cellSize * 10,2 * cellSize * 10))
    pygame.display.set_caption("simpleStatki")
    gameInstance = Game()
    screen.fill(pygame.color.Color("black"))


    while isRunning:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                isRunning = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
            for y in range(10):
                for x in range(10):
                    pygame.draw.rect(screen, gameInstance.getColorForAiPosition(x, y),
                                    [x * cellSize, y * cellSize,
                                    cellSize, cellSize])

                    dmz = 30
                    pygame.draw.rect(screen, gameInstance.getColorForPlayerPosition(x, y),
                                    [x * cellSize,
                                    dmz + y * cellSize,
                                    cellSize, cellSize])

    pygame.quit()
    
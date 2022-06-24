import pygame
from board import Board
from game import Game

if __name__ == '__main__':

    pygame.init()  

    dmz = 20
    isRunning = True
    cellSize = 30
    screen = pygame.display.set_mode((cellSize * 10,dmz + 2 * cellSize * 10))
    pygame.display.set_caption("simpleStatki")
    gameInstance = Game()
    screen.fill(("white"))

    while isRunning:
        for event in pygame.event.get():  
            for y in range(10):
                for x in range(10):
                    pygame.draw.rect(screen, gameInstance.getColorForAiPosition(x, y),
                                    [x * cellSize, y * cellSize,
                                    cellSize, cellSize])

                    offset = dmz + 10 * cellSize
                    pygame.draw.rect(screen, gameInstance.getColorForPlayerPosition(x, y),
                                    [x * cellSize,
                                    offset + y * cellSize,
                                    cellSize, cellSize])
                pygame.display.update()
            if event.type == pygame.QUIT:  
                isRunning = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clickx, clicky = pygame.mouse.get_pos()
            screen.fill("white")

    pygame.quit()
    
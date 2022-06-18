import pygame
from ship import Ship
from board import Board

if __name__ == '__main__':

    pygame.init()  

    isRunning = True
    screen = pygame.display.set_mode((800,500))  

    while isRunning:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                isRunning = False  
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
        print("Hello world")

    pygame.quit()
    
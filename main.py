import pygame

if __name__ == '__main__':

    pygame.init()  

    isRunning = True
    screen = pygame.display.set_mode((800,500))  

    while isRunning:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                isRunning = False  
        print("Hello world")

    pygame.quit()
    
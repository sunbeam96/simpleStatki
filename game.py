# class representing game logic
from board import Board
import pygame

class Game:
    def __init__(self):
        self.playerBoard = Board()
        self.aiBoard = Board()
        self.aiBoard.placeShipsRandomly()
        self.playerBoard.placeShipsRandomly()

    def __getColorForPosition(self, x, y, board):
        val = board.getPositionValue(x, y)
        if val == 's':
            return pygame.color.Color("blue")
        elif val == 'b':
            return pygame.color.Color("gray")
        elif val == 'm':
            return pygame.color.Color("lightcyan")
        elif val == 'x':
            return pygame.color.Color("red")

    def getColorForAiPosition(self, x, y):
        return self.__getColorForPosition(x, y, self.aiBoard)

    def getColorForPlayerPosition(self, x, y):
        return self.__getColorForPosition(x, y, self.playerBoard)

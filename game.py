# class representing game logic
from board import Board
import pygame

class Game:
    def __init__(self):
        self.playerBoard = Board()
        self.aiBoard = Board()
        self.aiBoard.placeShipsRandomly()
        self.playerBoard.placeShipsRandomly()
        self.enemyDisplayBoard = Board()

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

    def __syncAiBoardWithDisplayBoard(self):
        for y in range(10):
            for x in range(10):
                valAi = self.aiBoard.getPositionValue(x, y)
                valDisplay = self.enemyDisplayBoard.getPositionValue(x, y)
                if (valAi == valDisplay):
                    continue
                if (valAi == 'x') or (valAi == 'm'):
                    self.enemyDisplayBoard.setPositionValue(x, y, valAi)

    def getColorForAiPosition(self, x, y):
        return self.__getColorForPosition(x, y, self.enemyDisplayBoard)

    def getColorForPlayerPosition(self, x, y):
        return self.__getColorForPosition(x, y, self.playerBoard)

    def shootAtPos(self, x, y):
        self.aiBoard.tryShootAtPos(x, y)
        self.__syncAiBoardWithDisplayBoard()
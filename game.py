# class representing game logic
from board import Board

class Game:
    def __init__(self):
        self.playerBoard = Board()
        self.aiBoard = Board()
        self.aiBoard.placeShipsRandomly()





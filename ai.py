# class representing game logic
from board import Board
from random import randint

class Ai:
    def __init__(self, board: Board()):
        self.playerBoard = board # this is a non-AI player board on which AI will try to hit ships

    def __isFieldLeftToShoot(self):
        for y in range(10):
            for x in range(10):
                fieldVal = self.playerBoard.getPositionValue(x, y)
                if (fieldVal == 's' or fieldVal == 'b'): # still can shoot as long as there are not uncovered fields
                    return True
        return False

    def __getRandomPos(self):
        startx = randint(0, 9)
        starty = randint(0, 9)
        return startx, starty

    def __getRandomPosValidToShoot(self):
        if (not self.__isFieldLeftToShoot):
            return False
        startx, starty = self.__getRandomPos()
        randomVal = self.playerBoard.getPositionValue(startx, starty)
        while (randomVal != 's') or (randomVal != 'b'): # valid position to shoot is when it is sea field or battleship field on a board
            startx, starty = self.__getRandomPos()
            randomVal = self.playerBoard.getPositionValue(startx, starty)
        return startx, starty

    def actSingleMove(self):
        x, y = self.__getRandomPosValidToShoot()
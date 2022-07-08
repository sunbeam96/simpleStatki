# class representing ai player logic

from board import Board
from random import randint
import queue

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Ai:
    def __init__(self, board: Board()):
        self.playerBoard = board # this is a non-AI player board on which AI will try to hit ships
        self.shootingAreaExhaused = False
        self.moveQueue = queue.Queue()

    def __dispatchNextMove(self):
        nextMove = self.moveQueue.get()
        self.playerBoard.tryShootAtPos(nextMove.x, nextMove.y)

    def __addToQueueInDirection(self, startx, starty, direction):
        x = startx
        y = starty
        nextPos = Pos(x, y)
        self.moveQueue.put(nextPos)
        if direction == 'north':
            while (y+1<=9):
                nextPos = Pos(x, y+1)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x, y+1)):
                    y = y+1
                else:
                    return
        if direction == 'south':
            while (y-1>=0):
                nextPos = Pos(x, y-1)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x, y-1)):
                    y = y-1
                else:
                    return
        if direction == 'east':
            while (x+1<=9):
                nextPos = Pos(x+1, y)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x+1, y)):
                    x = x+1
                else:
                    return
        if direction == 'west':
            while (x-1>=0):
                nextPos = Pos(x-1, y)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x-1, y)):
                    x = x-1
                else:
                    return

    def __fillUpMoveQueue(self):
        x, y = self.__getRandomPosValidToShoot()
        if (x == -1):
            return
        nextPos = Pos(x, y)
        self.moveQueue.put(nextPos)
        if not (x-1<0):
            if (self.playerBoard.isPosValidToShoot(x-1, y)):
                nextPos = Pos(x-1, y)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x-1, y)):
                    self.__addToQueueInDirection(x-1, y, 'west')
        if not (x+1>9):
            if (self.playerBoard.isPosValidToShoot(x+1, y)):
                nextPos = Pos(x+1, y)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x+1, y)):
                    self.__addToQueueInDirection(x+1, y, 'east')
        if not (y-1<0):
            if (self.playerBoard.isPosValidToShoot(x, y-1)):
                nextPos = Pos(x, y-1)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x, y-1)):
                    self.__addToQueueInDirection(x, y-1, 'south')
        if not (y+1>9):
            if (self.playerBoard.isPosValidToShoot(x, y+1)):
                nextPos = Pos(x, y+1)
                self.moveQueue.put(nextPos)
                if (self.playerBoard.isShip(x, y+1)):
                    self.__addToQueueInDirection(x, y+1, 'north')

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
            return -1, -1
        startx, starty = self.__getRandomPos()
        randomVal = self.playerBoard.getPositionValue(startx, starty)
        while (randomVal != 's') and (randomVal != 'b'): # valid position to shoot is when it is sea field or battleship field on a board
            startx, starty = self.__getRandomPos()
            randomVal = self.playerBoard.getPositionValue(startx, starty)
        return startx, starty

    def actSingleMove(self):
        if (self.moveQueue.empty):
            self.__fillUpMoveQueue()
        self.__dispatchNextMove()

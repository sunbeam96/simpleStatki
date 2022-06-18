from random import randint
from random import choice
# class representing game board per each player
# legend:
# s - sea
# b - battleship
# m - missed shot
# x - hit
class Board:
    def __init__(self, boardSize = 10):
        self.board = self.__initializeBoardWithSea(boardSize)

    def __initializeBoardWithSea(self, boardSize):
        board = []
        for yIter in range(boardSize):
            row = []
            for xIter in range(boardSize):
                row.append('s')
            board.append(row)
        return board

    def getBoard(self):
        return self.board

    def isSea(self, x, y):
        return self.board[y][x] == 's'

    def __isPlacingPossible(self, x, y):
        if not self.isSea(x, y):
            return False
        else:
            if not (x-1<0):
                if not self.isSea(x-1, y):
                    return False
            if not (x+1>9):
                if not self.isSea(x+1, y):
                    return False
            if not (y-1<0):
                if not self.isSea(x, y-1):
                    return False
            if not (y+1>9):
                if not self.isSea(x, y+1):
                    return False
            if not self.isSea(x+1, y+1):
                return False
            if not self.isSea(x+1, y-1):
                return False
            if not self.isSea(x-1, y+1):
                return False
            if not self.isSea(x-1, y-1):
                return False
        return True

    def __canBePlacedInDirection(self, x, y, direction, length):
        directionx = x
        directiony = y
        if direction == 'north':
            for iter in range(length):
                directiony = directiony+1
                if not self.isSea(x, directiony):
                    return False
        if direction == 'south':
            for iter in range(length):
                directiony = directiony-1
                if not self.isSea(x, directiony):
                    return False
        if direction == 'east':
            for iter in range(length):
                directionx = directionx-1
                if not self.isSea(directionx, y):
                    return False
        if direction == 'west':
            for iter in range(length):
                directionx = directionx+1
                if not self.isSea(directionx, y):
                    return False
        return True

    def __placeShipRandomly(self, numOfMasts):
        startx = randint(0, 9)
        starty = randint(0, 9)
        while not self.__isPlacingPossible(startx, starty):
            startx = randint(0, 9)
            starty = randint(0, 9)

        directions = ['north', 'south', 'east', 'west']
        direction = choice(directions)
        while not self.__canBePlacedInDirection(startx, starty, direction, numOfMasts):
            direction = choice(directions)

    def placeShipsRandomly(self):
        singleMastShipsLeft = 4
        doubleMastShipsLeft = 3
        tripleMastShipsLeft = 2
        quadrupleMastShipsLeft = 1

        for iter in range(10):
            if quadrupleMastShipsLeft:
                self.__placeShipRandomly(4)
                quadrupleMastShipsLeft = quadrupleMastShipsLeft - 1
            elif tripleMastShipsLeft:
                self.__placeShipRandomly(3)
                tripleMastShipsLeft = tripleMastShipsLeft - 1
            elif doubleMastShipsLeft:
                self.__placeShipRandomly(2)
                doubleMastShipsLeft = doubleMastShipsLeft - 1
            elif singleMastShipsLeft:
                self.__placeShipRandomly(1)
                singleMastShipsLeft = singleMastShipsLeft - 1



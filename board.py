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
        self.placingProcedureRestartNeeded = False

    def __initializeBoardWithSea(self, boardSize):
        board = []
        for yIter in range(boardSize):
            row = []
            for xIter in range(boardSize):
                row.append('s')
            board.append(row)
        return board

    def tryShootAtPos(self, x, y):
        originalVal = self.getPositionValue(x, y)
        if (originalVal == 'b'):
            self.setPositionValue(x, y, 'x')
        if (originalVal == 's'):
            self.setPositionValue(x, y, 'm')

    def getBoard(self):
        return self.board

    def isSea(self, x, y):
        return self.board[y][x] == 's'

    def getPositionValue(self, x, y):
        return self.board[y][x]

    def setPositionValue(self, x, y, val):
        self.board[y][x] = val

    def __placeShipWithParameters(self, startx, starty, direction, numOfMasts):
        currentx = startx
        currenty = starty
        for mast in range(numOfMasts):
            self.board[currenty][currentx] = 'b'
            if direction == 'north':
                currenty = currenty+1
            if direction == 'south':
                currenty = currenty-1
            if direction == 'east':
                currentx = currentx-1
            if direction == 'west':
                currentx = currentx+1

    def __isPlacingPossible(self, x, y):
        if not self.isSea(x, y):
            return False
        else:
            if (x-1<0) or (x+1>9) or (y-1<0) or (y+1>9):
                return False
            if not self.isSea(x-1, y):
                return False
            if not self.isSea(x+1, y):
                return False
            if not self.isSea(x, y-1):
                return False
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
                if (directiony+1 > 9):
                    return False
                directiony = directiony+1
                if not self.__isPlacingPossible(x, directiony):
                    return False
        if direction == 'south':
            for iter in range(length):
                if (directiony-1 < 0):
                    return False
                directiony = directiony-1
                if not self.__isPlacingPossible(x, directiony):
                    return False
        if direction == 'east':
            for iter in range(length):
                if (directionx-1 < 0):
                    return False
                directionx = directionx-1
                if not self.__isPlacingPossible(directionx, y):
                    return False
        if direction == 'west':
            for iter in range(length):
                if (directionx+1 > 9):
                    return False
                directionx = directionx+1
                if not self.__isPlacingPossible(directionx, y):
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
        directionFailCounter = 0
        while not self.__canBePlacedInDirection(startx, starty, direction, numOfMasts):
            direction = choice(directions)
            directionFailCounter = directionFailCounter + 1
            if (directionFailCounter % 4) == 0:
                while not self.__isPlacingPossible(startx, starty):
                    startx = randint(0, 9)
                    starty = randint(0, 9)
            if (directionFailCounter > 50):
                print("Failing ship placing")
                self.placingProcedureRestartNeeded = True
                return
        self.__placeShipWithParameters(startx, starty, direction, numOfMasts)

    def placeShipsRandomly(self):
        singleMastShipsLeft = 4
        doubleMastShipsLeft = 3
        tripleMastShipsLeft = 2
        quadrupleMastShipsLeft = 1

        for iter in range(10):
            if self.placingProcedureRestartNeeded:
                self.board = self.__initializeBoardWithSea(10)
                self.placingProcedureRestartNeeded = False
                self.placeShipsRandomly()
                return
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



#class representing game board per each player
class Board:
    def __init__(self, boardSize):
        self.board = self.__initializeBoardWithSea(boardSize)

    def __initializeBoardWithSea(self, boardSize):
        board = [[]]
        for yIter in range(boardSize):
            row = []
            for xIter in range(boardSize):
                row.append('s')
            board.append(row)
        return board




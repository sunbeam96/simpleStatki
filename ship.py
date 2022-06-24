# class representing a battleship
class Ship:
    def __init__(self, x0, y0, x1, y1):
        self.startPoint = (x0, y0)
        self.endPoint = (x1, y1)

    def getLength(self):
        x0, y0 = self.startPoint
        x1, y1 = self.endPoint
        xdiff = abs(x0-x1)
        ydiff = abs(y0-y1)
        if xdiff:
            return xdiff
        else:
            return ydiff



class Cell:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

    def setCurrentPiece(self,val = None):
        self.currentpiece = val

    def getCurrentPiece(self,val):
        return self.currentpiece

    def isFree(self):
        return self.currentpiece==None
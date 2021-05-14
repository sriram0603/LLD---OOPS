class Piece:
    def __init__(self, color, pieceType: pieceType, moveproviders):
        self.isKilled = False
        self.color = color
        self.pieceType = pieceType
        self.moveProviders = moveproviders
        self.numberMoves = 0
    
    def getCurrentCell(self):
        return self.getCurrentCell
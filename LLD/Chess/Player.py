from abc import abstractmethod
class Player:
    def __init__(self, pieces: list):
        self.pieces =  pieces
    
    def getPiece(PieceType: pieceType):
        for piece in getPieces():
            if piece.getPieceType()==PieceType:
                return piece
        print("piece Not found error")

    @abstractmethod
    def makeMove():
        pass
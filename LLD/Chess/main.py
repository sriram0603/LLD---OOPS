from . import Cell
class Board:
    def __init__(self,size = 8,cells):
        self.boardsize = size
        self.cells = cells
    
    def getLeftCell(self,cell: Cell):
        return self.getCellAtLocation(cell.getX(),cell.getY()-1)
    
    def getRightCell(self,cell: Cell):
        return self.getCellAtLocation(cell.getX(),cell.getY()+1)
    
    def getUpCell(self,cell: Cell):
        return self.getCellAtLocation(cell.getX()-1,cell.getY())
    
    def getDownBoard(self,cell: Cell):
        return self.getCellAtLocation(cell.getX()+1,cell.getY())
    
    def getCellAtLocation(x: int, y: int) -> Cell:
        if x>=self.boardsize or x<0:
            return None
        if y>=self.boardsize or y<0:
            return None
        return self.cells[x][y]
    
    # to check if the player is on check on the current board 

    def isPlayerOnCheck(player: Player):
        return self.checkIfPieceCanBeKilled(player.getPiece(PieceType.KING),kingCheckEvaluationBlockers(), player)
    
    # to check if target piece can be killed, 
    # to which player does the target belongs to.
    # list of blockers for the target piece to be non occupiable.
    # return if the cell is in danger or not.

    def checkIfPieceCanBeKilled(self, targetpiece: Piece, cellOccupyBlockers: List, player: Player):
        for i in range(len(self.boardsize)):
            for j in range(len(self.boardsize[0])):
                currPiece = self.getCellAtLocation(i,j).getCurrentPiece()
                if currPiece is not None and not currPiece.isPieceFromSamePlayer(targetpiece):
                    nextPossibleCells = currPiece.nextPossiblecells(self.boardsize,player)
                    if targetpiece in nextPossibleCells:
                        return True
        return False
    
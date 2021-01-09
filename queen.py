# importing bishop and rook like this vs just 'import' prevents circular import error; unsure if good work around
from bishop import Bishop
from rook import Rook


class Queen(Bishop, Rook):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.bMoves = []
        self.rMoves = []

    def getMoves(self, piecesDict):
        Bishop.getMoves(self, piecesDict)
        Rook.getMoves(self, piecesDict)

    def showMoves(self, display):
        if self.selected:
            Bishop.showMoves(self, display)
            Rook.showMoves(self, display)

    def validMove(self, mouseP):
        # could make faster by checking if mouseP x or y axis is same to self then you know it is a rook move
        if Bishop.validMove(self, mouseP) or Rook.validMove(self, mouseP):
            return True
        return False

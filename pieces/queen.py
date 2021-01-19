# importing bishop and rook like this vs just 'import' prevents circular import error; unsure if good work around
from pieces.bishop import Bishop
from pieces.rook import Rook


class Queen(Bishop, Rook):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.bMoves = []
        self.rMoves = []

    def getMoves(self, gameState):
        Bishop.getMoves(self, gameState)
        Rook.getMoves(self, gameState)

    def showMoves(self, display):
        Bishop.showMoves(self, display)
        Rook.showMoves(self, display)

    def validMove(self, mouseP):
        # could make faster by checking if mouseP x or y axis is same to self then you know it is a rook move
        return Bishop.validMove(self, mouseP) or Rook.validMove(self, mouseP)

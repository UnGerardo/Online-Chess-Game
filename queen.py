import pygame
import chesspiece
# importing bishop and rook like this vs just 'import' prevents circular import error; unsure if good work around
from bishop import Bishop
from rook import Rook
from grid import SQUARE_SIZE


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
            print("got here")
            Bishop.showMoves(self, display)
            Rook.showMoves(self, display)

    def validMove(self, mouseP):
        for move in self.bMoves:
            if move and mouseP[0] == move[0] and mouseP[1] == move[1]:
                return True
        return False

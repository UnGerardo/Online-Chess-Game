import pygame
import chesspiece
import bishop as b
import rook as r
import grid


class Queen(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.bMoves = []
        self.rMoves = []

    def getMoves(self, piecesDict):




    def showMoves(self, display):
        if self.selected and self.moves[0]:
            for move in self.moves:
                if move:
                    pygame.draw.rect(display,
                                     '#009900',
                                     pygame.Rect(((move[0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                 ((move[1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                 grid.SQUARE_SIZE, grid.SQUARE_SIZE))

    def validMove(self, mouseP):
        for move in self.moves:
            if move and mouseP[0] == move[0] and mouseP[1] == move[1]:
                return True
        return False

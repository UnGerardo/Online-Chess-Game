import pygame
import chesspiece
import bishop as b
import rook as r
import grid


class Queen(b.Bishop, r.Rook):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.bMoves = []
        self.rMoves = []

    def getMoves(self, piecesDict):
        b.Bishop.getMoves(self, piecesDict)
        r.Rook.getMoves(self, piecesDict)

    # def showMoves(self, display):
    #     if self.selected:
    #         for move in self.bMoves:
    #             if move:
    #                 pygame.draw.rect(display,
    #                                  '#009900',
    #                                  pygame.Rect(((move[0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
    #                                              ((move[1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
    #                                              grid.SQUARE_SIZE, grid.SQUARE_SIZE))
    #
    # def validMove(self, mouseP):
    #     for move in self.bMoves:
    #         if move and mouseP[0] == move[0] and mouseP[1] == move[1]:
    #             return True
    #     return False

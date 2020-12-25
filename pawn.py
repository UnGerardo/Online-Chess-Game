import pygame
import chesspiece as piece
import grid


class Pawn(piece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.firstMove = True

    def getMoves(self):
        self.possibleMoves = [(self.x, self.y - 1), (self.x, self.y - 2)]

    def showMoves(self, display):
        for move in self.possibleMoves:
            if self.selected:
                pygame.draw.rect(display,
                                 '#009900',
                                 pygame.Rect(((move[0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                             ((move[1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                             grid.SQUARE_SIZE, grid.SQUARE_SIZE))

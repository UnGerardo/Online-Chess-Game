import pygame
import chesspiece as piece
import grid


class Pawn(piece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.firstMove = True

    def showMoves(self, display):
        if self.selected:
            pygame.draw.rect(display,
                             '#00FF00',
                             pygame.Rect(((self.x * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                         (((self.y - 1) * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                         grid.SQUARE_SIZE, grid.SQUARE_SIZE))
            pygame.draw.rect(display,
                             '#00FF00',
                             pygame.Rect(((self.x * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                         (((self.y - 2) * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                         grid.SQUARE_SIZE, grid.SQUARE_SIZE))

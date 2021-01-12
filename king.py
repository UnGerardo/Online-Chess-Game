import pygame
from chesspiece import ChessPiece
from grid import SQUARE_SIZE


class King(ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.moves = []

    def getMoves(self, piecesDict):
        self.moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = self.x + j
                y = self.y + i
                if (1 <= x <= 8) and (1 <= y <= 8) and (not piecesDict[x][y]):
                    self.moves.append((self.x + j, self.y + i))

    def showMoves(self, display):
        if self.selected:
            for move in self.moves:
                if move:
                    pygame.draw.rect(display,
                                     '#009900',
                                     pygame.Rect(((move[0] * SQUARE_SIZE) - SQUARE_SIZE),
                                                 ((move[1] * SQUARE_SIZE) - SQUARE_SIZE),
                                                 SQUARE_SIZE, SQUARE_SIZE))

    def validMove(self, mouseP):
        for move in self.moves:
            if move and mouseP[0] == move[0] and mouseP[1] == move[1]:
                return True
        return False

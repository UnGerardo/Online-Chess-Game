import pygame
import chesspiece
import grid


class Knight(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.moves = []

    def getMoves(self):
        # reset
        self.moves = []

        upShift = self.y - 2
        rightShift = self.x + 2
        bottomShift = self.y + 2
        leftShift = self.x - 2
        # get top two
        if upShift >= 1:
            self.moves.append((self.x + 1, upShift))
            self.moves.append((self.x - 1, upShift))
        # get right two
        if rightShift <= 8:
            self.moves.append((rightShift, self.y + 1))
            self.moves.append((rightShift, self.y - 1))
        # get bottom two
        if bottomShift <= 8:
            self.moves.append((self.x + 1, bottomShift))
            self.moves.append((self.x - 1, bottomShift))
        # get left two
        if leftShift >= 1:
            self.moves.append((leftShift, self.y + 1))
            self.moves.append((leftShift, self.y - 1))

    def showMoves(self, display):
        if self.selected:
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

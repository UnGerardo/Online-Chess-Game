import pygame
import chesspiece
import grid


class Pawn(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.firstPos = (x, y)
        self.firstMove = True
        self.moves = []

    def getMoves(self, piecesDict):
        # get possible bMoves
        if self.firstMove:
            if (self.firstPos[0] == self.x) and (self.firstPos[1] == self.y):
                self.moves = [(self.x, self.y - 1), (self.x, self.y - 2)]
            else:
                self.moves = [(self.x, self.y - 1)]
                self.firstMove = False
        else:
            self.moves = [(self.x, self.y - 1)]

        # go through possible bMoves and see if any are taken, set to 0
        try:
            for i in range(len(self.moves)):
                if piecesDict[self.moves[i][0]][self.moves[i][1]]:
                    self.moves[i] = 0
        except KeyError:
            print('Possible move is out of bounds. Dont need to handle now because Pawn will switch-out in this case.')

        # if piece above but can move two spaces, prevent from moving to second
        if not self.moves[0] and self.firstMove:
            self.moves[1] = 0

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

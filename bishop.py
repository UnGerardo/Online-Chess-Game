import pygame
import chesspiece
import grid


class Bishop(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.possibleMoves = [
            'forwardRight': 
        ]

    def getMoves(self, piecesDict):
        # get possible moves
        if self.firstMove:
            if (self.firstPos[0] == self.x) and (self.firstPos[1] == self.y):
                self.possibleMoves = [(self.x, self.y - 1), (self.x, self.y - 2)]
            else:
                self.possibleMoves = [(self.x, self.y - 1)]
        else:
            self.possibleMoves = [(self.x, self.y - 1)]

        # go through possible moves and see if any are taken, set to 0
        try:
            for i in range(len(self.possibleMoves)):
                if piecesDict[self.possibleMoves[i][0]][self.possibleMoves[i][1]]:
                    self.possibleMoves[i] = 0
        except KeyError:
            print('Possible move is out of bounds. Dont need to handle now because Pawn will switch-out in this case.')

    # showMoves method for each piece bc need to determine if any straight line is blocked (see second condition in if)
    def showMoves(self, display):
        if self.selected and self.possibleMoves[0]:
            for move in self.possibleMoves:
                if move:
                    pygame.draw.rect(display,
                                     '#009900',
                                     pygame.Rect(((move[0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                 ((move[1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                 grid.SQUARE_SIZE, grid.SQUARE_SIZE))

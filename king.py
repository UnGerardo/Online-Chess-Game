from chesspiece import ChessPiece, validAMove
from grid import SQUARE_SIZE, HL_SQUARE


class King(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
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
                    display.blit(HL_SQUARE, (((move[0] * SQUARE_SIZE) - SQUARE_SIZE),
                                             ((move[1] * SQUARE_SIZE) - SQUARE_SIZE)))

    def validMove(self, mousePos):
        validAMove(self.moves, mousePos)

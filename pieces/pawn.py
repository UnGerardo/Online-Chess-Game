from pieces.chesspiece import ChessPiece, showAMoves, validAMove


class Pawn(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.firstPos = (x, y)
        self.firstMove = True
        self.moves = []
        self.direction = int((self.y - 5)/abs(self.y - 5)) * -1

    def getMoves(self, piecesDict):
        self.moves = []
        # get one space ahead
        if not piecesDict[self.x][self.y + self.direction]:
            self.moves.append((self.x, self.y + self.direction))

        # get second space ahead if first move
        if self.firstMove and not piecesDict[self.x][self.y + (self.direction * 2)] and self.moves:
            self.moves.append((self.x, self.y + (self.direction * 2)))

        # get top left move
        if not self.x == 1:
            takeLeft = piecesDict[self.x - 1][self.y + self.direction]
            if takeLeft and not (takeLeft.color == self.color):
                self.moves.append((self.x - 1, self.y + self.direction))

        # get top right move
        if not self.x == 8:
            takeRight = piecesDict[self.x + 1][self.y + self.direction]
            if takeRight and not (takeRight.color == self.color):
                self.moves.append((self.x + 1, self.y + self.direction))

    def showMoves(self, display):
        showAMoves(self.moves, display)

    def validMove(self, mousePos):
        return validAMove(self.moves, mousePos)

from chesspiece import ChessPiece, showAMoves, validAMove


class Pawn(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.firstPos = (x, y)
        self.firstMove = True
        self.moves = []

    def getMoves(self, piecesDict):
        # get possible moves maybe use a linked list for first move
        if self.firstMove:
            if (self.firstPos[0] == self.x) and (self.firstPos[1] == self.y):
                self.moves = [(self.x, self.y - 1), (self.x, self.y - 2)]
            else:
                self.moves = [(self.x, self.y - 1)]
                self.firstMove = False
        else:
            self.moves = [(self.x, self.y - 1)]

        # go through possible moves and see if any are taken, set to 0
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
        showAMoves(self.moves, display)

    def validMove(self, mousePos):
        return validAMove(self.moves, mousePos)

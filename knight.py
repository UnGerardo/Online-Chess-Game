from chesspiece import ChessPiece, showAMoves, validAMove


class Knight(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.moves = []

    def getMoves(self, piecesDict):
        # reset; piecesDict isn't used yet but will be to differentiate allies from enemies
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
        showAMoves(self.moves, display)

    def validMove(self, mousePos):
        return validAMove(self.moves, mousePos)

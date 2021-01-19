from pieces.chesspiece import ChessPiece, showAMoves, validAMove


class Knight(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.moves = []

    def getMoves(self, gameState):
        # reset
        self.moves = []

        upShift = self.y - 2
        rightShift = self.x + 2
        bottomShift = self.y + 2
        leftShift = self.x - 2
        # get top two
        if upShift >= 1:
            if (self.x + 1 <= 8) and \
               (not gameState[self.x + 1][upShift] or
               (not gameState[self.x + 1][upShift].color == self.color)):
                self.moves.append((self.x + 1, upShift))
            if (self.x - 1 >= 1) and \
               (not gameState[self.x - 1][upShift] or
               (not gameState[self.x - 1][upShift].color == self.color)):
                self.moves.append((self.x - 1, upShift))
        # get right two
        if rightShift <= 8:
            if (self.y + 1 <= 8) and \
               (not gameState[rightShift][self.y + 1] or
               (not gameState[rightShift][self.y + 1].color == self.color)):
                self.moves.append((rightShift, self.y + 1))
            if (self.y - 1 >= 1) and \
               (not gameState[rightShift][self.y - 1] or
               (not gameState[rightShift][self.y - 1].color == self.color)):
                self.moves.append((rightShift, self.y - 1))
        # get bottom two
        if bottomShift <= 8:
            if (self.x + 1 <= 8) and \
               (not gameState[self.x + 1][bottomShift] or
               (not gameState[self.x + 1][bottomShift].color == self.color)):
                self.moves.append((self.x + 1, bottomShift))
            if (self.x - 1 >= 1) and \
               (not gameState[self.x - 1][bottomShift] or
               (not gameState[self.x - 1][bottomShift].color == self.color)):
                self.moves.append((self.x - 1, bottomShift))
        # get left two
        if leftShift >= 1:
            if (self.y + 1 <= 8) and \
               (not gameState[leftShift][self.y + 1] or
               (not gameState[leftShift][self.y + 1].color == self.color)):
                self.moves.append((leftShift, self.y + 1))
            if (self.y - 1 >= 1) and \
               (not gameState[leftShift][self.y - 1] or
               (not gameState[leftShift][self.y - 1].color == self.color)):
                self.moves.append((leftShift, self.y - 1))

    def showMoves(self, display):
        showAMoves(self.moves, display)

    def validMove(self, mousePos):
        return validAMove(self.moves, mousePos)

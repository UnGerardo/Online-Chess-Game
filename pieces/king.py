from pieces.chesspiece import ChessPiece, showAMoves, validAMove


class King(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.moves = []

    def getMoves(self, gameState):
        self.moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                x = self.x + j
                y = self.y + i
                if (1 <= x <= 8) and (1 <= y <= 8):
                    if (not gameState[f'{x}'][f'{y}']) or (not gameState[f'{x}'][f'{y}'].color == self.color):
                        self.moves.append((self.x + j, self.y + i))

    def showMoves(self, display):
        showAMoves(self.moves, display)

    def validMove(self, mousePos):
        return validAMove(self.moves, mousePos)

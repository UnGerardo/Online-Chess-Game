import chesspiece as piece
import grid


class Pawn(piece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        self.firstMove = True

    def move(self):
        pass

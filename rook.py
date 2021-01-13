from chesspiece import ChessPiece, showLLMoves, validLLMove
from linkedlist import LinkedList


class Rook(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.rMoves = None

    def getMoves(self, piecesDict):
        # reset
        self.rMoves = LinkedList(None)

        rightShift = self.x + 1
        leftShift = self.x - 1
        upShift = self.y - 1
        bottomShift = self.y + 1
        tStop = False
        rStop = False
        bStop = False
        lStop = False
        while (not tStop) or (not rStop) or (not bStop) or (not lStop):
            # get top moves - while top is not reached or tStop isn't true
            if (not tStop) and upShift >= 1:
                tStop = True  # assume piece blocks path - removes need for additional check (if)
                if not piecesDict[self.x][upShift]:  # if no piece blocks path - add to moves and remove block
                    self.rMoves.append((self.x, upShift))
                    tStop = False
                elif not piecesDict[self.x][upShift].color == self.color:  # if there is a piece check color
                    self.rMoves.append((self.x, upShift))
            else:  # path blocked by piece or top reached
                tStop = True

            # get right moves
            if (not rStop) and rightShift <= 8:
                rStop = True
                if not piecesDict[rightShift][self.y]:
                    self.rMoves.append((rightShift, self.y))
                    rStop = False
                elif not piecesDict[rightShift][self.y].color == self.color:
                    self.rMoves.append((rightShift, self.y))
            else:
                rStop = True

            # get bottom moves
            if (not bStop) and bottomShift <= 8:
                bStop = True
                if not piecesDict[self.x][bottomShift]:
                    self.rMoves.append((self.x, bottomShift))
                    bStop = False
                elif not piecesDict[self.x][bottomShift].color == self.color:
                    self.rMoves.append((self.x, bottomShift))
            else:
                bStop = True

            # get left moves
            if (not lStop) and leftShift >= 1:
                lStop = True
                if not piecesDict[leftShift][self.y]:
                    self.rMoves.append((leftShift, self.y))
                    lStop = False
                elif not piecesDict[leftShift][self.y].color == self.color:
                    self.rMoves.append((leftShift, self.y))
            else:
                lStop = True
            upShift -= 1
            bottomShift += 1
            rightShift += 1
            leftShift -= 1

    def showMoves(self, display):
        showLLMoves(self.rMoves, display)

    def validMove(self, mousePos):
        validLLMove(self.rMoves, mousePos)

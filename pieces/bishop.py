from pieces.chesspiece import ChessPiece, showLLMoves, validLLMove
from pieces.linkedlist import LinkedList


class Bishop(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        self.bMoves = None

    def getMoves(self, gameState):
        # reset
        self.bMoves = LinkedList(None)

        rightShift = self.x + 1
        leftShift = self.x - 1
        upShift = self.y - 1
        bottomShift = self.y + 1
        trStop = False
        tlStop = False
        brStop = False
        blStop = False
        while (not trStop) or (not brStop) or (not blStop) or (not tlStop):
            # get top right bMoves + example of putting conditions on multiple lines
            if (not trStop) and (rightShift <= 8) and (upShift >= 1):
                trStop = True
                if not gameState[f'{rightShift}'][f'{upShift}']:
                    self.bMoves.append((rightShift, upShift))
                    trStop = False
                elif not gameState[f'{rightShift}'][f'{upShift}'].color == self.color:
                    self.bMoves.append((rightShift, upShift))
            else:
                trStop = True

            # get bottom right bMoves
            if (not brStop) and (rightShift <= 8) and (bottomShift <= 8):
                brStop = True
                if not gameState[f'{rightShift}'][f'{bottomShift}']:
                    self.bMoves.append((rightShift, bottomShift))
                    brStop = False
                elif not gameState[f'{rightShift}'][f'{bottomShift}'].color == self.color:
                    self.bMoves.append((rightShift, bottomShift))
            else:
                brStop = True

            # get bottom left bMoves
            if (not blStop) and (leftShift >= 1) and (bottomShift <= 8):
                blStop = True
                if not gameState[f'{leftShift}'][f'{bottomShift}']:
                    self.bMoves.append((leftShift, bottomShift))
                    blStop = False
                elif not gameState[f'{leftShift}'][f'{bottomShift}'].color == self.color:
                    self.bMoves.append((leftShift, bottomShift))
            else:
                blStop = True

            # get top left bMoves
            if (not tlStop) and (leftShift >= 1) and (upShift >= 1):
                tlStop = True
                if not gameState[f'{leftShift}'][f'{upShift}']:
                    self.bMoves.append((leftShift, upShift))
                    tlStop = False
                elif not gameState[f'{leftShift}'][f'{upShift}'].color == self.color:
                    self.bMoves.append((leftShift, upShift))
            else:
                tlStop = True

            rightShift += 1
            leftShift -= 1
            upShift -= 1
            bottomShift += 1

    def showMoves(self, display):
        showLLMoves(self.bMoves, display)

    def validMove(self, mousePos):
        return validLLMove(self.bMoves, mousePos)

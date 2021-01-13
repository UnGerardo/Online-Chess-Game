from chesspiece import ChessPiece
from linkedlist import LinkedList
from grid import SQUARE_SIZE, HL_SQUARE


class Rook(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        # bMoves linked list order: top, right, bottom, left
        self.rMoves = []

    def addToMoves(self, index, position):
        if not self.rMoves[index]:
            self.rMoves[index] = LinkedList(position)
        else:
            self.rMoves[index].append(position)

    def getMoves(self, piecesDict):
        # reset
        self.rMoves = [0, 0, 0, 0]

        rightShift = self.x + 1
        leftShift = self.x - 1
        upShift = self.y - 1
        bottomShift = self.y + 1
        tStop = False
        rStop = False
        bStop = False
        lStop = False
        while (not tStop) or (not rStop) or (not bStop) or (not lStop):
            # get top rMoves - while top is not reached or tStop isn't true
            if (not tStop) and upShift >= 1:
                if piecesDict[self.x][upShift]:  # if piece exists, check color
                    # if piece color is different, add to moves and stop
                    if not piecesDict[self.x][upShift].color == self.color:
                        self.addToMoves(0, (self.x, upShift))
                    tStop = True  # whether piece is same color or not, stop
                else:  # else piece not in the way, add and keep going
                    self.addToMoves(0, (self.x, upShift))
            else:  # path blocked by piece or top reached
                tStop = True

            # get right rMoves
            if (not rStop) and rightShift <= 8 and (not piecesDict[rightShift][self.y]):
                if not self.rMoves[1]:
                    self.rMoves[1] = LinkedList((rightShift, self.y))
                else:
                    self.rMoves[1].append((rightShift, self.y))
            else:
                rStop = True

            # get bottom rMoves
            if (not bStop) and bottomShift <= 8 and (not piecesDict[self.x][bottomShift]):
                if not self.rMoves[2]:
                    self.rMoves[2] = LinkedList((self.x, bottomShift))
                else:
                    self.rMoves[2].append((self.x, bottomShift))
            else:
                bStop = True

            # get left rMoves
            if (not lStop) and leftShift >= 1 and (not piecesDict[leftShift][self.y]):
                if not self.rMoves[3]:
                    self.rMoves[3] = LinkedList((leftShift, self.y))
                else:
                    self.rMoves[3].append((leftShift, self.y))
            else:
                lStop = True
            upShift -= 1
            bottomShift += 1
            rightShift += 1
            leftShift -= 1

    def showMoves(self, display):
        if self.selected:
            for linlist in self.rMoves:
                if linlist:
                    currentNode = linlist.head
                    while currentNode:
                        if currentNode['value']:
                            display.blit(HL_SQUARE, (((currentNode['value'][0] * SQUARE_SIZE) - SQUARE_SIZE),
                                                     ((currentNode['value'][1] * SQUARE_SIZE) - SQUARE_SIZE)))
                        currentNode = currentNode['next']

    def validMove(self, mouseP):
        # could possibly make faster if checking whether mousePos is to the right/left and above/below piece, then check
        # linlist that relates (topleft/topright, etc);
        for linlist in self.rMoves:
            if linlist:
                currentNode = linlist.head
                while currentNode:
                    if mouseP[0] == currentNode['value'][0] and mouseP[1] == currentNode['value'][1]:
                        return True
                    currentNode = currentNode['next']
        return False

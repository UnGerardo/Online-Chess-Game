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
        # reset - think about making moves one linked list, also for bishop=============================================
        # one linked list would mean the moves would be in top, right, bottom, left, top, right, bottom...
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
            # get top moves - while top is not reached or tStop isn't true
            if (not tStop) and upShift >= 1:
                tStop = True  # assume piece blocks path - removes need for additional check (if)
                if not piecesDict[self.x][upShift]:  # if no piece blocks path - add to moves and remove block
                    self.addToMoves(0, (self.x, upShift))
                    tStop = False
                elif not piecesDict[self.x][upShift].color == self.color:  # if there is a piece check color
                    self.addToMoves(0, (self.x, upShift))
            else:  # path blocked by piece or top reached
                tStop = True

            # get right moves
            if (not rStop) and rightShift <= 8:
                rStop = True
                if not piecesDict[rightShift][self.y]:
                    self.addToMoves(1, (rightShift, self.y))
                    rStop = False
                elif not piecesDict[rightShift][self.y].color == self.color:
                    self.addToMoves(1, (rightShift, self.y))
            else:
                rStop = True

            # get bottom moves
            if (not bStop) and bottomShift <= 8:
                bStop = True
                if not piecesDict[self.x][bottomShift]:
                    self.addToMoves(2, (self.x, bottomShift))
                    bStop = False
                elif not piecesDict[self.x][bottomShift].color == self.color:
                    self.addToMoves(2, (self.x, bottomShift))
            else:
                bStop = True

            # get left moves
            if (not lStop) and leftShift >= 1:
                lStop = True
                if not piecesDict[leftShift][self.y]:
                    self.addToMoves(3, (leftShift, self.y))
                    lStop = False
                elif not piecesDict[leftShift][self.y].color == self.color:
                    self.addToMoves(3, (leftShift, self.y))
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

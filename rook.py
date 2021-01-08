import pygame
import chesspiece
import linkedlist as ll
import grid


class Rook(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        # moves linked list order: top, right, bottom, left
        self.possibleMoves = []

    def getMoves(self, piecesDict):
        # reset
        self.possibleMoves = [0, 0, 0, 0]

        rightShift = self.x + 1
        leftShift = self.x - 1
        upShift = self.y - 1
        bottomShift = self.y + 1
        tStop = False
        rStop = False
        bStop = False
        lStop = False
        while (not tStop) or (not rStop) or (not bStop) or (not lStop):
            # get top moves
            if (not tStop) and upShift >= 1 and (not piecesDict[self.x][upShift]):
                if not self.possibleMoves[0]:
                    self.possibleMoves[0] = ll.LinkedList((self.x, upShift))
                else:
                    self.possibleMoves[0].append((self.x, upShift))
            else:
                tStop = True

            # get right moves
            if (not rStop) and rightShift <= 8 and (not piecesDict[rightShift][self.y]):
                if not self.possibleMoves[1]:
                    self.possibleMoves[1] = ll.LinkedList((rightShift, self.y))
                else:
                    self.possibleMoves[1].append((rightShift, self.y))
            else:
                rStop = True

            # get bottom moves
            if (not bStop) and bottomShift <= 8 and (not piecesDict[self.x][bottomShift]):
                if not self.possibleMoves[2]:
                    self.possibleMoves[2] = ll.LinkedList((self.x, bottomShift))
                else:
                    self.possibleMoves[2].append((self.x, bottomShift))
            else:
                bStop = True

            # get left moves
            if (not lStop) and leftShift >= 1 and (not piecesDict[leftShift][self.y]):
                if not self.possibleMoves[3]:
                    self.possibleMoves[3] = ll.LinkedList((leftShift, self.y))
                else:
                    self.possibleMoves[3].append((leftShift, self.y))
            else:
                lStop = True
            upShift -= 1
            bottomShift += 1
            rightShift += 1
            leftShift -= 1

    def showMoves(self, display):
        if self.selected:
            for linlist in self.possibleMoves:
                if linlist:
                    currentNode = linlist.head
                    while currentNode:
                        if currentNode['value']:
                            pygame.draw.rect(display,
                                             '#009900',
                                             pygame.Rect(((currentNode['value'][0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                         ((currentNode['value'][1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                                         grid.SQUARE_SIZE, grid.SQUARE_SIZE))
                        currentNode = currentNode['next']

    def validMove(self, mouseP):
        # could possibly make faster if checking whether mousePos is to the right/left and above/below piece, then check
        # linlist that relates (topleft/topright, etc);
        for linlist in self.possibleMoves:
            if linlist:
                currentNode = linlist.head
                while currentNode:
                    if mouseP[0] == currentNode['value'][0] and mouseP[1] == currentNode['value'][1]:
                        return True
                    currentNode = currentNode['next']
        return False

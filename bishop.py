import pygame
from chesspiece import ChessPiece
from linkedlist import LinkedList
from grid import SQUARE_SIZE


class Bishop(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        # bMoves linked list order: top right, bottom right, bottom left, top left
        self.bMoves = []

    def getMoves(self, piecesDict):
        # reset
        self.bMoves = [0, 0, 0, 0]

        rightShift = self.x+1
        leftShift = self.x-1
        upShift = self.y-1
        bottomShift = self.y+1
        trStop = False
        tlStop = False
        brStop = False
        blStop = False
        while (not trStop) or (not brStop) or (not blStop) or (not tlStop):
            # get top right bMoves + example of putting conditions on multiple lines
            if (not trStop) and \
                    (rightShift <= 8) and \
                    (upShift >= 1) and \
                    (not piecesDict[rightShift][upShift]):
                if not self.bMoves[0]:
                    self.bMoves[0] = LinkedList((rightShift, upShift))
                else:
                    self.bMoves[0].append((rightShift, upShift))
            else:
                trStop = True

            # get bottom right bMoves
            if (not brStop) and (rightShift <= 8) and (bottomShift <= 8) and (not piecesDict[rightShift][bottomShift]):
                if not self.bMoves[1]:
                    self.bMoves[1] = LinkedList((rightShift, bottomShift))
                else:
                    self.bMoves[1].append((rightShift, bottomShift))
            else:
                brStop = True

            # get bottom left bMoves
            if (not blStop) and (leftShift >= 1) and (bottomShift <= 8) and (not piecesDict[leftShift][bottomShift]):
                if not self.bMoves[2]:
                    self.bMoves[2] = LinkedList((leftShift, bottomShift))
                else:
                    self.bMoves[2].append((leftShift, bottomShift))
            else:
                blStop = True

            # get top left bMoves
            if (not tlStop) and (leftShift >= 1) and (upShift >= 1) and (not piecesDict[leftShift][upShift]):
                if not self.bMoves[3]:
                    self.bMoves[3] = LinkedList((leftShift, upShift))
                else:
                    self.bMoves[3].append((leftShift, upShift))
            else:
                tlStop = True

            rightShift += 1
            leftShift -= 1
            upShift -= 1
            bottomShift += 1

    def showMoves(self, display):
        if self.selected:
            for linlist in self.bMoves:
                if linlist:
                    currentNode = linlist.head
                    while currentNode:
                        if currentNode['value']:
                            pygame.draw.rect(display,
                                             '#009900',
                                             pygame.Rect(((currentNode['value'][0] * SQUARE_SIZE) - SQUARE_SIZE),
                                                         ((currentNode['value'][1] * SQUARE_SIZE) - SQUARE_SIZE),
                                                         SQUARE_SIZE, SQUARE_SIZE))
                        currentNode = currentNode['next']

    def validMove(self, mouseP):
        # could possibly make faster if checking whether mousePos is to the right/left and above/below piece, then check
        # linlist that relates (topleft/topright, etc);
        for linlist in self.bMoves:
            if linlist:
                currentNode = linlist.head
                while currentNode:
                    if mouseP[0] == currentNode['value'][0] and mouseP[1] == currentNode['value'][1]:
                        return True
                    currentNode = currentNode['next']
        return False

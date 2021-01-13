import pygame
from chesspiece import ChessPiece
from linkedlist import LinkedList
from grid import SQUARE_SIZE


class Rook(ChessPiece):
    def __init__(self, x, y, image, color):
        super().__init__(x, y, image, color)
        # bMoves linked list order: top, right, bottom, left
        self.rMoves = []

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
            # get top rMoves
            if (not tStop) and upShift >= 1 and (not piecesDict[self.x][upShift]):
                if not self.rMoves[0]:
                    self.rMoves[0] = LinkedList((self.x, upShift))
                else:
                    self.rMoves[0].append((self.x, upShift))
            else:
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
                            square = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
                            square.set_alpha(64)
                            square.fill((0, 255, 0))
                            display.blit(square, (((currentNode['value'][0] * SQUARE_SIZE) - SQUARE_SIZE),
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

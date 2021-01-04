import pygame
import chesspiece
import linkedlist as ll
import grid


class Bishop(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        # moves linked list order: top right, bottom right, bottom left, top left
        self.possibleMoves = []

    def getMoves(self, piecesDict):
        # reset
        self.possibleMoves = [0, 0, 0, 0]

        rightShift = self.x+1
        leftShift = self.x-1
        upShift = self.y-1
        bottomShift = self.y+1
        while rightShift <= 8 or leftShift >= 1 or upShift >= 1 or bottomShift <= 8:
            # get top right moves
            if (rightShift <= 8) and (upShift >= 1) and (not piecesDict[rightShift][upShift]):
                if not self.possibleMoves[0]:
                    self.possibleMoves[0] = ll.LinkedList((rightShift, upShift))
                self.possibleMoves[0].append((rightShift, upShift))

            # get bottom right moves
            if (rightShift <= 8) and (bottomShift <= 8) and (not piecesDict[rightShift][bottomShift]):
                if not self.possibleMoves[1]:
                    self.possibleMoves[1] = ll.LinkedList((rightShift, bottomShift))
                self.possibleMoves[1].append((rightShift, bottomShift))

            # get bottom left moves
            if (leftShift >= 1) and (bottomShift <= 8) and (not piecesDict[leftShift][bottomShift]):
                if not self.possibleMoves[2]:
                    self.possibleMoves[2] = ll.LinkedList((leftShift, bottomShift))
                self.possibleMoves[2].append((leftShift, bottomShift))

            # get top left moves
            if (leftShift >= 1) and (upShift >= 1) and (not piecesDict[leftShift][upShift]):
                if not self.possibleMoves[3]:
                    self.possibleMoves[3] = ll.LinkedList((leftShift, upShift))
                self.possibleMoves[3].append((leftShift, upShift))

            rightShift += 1
            leftShift -= 1
            upShift -= 1
            bottomShift += 1

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
        for linlist in self.possibleMoves:
            if linlist:
                currentNode = linlist.head
                while currentNode:
                    if mouseP[0] == currentNode['value'][0] and mouseP[1] == currentNode['value'][1]:
                        return True
                    currentNode = currentNode['next']
        return False

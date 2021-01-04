import pygame
import chesspiece
import linkedlist as ll
import grid


class Bishop(chesspiece.ChessPiece):
    def __init__(self, name, x, y, image,):
        super().__init__(name, x, y, image)
        # moves linked list order: top right, bottom right, bottom left, top left
        self.possibleMoves = [0, 0, 0, 0]

    def getMoves(self, piecesDict):
        # reset
        self.possibleMoves = [0, 0, 0, 0]

        # get top right moves
        shift = 1
        while (self.x+shift <= 8) and (self.y-shift >= 1) and (not piecesDict[self.x+shift][self.y-shift]):
            if shift == 1:
                self.possibleMoves[0] = ll.LinkedList((self.x+shift, self.y-shift))
            self.possibleMoves[0].append((self.x + shift, self.y - shift))
            shift += 1

        # get bottom right moves
        shift = 1
        while (self.x+shift <= 8) and (self.y+shift <= 8) and (not piecesDict[self.x+shift][self.y+shift]):
            if shift == 1:
                self.possibleMoves[1] = ll.LinkedList((self.x+shift, self.y+shift))
            self.possibleMoves[1].append((self.x + shift, self.y + shift))
            shift += 1

        # get bottom left moves
        shift = 1
        while (self.x-shift >= 1) and (self.y+shift <= 8) and (not piecesDict[self.x-shift][self.y+shift]):
            if shift == 1:
                self.possibleMoves[2] = ll.LinkedList((self.x-shift, self.y+shift))
            self.possibleMoves[2].append((self.x - shift, self.y + shift))
            shift += 1

        # get top left moves
        shift = 1
        while (self.x-shift >= 1) and (self.y-shift >= 1) and (not piecesDict[self.x-shift][self.y-shift]):
            if shift == 1:
                self.possibleMoves[3] = ll.LinkedList((self.x-shift, self.y-shift))
            self.possibleMoves[3].append((self.x - shift, self.y - shift))
            shift += 1

    # showMoves method for each piece bc need to determine if any straight line is blocked (see second condition in if)
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

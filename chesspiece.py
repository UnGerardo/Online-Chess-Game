import pygame
from grid import SQUARE_SIZE, HL_SQUARE


# for pieces that store moves as a linked list
def showLLMoves(moves, display):
    currentNode = moves.head['next']
    while currentNode:
        if currentNode['value']:
            display.blit(HL_SQUARE, (((currentNode['value'][0] * SQUARE_SIZE) - SQUARE_SIZE),
                                     ((currentNode['value'][1] * SQUARE_SIZE) - SQUARE_SIZE)))
        currentNode = currentNode['next']


# for pieces that store moves as a linked list
def validLLMove(moves, mousePos):
    currentNode = moves.head['next']
    while currentNode:
        if mousePos[0] == currentNode['value'][0] and mousePos[1] == currentNode['value'][1]:
            return True
        currentNode = currentNode['next']
    return False


# for pieces that store moves as an array
def showAMoves(moves, display):
    for move in moves:
        if move:
            display.blit(HL_SQUARE, (((move[0] * SQUARE_SIZE) - SQUARE_SIZE),
                                     ((move[1] * SQUARE_SIZE) - SQUARE_SIZE)))


# for pieces that store moves as an array
def validAMove(moves, mousePos):
    for move in moves:
        if move and mousePos[0] == move[0] and mousePos[1] == move[1]:
            return True
    return False


class ChessPiece:
    def __init__(self, x, y, image, color):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        # 0 is for black and 1 is for white
        self.color = color
        self.selected = False

    def show(self, display):
        display.blit(self.image, (
                                 ((self.x * SQUARE_SIZE) - SQUARE_SIZE),
                                 ((self.y * SQUARE_SIZE) - SQUARE_SIZE)
                                 ))

    def move(self, mousePos):
        self.selected = False
        self.x = mousePos[0]
        self.y = mousePos[1]

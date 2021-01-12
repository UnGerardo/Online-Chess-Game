import pygame
from grid import SQUARE_SIZE


class ChessPiece:
    def __init__(self, x, y, image, color):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        # 0 is for black and 1 is for white
        self.color = color
        self.selected = False
        self.captured = False

    def killed(self):
        self.captured = True

    def show(self, display):
        display.blit(self.image, (
                                 ((self.x * SQUARE_SIZE) - SQUARE_SIZE),
                                 ((self.y * SQUARE_SIZE) - SQUARE_SIZE)
                                 ))

    def move(self, mousePos):
        self.selected = False
        self.x = mousePos[0]
        self.y = mousePos[1]
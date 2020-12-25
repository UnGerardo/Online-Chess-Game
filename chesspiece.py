import pygame
import grid


class ChessPiece:
    def __init__(self, name, x, y, image):
        self.name = name
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.selected = False
        self.captured = False
        self.possibleMoves = []

    def killed(self):
        self.captured = True

    def show(self, display):
        display.blit(self.image, (
                                 ((self.x * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                 ((self.y * grid.SQUARE_SIZE) - grid.SQUARE_SIZE)
                                 ))
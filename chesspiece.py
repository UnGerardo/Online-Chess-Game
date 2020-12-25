import pygame
import grid


class ChessPiece:
    def __init__(self, name, x, y, image):
        self.name = name
        self.pos = (x, y)
        self.image = pygame.image.load(image)
        self.captured = False

    def killed(self):
        self.captured = True

    def show(self, display):
        display.blit(self.image, (
                                 ((self.pos[0] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE),
                                 ((self.pos[1] * grid.SQUARE_SIZE) - grid.SQUARE_SIZE)
                                 ))
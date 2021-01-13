import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
SQUARE_SIZE = 75

HL_SQUARE = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
HL_SQUARE.set_alpha(50)
HL_SQUARE.fill((0, 255, 0))


class Grid:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF, 32)

    def setScreen(self):
        pygame.display.set_caption("Chess")  # set window title
        self.screen.fill("#000000")  # setting bg color to black

    def drawGrid(self):
        counter = 0
        top = 0
        for i in range(8):
            left = 0
            for j in range(8):
                if counter % 2:
                    pygame.draw.rect(self.screen, '#000000', pygame.Rect(left, top, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, '#ffffff', pygame.Rect(left, top, SQUARE_SIZE, SQUARE_SIZE))
                left += SQUARE_SIZE
                counter += 1
            counter += 1
            top += SQUARE_SIZE

    def show(self):
        pygame.display.flip()

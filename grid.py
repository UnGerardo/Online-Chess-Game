import pygame


class Grid:
    def __init__(self):
        self.WINDOW_HEIGHT = 600
        self.WINDOW_WIDTH = 600
        self.SQUARE_SIZE = 75
        self.screen = pygame.display.set_mode(size=(self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

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
                    pygame.draw.rect(self.screen, '#000000', pygame.Rect(left, top, self.SQUARE_SIZE, self.SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, '#ffffff', pygame.Rect(left, top, self.SQUARE_SIZE, self.SQUARE_SIZE))
                left += self.SQUARE_SIZE
                counter += 1
            counter += 1
            top += self.SQUARE_SIZE

    def showGrid(self):
        pygame.display.flip()

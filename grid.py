import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
SQUARE_SIZE = 75
square = pygame.Rect(20.0, 10.0, SQUARE_SIZE, SQUARE_SIZE) # create square object with appropriate size

screen = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # set window width and height
pygame.display.set_caption("Chess")  # set window title
screen.fill("#000000")  # setting bg color to black

counter = 0
top = 0
for i in range(8):
    left = 0
    for j in range(8):
        if counter % 2:
            pygame.draw.rect(screen, '#000000', pygame.Rect(left, top, SQUARE_SIZE, SQUARE_SIZE))
        else:
            pygame.draw.rect(screen, '#ffffff', pygame.Rect(left, top, SQUARE_SIZE, SQUARE_SIZE))
        left += SQUARE_SIZE
        counter += 1
    counter += 1
    top += SQUARE_SIZE


def showGrid():
    pygame.display.flip()

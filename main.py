import pygame
import math
import pawn as p
import grid


def getMousePosition(value):
    return math.ceil((pygame.mouse.get_pos())[value]/grid.SQUARE_SIZE)


if __name__ == '__main__':
    chessGrid = grid.Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    running = True
    pawn = p.Pawn("bPawn", 1, 7, "images/pawn.png")

    mousePos = (0, 0)

    # Game loop
    while running:
        # if quit event is called stop loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mousePos = (getMousePosition(0), getMousePosition(1))
        print(mousePos)
        chessGrid.showGrid()
        pawn.show(chessGrid.screen)

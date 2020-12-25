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
    pieces = [p.Pawn("bPawn", 1, 7, "images/pawn.png"), p.Pawn("bPawn", 2, 7, "images/pawn.png")]
    mousePos = (0, 0)
    pieceSelected = False

    # Game loop
    while running:
        # if quit event is called stop loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = (getMousePosition(0), getMousePosition(1))
                print(mousePos)
                if pieceSelected:
                    for piece in pieces:
                        if piece.selected:
                            piece.selected = False
                            pieceSelected = False
                            piece.x = mousePos[0]
                            piece.y = mousePos[1]
                else:
                    for piece in pieces:
                        if mousePos[0] == piece.x and mousePos[1] == piece.y:
                            pieceSelected = True
                            piece.selected = True
                            print(piece)
            if event.type == pygame.KEYDOWN:
                for piece in pieces:
                    print(str(piece.x) + " " + str(piece.y) + " " + str(piece.selected))

        chessGrid.show()

        for piece in pieces:
            piece.show(chessGrid.screen)

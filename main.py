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
    currentPiece = None

    # Game loop
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = (getMousePosition(0), getMousePosition(1))
                print(mousePos)
                if pieceSelected:
                    for piece in pieces:
                        # check if a different piece is selected
                        if mousePos[0] == piece.x and mousePos[1] == piece.y:
                            currentPiece.selected = False
                            piece.selected = True
                            currentPiece = piece
                            currentPiece.getMoves()
                        # removes moves if other pieces are blocking them
                        for i in range(len(currentPiece.possibleMoves)):
                            if currentPiece.possibleMoves[0] == piece.x and currentPiece.possibleMoves[1] == piece.y:
                                currentPiece.possibleMoves.pop(i)
                    for move in currentPiece.possibleMoves:
                        if mousePos[0] == move[0] and mousePos[1] == move[1]:
                            currentPiece.selected = False
                            pieceSelected = False
                            currentPiece.x = mousePos[0]
                            currentPiece.y = mousePos[1]
                            chessGrid.drawGrid()
                else:
                    for piece in pieces:
                        if mousePos[0] == piece.x and mousePos[1] == piece.y:
                            pieceSelected = True
                            piece.selected = True
                            currentPiece = piece
                            currentPiece.getMoves()
                            print(piece)

            if event.type == pygame.KEYDOWN:
                for piece in pieces:
                    print(str(piece.x) + " " + str(piece.y) + " " + str(piece.selected))

        chessGrid.show()

        for piece in pieces:
            piece.show(chessGrid.screen)
            piece.showMoves(chessGrid.screen)
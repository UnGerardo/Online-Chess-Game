import pygame
import math
import pawn as p
import grid


def getMousePosition(value):
    return math.ceil((pygame.mouse.get_pos())[value]/grid.SQUARE_SIZE)


def changePiece(newPiece, piecesArr):
    newPiece.selected = True
    newPiece.getMoves(piecesArr)
    return newPiece


def canMove(piece, mousePos):
    for move in piece.possibleMoves:
        if move and mousePos[0] == move[0] and mousePos[1] == move[1]:
            return True
    return False


def updatePiecesLocation(locations, piece, mousePos):
    locations[piece.x][piece.y] = None
    locations[mousePos[0]][mousePos[1]] = piece


if __name__ == '__main__':
    chessGrid = grid.Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    running = True
    # maybe store all pieces in arr and in object one for looping show() and the object for quick lookup
    pieces = [p.Pawn("bPawn", 1, 7, "images/pawn.png"), p.Pawn("bPawn", 1, 6, "images/pawn.png")]
    pieceLocations = {
        # columns - x - top left (1,1)
        1: {
            # rows - y
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: pieces[1],#p.Pawn("bPawn", 1, 6, "images/pawn.png"),
            7: pieces[0],#p.Pawn("bPawn", 1, 7, "images/pawn.png"),
            8: None
        },
        2: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        3: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        4: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        5: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        6: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        7: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        },
        8: {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None
        }
    }
    # for
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
                # if a piece has been selected
                if pieceSelected:
                    # if the user selects a piece after another, change selection
                    if pieceLocations[mousePos[0]][mousePos[1]]:
                        currentPiece.selected = False
                        currentPiece = changePiece(pieceLocations[mousePos[0]][mousePos[1]], pieces)
                    # else check if desired move is available and move if it is
                    elif canMove(currentPiece, mousePos):
                        pieceSelected = False
                        updatePiecesLocation(pieceLocations, currentPiece, mousePos)
                        currentPiece.move(mousePos)
                # if a piece has not been selected (starting point)
                else:
                    if pieceLocations[mousePos[0]][mousePos[1]]:
                        pieceSelected = True
                        currentPiece = changePiece(pieceLocations[mousePos[0]][mousePos[1]], pieces)

            if event.type == pygame.KEYDOWN:
                print(pieceLocations)
                print(currentPiece.x)
                print(currentPiece.y)
                # for piece in pieces:
                #     print(str(piece.x) + " " + str(piece.y) + " " + str(piece.selected)
                #           + " " + str(piece.possibleMoves)
                #           )

        chessGrid.show()
        chessGrid.drawGrid()  # this refreshes the screen correctly stopping multiple green squares from showing

        for piece in pieces:
            piece.show(chessGrid.screen)
            piece.showMoves(chessGrid.screen)
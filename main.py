import pygame
import math
import pawn as p
import bishop as b
import grid


def getMousePosition(value):
    return math.ceil((pygame.mouse.get_pos())[value]/grid.SQUARE_SIZE)


def changePiece(newPiece, piecesDict):
    newPiece.selected = True
    newPiece.getMoves(piecesDict)
    return newPiece


# pieces like rooks and bishops could use linked lists to store lines of travel; would need to check piece type
def validMove(currPiece, mouseP):
    for move in currPiece.possibleMoves:
        if move and mouseP[0] == move[0] and mouseP[1] == move[1]:
            return True
    return False


def updatePiecesLocation(pieceDict, currPiece, mouseP):
    pieceDict[currPiece.x][currPiece.y] = None
    pieceDict[mouseP[0]][mouseP[1]] = currPiece
    currPiece.move(mouseP)


if __name__ == '__main__':
    chessGrid = grid.Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    pieceLocations = {
        # columns - x - top left (1,1)
        1: {
            # rows - y
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: p.Pawn("bPawn", 1, 6, "images/pawn.png"),
            7: p.Pawn("bPawn", 1, 7, "images/pawn.png"),
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
            5: b.Bishop('bBishop', 5, 5, "images/bishop.png"),
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
    mousePos = (0, 0)
    pieceSelected = False
    currentPiece = None # :: see if could ever be undefined and used
    playing = True
    # Game loop
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            # on click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = (getMousePosition(0), getMousePosition(1))
                space = pieceLocations[mousePos[0]][mousePos[1]]

                # if a piece has been selected; change selection or move
                if pieceSelected:

                    # if the user selects a piece after another, change selection
                    if space:
                        currentPiece.selected = False
                        currentPiece = changePiece(space, pieceLocations)

                    # else check if desired move is valid and move if it is
                    elif validMove(currentPiece, mousePos):
                        pieceSelected = False
                        updatePiecesLocation(pieceLocations, currentPiece, mousePos)

                # if a piece has not been selected (starting point)
                else:
                    if space:
                        pieceSelected = True
                        currentPiece = changePiece(space, pieceLocations)

            if event.type == pygame.KEYDOWN:
                print(pieceLocations)
                print(currentPiece.x)
                print(currentPiece.y)
                print(currentPiece.possibleMoves[0].head)

        chessGrid.show()
        chessGrid.drawGrid()  # this refreshes the screen correctly stopping multiple green squares from showing

        # loops through pieceLocations dict to show pieces
        for col in range(8):
            for row in range(8):
                piece = pieceLocations[col+1][row+1]
                if piece:
                    piece.show(chessGrid.screen)
                    piece.showMoves(chessGrid.screen)
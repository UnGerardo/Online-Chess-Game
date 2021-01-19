import pygame
import math
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King
from grid import Grid, SQUARE_SIZE


def getMousePosition(value):
    return math.ceil((pygame.mouse.get_pos())[value]/SQUARE_SIZE)


def changePiece(newPiece, piecesDict):
    newPiece.selected = True
    newPiece.getMoves(piecesDict)
    return newPiece


def updatePiecesLocation(pieceDict, currPiece, mouseP, screen):
    pieceDict[currPiece.x][currPiece.y] = None
    currPiece.move(mouseP)
    if isinstance(currPiece, Pawn):
        currPiece.firstMove = False
        if currPiece.y == 8 or currPiece.y == 1:
            currPiece = switchOutPawn(currPiece, screen)
    pieceDict[mouseP[0]][mouseP[1]] = currPiece


def switchOutPawn(currPiece, screen):
    screen.blit(switchText, (75, 280))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if currPiece.color:
                        return Queen(currPiece.x, currPiece.y, "images/whiteQueen.png", 1)
                    else:
                        return Queen(currPiece.x, currPiece.y, "images/blackQueen.png", 0)
                if event.key == pygame.K_r:
                    if currPiece.color:
                        return Rook(currPiece.x, currPiece.y, "images/whiteRook.png", 1)
                    else:
                        return Rook(currPiece.x, currPiece.y, "images/blackRook.png", 0)
                if event.key == pygame.K_b:
                    if currPiece.color:
                        return Bishop(currPiece.x, currPiece.y, "images/whiteBishop.png", 1)
                    else:
                        return Bishop(currPiece.x, currPiece.y, "images/blackBishop.png", 0)
                if event.key == pygame.K_k:
                    if currPiece.color:
                        return Knight(currPiece.x, currPiece.y, "images/whiteKnight.png", 1)
                    else:
                        return Knight(currPiece.x, currPiece.y, "images/blackKnight.png", 0)


if __name__ == '__main__':
    pygame.init()
    chessGrid = Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    gameState = {
        # columns - x - top left (1,1)
        1: {
            # rows - y
            1: Rook(1, 1, "images/blackRook.png", 0),
            2: Pawn(1, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(1, 7, "images/whitePawn.png", 1),
            8: Rook(1, 8, "images/whiteRook.png", 1)
        },
        2: {
            1: Knight(2, 1, "images/blackKnight.png", 0),
            2: Pawn(2, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(2, 7, "images/whitePawn.png", 1),
            8: Knight(2, 8, "images/whiteKnight.png", 1)
        },
        3: {
            1: Bishop(3, 1, "images/blackBishop.png", 0),
            2: Pawn(3, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(3, 7, "images/whitePawn.png", 1),
            8: Bishop(3, 8, "images/whiteBishop.png", 1)
        },
        4: {
            1: Queen(4, 1, "images/blackQueen.png", 0),
            2: Pawn(4, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(4, 7, "images/whitePawn.png", 1),
            8: Queen(4, 8, "images/whiteQueen.png", 1)
        },
        5: {
            1: King(5, 1, "images/blackKing.png", 0),
            2: Pawn(5, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(5, 7, "images/whitePawn.png", 1),
            8: King(5, 8, "images/whiteKing.png", 1)
        },
        6: {
            1: Bishop(6, 1, "images/blackBishop.png", 0),
            2: Pawn(6, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(6, 7, "images/whitePawn.png", 1),
            8: Bishop(6, 8, "images/whiteBishop.png", 1)
        },
        7: {
            1: Knight(7, 1, "images/blackKnight.png", 0),
            2: Pawn(7, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(7, 7, "images/whitePawn.png", 1),
            8: Knight(7, 8, "images/whiteKnight.png", 1)
        },
        8: {
            1: Rook(8, 1, "images/blackRook.png", 0),
            2: Pawn(8, 2, "images/blackPawn.png", 0),
            3: None,
            4: None,
            5: None,
            6: None,
            7: Pawn(8, 7, "images/whitePawn.png", 1),
            8: Rook(8, 8, "images/whiteRook.png", 1)
        }
    }
    gameFont = pygame.font.Font('font/Roboto-Regular.ttf', 18)
    switchText = gameFont.render('Press Q, R, B, or K: Q - Queen R - Rook B - Bishop K - Knight',
                                 True, (255, 255, 255), (0, 0, 0))
    pieceSelected = False
    currentPiece = None  # :: see if could ever be undefined and used
    colorWin = ''
    playing = True
    # Game loop
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if not colorWin:
                # on click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = (getMousePosition(0), getMousePosition(1))
                    space = gameState[mousePos[0]][mousePos[1]]

                    # if a piece has been selected; change selection or move
                    if pieceSelected:

                        # if desired move is valid and move if it is, needs to check this first to capture pieces
                        if currentPiece.validMove(mousePos):
                            pieceSelected = False
                            # checks if a king was taken
                            if isinstance(gameState[mousePos[0]][mousePos[1]], King):
                                if gameState[mousePos[0]][mousePos[1]].color:
                                    colorWin = 'Black'
                                else:
                                    colorWin = 'White'
                            gameState[mousePos[0]][mousePos[1]] = None
                            updatePiecesLocation(gameState, currentPiece, mousePos, chessGrid.screen)

                        # else if the user selects a piece after another, change selection
                        elif space:
                            currentPiece.selected = False
                            currentPiece = changePiece(space, gameState)

                    # if a piece has not been selected (starting point)
                    else:
                        if space:
                            pieceSelected = True
                            currentPiece = changePiece(space, gameState)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        print(currentPiece.direction)

        chessGrid.show()
        chessGrid.drawGrid()  # this refreshes the screen correctly stopping multiple green squares from showing

        # loops through gameState dict to show pieces
        for col in range(8):
            for row in range(8):
                piece = gameState[col + 1][row + 1]
                if piece:
                    piece.show(chessGrid.screen)
                    if piece.selected:
                        piece.showMoves(chessGrid.screen)
        if colorWin:
            winText = gameFont.render(f'{colorWin} won!', True, (255, 255, 255), (0, 0, 0))
            chessGrid.screen.blit(winText, (75, 280))
            pygame.display.update()

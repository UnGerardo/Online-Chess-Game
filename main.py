import pygame
import jsonpickle
import math
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.king import King
from network import Network
from grid import Grid, SQUARE_SIZE


def getMousePosition(value):
    return math.ceil((pygame.mouse.get_pos())[value] / SQUARE_SIZE)


def changePiece(newPiece, piecesDict):
    newPiece.selected = True
    newPiece.getMoves(piecesDict)
    return newPiece


def updatePiecesLocation(pieceDict, currPiece, mouseP, screen):
    pieceDict[f'{currPiece.x}'][f'{currPiece.y}'] = None
    currPiece.move(mouseP)
    if isinstance(currPiece, Pawn):
        currPiece.firstMove = False
        if currPiece.y == 8 or currPiece.y == 1:
            currPiece = switchOutPawn(currPiece, screen)
    pieceDict[f'{mouseP[0]}'][f'{mouseP[1]}'] = currPiece


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


def send_data(network, gameState, temp):
    data = jsonpickle.encode(gameState)
    reply = network.send(f'{temp[0]}=' + data)
    temp[0] = network.id
    return reply


def parse_data(gameState):
    try:
        return jsonpickle.decode(gameState)
    except:
        return {}


if __name__ == '__main__':
    pygame.init()
    chessGrid = Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    net = Network()
    # lets players switch turn by sending opponents ID when turn changes so they match and gameState saves (server 122)
    temp = [net.id]
    gameState = {
        '1': {
            '1': Rook(1, 1, 'images/blackRook.png', 1),
            '2': Pawn(1, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(1, 7, 'images/whitePawn.png', 0),
            '8': Rook(1, 8, 'images/whiteRook.png', 0)
        },
        '2': {
            '1': Knight(2, 1, 'images/blackKnight.png', 1),
            '2': Pawn(2, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(2, 7, 'images/whitePawn.png', 0),
            '8': Knight(2, 8, 'images/whiteKnight.png', 0)
        },
        '3': {
            '1': Bishop(3, 1, 'images/blackBishop.png', 1),
            '2': Pawn(3, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(3, 7, 'images/whitePawn.png', 0),
            '8': Bishop(3, 8, 'images/whiteBishop.png', 0)
        },
        '4': {
            '1': Queen(4, 1, 'images/blackQueen.png', 1),
            '2': Pawn(4, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(4, 7, 'images/whitePawn.png', 0),
            '8': Queen(4, 8, 'images/whiteQueen.png', 0)
        },
        '5': {
            '1': King(5, 1, 'images/blackKing.png', 1),
            '2': Pawn(5, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(5, 7, 'images/whitePawn.png', 0),
            '8': King(5, 8, 'images/whiteKing.png', 0)
        },
        '6': {
            '1': Bishop(6, 1, 'images/blackBishop.png', 1),
            '2': Pawn(6, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(6, 7, 'images/whitePawn.png', 0),
            '8': Bishop(6, 8, 'images/whiteBishop.png', 0)
        },
        '7': {
            '1': Knight(7, 1, 'images/blackKnight.png', 1),
            '2': Pawn(7, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(7, 7, 'images/whitePawn.png', 0),
            '8': Knight(7, 8, 'images/whiteKnight.png', 0)
        },
        '8': {
            '1': Rook(8, 1, 'images/blackRook.png', 1),
            '2': Pawn(8, 2, 'images/blackPawn.png', 1),
            '3': None,
            '4': None,
            '5': None,
            '6': None,
            '7': Pawn(8, 7, 'images/whitePawn.png', 0),
            '8': Rook(8, 8, 'images/whiteRook.png', 0)
        },
        'colorWin': '',
        'turn': '0'
    }
    gameFont = pygame.font.Font('font/Roboto-Regular.ttf', 18)
    switchText = gameFont.render('Press Q, R, B, or K: Q - Queen R - Rook B - Bishop K - Knight',
                                 True, (255, 255, 255), (0, 0, 0))
    pieceSelected = False
    currentPiece = None
    playing = True
    # Game loop
    while playing:
        gameState = parse_data(send_data(net, gameState, temp))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False

            if (not gameState['colorWin']) and gameState['turn'] == net.id:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = (getMousePosition(0), getMousePosition(1))
                    space = gameState[f'{mousePos[0]}'][f'{mousePos[1]}']

                    # if a piece has been selected; change selection or move
                    if pieceSelected:

                        # if desired move is valid and move if it is, needs to check this first to capture pieces
                        if currentPiece.validMove(mousePos):
                            pieceSelected = False
                            # checks if a king was taken
                            if isinstance(gameState[f'{mousePos[0]}'][f'{mousePos[1]}'], King):
                                if gameState[f'{mousePos[0]}'][f'{mousePos[1]}'].color:
                                    gameState['colorWin'] = 'White'
                                else:
                                    gameState['colorWin'] = 'Black'
                            gameState[f'{mousePos[0]}'][f'{mousePos[1]}'] = None
                            updatePiecesLocation(gameState, currentPiece, mousePos, chessGrid.screen)
                            if gameState['turn'] == '0':
                                gameState['turn'] = '1'
                                temp[0] = '1'
                            else:
                                gameState['turn'] = '0'
                                temp[0] = '0'

                        # else if the user selects a piece after another, change selection
                        elif space and (f'{space.color}' == gameState['turn']):
                            currentPiece.selected = False
                            currentPiece = changePiece(space, gameState)

                    # if a piece has not been selected (starting point)
                    else:
                        if space and (f'{space.color}' == gameState['turn']):
                            pieceSelected = True
                            currentPiece = changePiece(space, gameState)

        chessGrid.show()
        chessGrid.drawGrid()

        # loops through gameState dict to show pieces
        for col in range(8):
            for row in range(8):
                piece = gameState[f'{col + 1}'][f'{row + 1}']
                if piece:
                    piece.show(chessGrid.screen)
                    if piece.selected and (gameState['turn'] == net.id) and (f'{piece.color}' == net.id):
                        # moves shown continually because when piece selection is saved in server
                        piece.showMoves(chessGrid.screen)
        if gameState['colorWin']:
            winText = gameFont.render(f"{gameState['colorWin']} won!", True, (255, 255, 255), (0, 0, 0))
            chessGrid.screen.blit(winText, (75, 280))
            pygame.display.update()

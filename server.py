import socket
from _thread import *

# this creates a socket object with the arguments to use the address family 'IPv4' and the socket type for TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# this is the IP address to send requests to and unused port to listen on
server = socket.gethostbyname(socket.gethostname())
port = 5555

# id separating connections, 0 will be white and 1 will be black
currentId = "0"
gameState = """{
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
    }"""


def threaded_client(connection):
    global currentId, gameState
    # send id to client
    connection.send(str.encode(currentId))
    currentId = "1"
    while True:
        data = b''
        try:
            # receive data from client - need loop to get entirety of data (too big)
            while True:
                chunk = connection.recv(2048)
                data += chunk
                if len(chunk) < 2048:
                    # either 0 or end of data
                    break

            # decode data into string and store in gameData, if turn of client sending data - store
            # place id of client in front of data and access it to compare whose turn it is
            gameData = data.decode()
            gameData = gameData.split('=')
            gameArr = gameData[1].split(',')
            turn = (gameArr[len(gameArr)-1]).split(':')
            # when white (0) makes a move and 'turn' changes to 1 the gameState isn't saved so white moves again
            if turn[1][2] == gameData[0]:
                gameState = gameData[1]
            # if no data is received break connection
            if not data:
                connection.send(str.encode("Goodbye"))
                break

            # send reply from client to others - args need to be bytes
            connection.sendall(str.encode(gameState))
        except:
            print('wrong')
            break

    print("Connection Closed")
    connection.close()


try:
    # bind associates the socket object with the network interface and port
    s.bind((server, port))

except socket.error as e:
    print(str(e))

# listen allows the socket to accept connections and arg only allows a max of 2 connections
s.listen(2)
print("Waiting for a connection")


while True:
    # s.accept will wait until it gets a connection, we get address and socket obj 'conn' to send data back
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))

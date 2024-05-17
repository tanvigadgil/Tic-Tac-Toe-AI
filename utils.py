BOARD_WIDTH = 3
BOARD_HEIGHT = 3
DEPTH = 4 # Max depth till which the algorithm should evaluate

ROWS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)]
]

COLUMNS = [
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)]
]

DIAGONALS = [
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

def getOpponent(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"

def getAllLegalMoves(board):
    legalMoves = []

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[x][y] == None:
                legalMoves.append((x, y))
    
    return legalMoves
BOARD_WIDTH = 3
BOARD_HEIGHT = 3

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


def newBoard():
    # board = [
    #     [None, None, None],
    #     [None, None, None],
    #     [None, None, None]
    # ]

    board = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    return board


def render(board):
    print("  0 1 2")
    print(" --------")

    for i in range(BOARD_HEIGHT):
        row = ""
        for sq in board[i]:
            if sq is None:
                row += "_"
            else:
                row += sq

        print(str(i) + "|" + " ".join(row))
    print(" --------")

def getMove():
    moveX = int(input("Enter your move's X co-ordinate: "))
    moveY = int(input("Enter your move's Y co-ordinate: "))
    return (moveX, moveY)  # Should be immutable

def isValidMove(board, coords):
    if board[coords[0]][coords[1]] is not None or not (0 <= coords[0] < BOARD_HEIGHT) or not (0 <= coords[1] < BOARD_WIDTH):
        return False
    return True

def makeMove(board, coords, player):
    if not isValidMove(board, coords):
        print("Invalid move, try again")
        return
    board[coords[0]][coords[1]] = player

# Convert into set (does not contain duplicates) and check the length
def getWinner(board):
    allLines = ROWS + COLUMNS + DIAGONALS

    for line in allLines:
        lineValues = [board[x][y] for (x, y) in line]
        if len(set(lineValues)) == 1 and lineValues[0] is not None:
            return lineValues[0]
    
    return None

def isBoardFull(board):
    for col in board:
        for row in col:
            if row is None:
                return False
    return True 

# board = newBoard()
# board[0][0] = "X"
# board[1][0] = "X"
# board[2][0] = "X"
# render(board)
# print(getWinner(board))
# moveCoords = getMove()
# print(moveCoords)
# makeMove(board, moveCoords, "O")
# render(board)
# print(getWinner(board))
# moveCoords_1 = (0, 0)
# makeMove(board, moveCoords_1, "X")
# render(board)
# print(getWinner(board))

def play():
    players = ["X", "O"]
    turnNum = 0
    board = newBoard()
    moveCoords = None

    while True:
        currentPlayer = players[turnNum % 2]
        render(board)
        print(currentPlayer, "'s turn:")

        moveCoords = getMove()
        makeMove(board, moveCoords, currentPlayer)
        winner = getWinner(board)

        if winner is not None:
            render(board)
            print("The winner is ", winner)
            break

        if isBoardFull(board):
            render(board)
            print("It's a DRAW!")
            break

        turnNum += 1

play()
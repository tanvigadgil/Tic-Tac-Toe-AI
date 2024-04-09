BOARD_WIDTH = 3
BOARD_HEIGHT = 3


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
    if board[coords[0]][coords[1]] is not None or coords[0] not in (0, 2) or coords[1] not in (0, 2):
        return False
    return True

def makeMove(board, coords, player):
    board[coords[0]][coords[1]] = player


board = newBoard()
board[0][1] = "X"
board[1][1] = "O"
board[1][0] = "X"
render(board)
moveCoords = getMove()
print(moveCoords)
makeMove(board, moveCoords, "O")
render(board)
moveCoords_1 = (0, 0)
makeMove(board, moveCoords_1, "X")
render(board)

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
        if not isValidMove(board, moveCoords):
            print("Invalid move, try again")
            continue

        makeMove(board, moveCoords, currentPlayer)

        turnNum += 1

play()
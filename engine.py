BOARD_WIDTH = 3
BOARD_HEIGHT = 3


def new_board():
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


board = new_board()
board[0][1] = "X"
board[1][1] = "O"
board[1][0] = "X"
render(board)

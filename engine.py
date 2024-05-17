import utils
import heuristic as ai

import sys

def newBoard():
    # board = [
    #     [None, None, None],
    #     [None, None, None],
    #     [None, None, None]
    # ]

    board = [[None for _ in range(utils.BOARD_WIDTH)] for _ in range(utils.BOARD_HEIGHT)]
    return board


def render(board):
    print("  0 1 2")
    print(" --------")

    for i in range(utils.BOARD_HEIGHT):
        row = ""
        for sq in board[i]:
            if sq is None:
                row += "_"
            else:
                row += sq

        print(str(i) + "|" + " ".join(row))
    print(" --------")

def getMove(board, currentPlayer, player):
    if player == "human":
        moveX = int(input("Enter your move's X co-ordinate: "))
        moveY = int(input("Enter your move's Y co-ordinate: "))
        return (moveX, moveY)  # Should be immutable
    elif player == "ai":
        aiOutput = ai.bestMove(board, currentPlayer, currentPlayer)
        # aiOutput = ai.minimax_ai(board, currentPlayer)
        print("Output:", aiOutput)
        return aiOutput

def isValidMove(board, coords):
    if board[coords[0]][coords[1]] is not None or not (0 <= coords[0] < utils.BOARD_HEIGHT) or not (0 <= coords[1] < utils.BOARD_WIDTH):
        return False
    return True

def makeMove(board, coords, player):
    if not isValidMove(board, coords):
        print("Invalid move, try again")
        return
    board[coords[0]][coords[1]] = player

# Convert into set (does not contain duplicates) and check the length
def getWinner(board):
    allLines = utils.ROWS + utils.COLUMNS + utils.DIAGONALS

    for line in allLines:
        lineValues = [board[x][y] for (x, y) in line]
        if len(set(lineValues)) == 1 and lineValues[0] is not None:
            return lineValues[0]
    
    return None

# TODO: Optimize this
def isBoardFull(board):
    # for col in board:
    #     for row in col:
    #         if row is None:
    #             return False
    # return True 
    return all([cell != None for row in board for cell in row])

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

def play(player1, player2):
    players = [("X", player1),
               ("O", player2)
               ]
    turnNum = 0
    board = newBoard()
    moveCoords = None

    while True:
        currentPlayer, player = players[turnNum % 2]
        render(board)
        print(currentPlayer, "'s turn:")

        moveCoords = getMove(board, currentPlayer, player)
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


def main():
    player1 = input("Player for 'X' (human / AI):").lower()
    player2 = input("Player for 'O' (human / AI):").lower()
    play(player1, player2)
    

if __name__ == "__main__":
    main()    
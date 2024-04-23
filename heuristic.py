import engine as en
import utils

def minimaxScore(board, currentPlayer, optimizePlayer):
    winner = en.getWinner(board)
    if winner is not None:
        if winner == optimizePlayer:
            return 10
        else:
            return -10
    elif en.isBoardFull(board):
        return 0
    
    legalMoves = utils.getAllLegalMoves(board)
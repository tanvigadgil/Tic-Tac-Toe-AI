import engine as en
import utils

def minimax(board, depth, currentPlayer, optimizingPlayer, alpha, beta):
    winner = en.getWinner(board)
    opponent = utils.getOpponent(currentPlayer)

    if depth == utils.DEPTH or en.isBoardFull(board):
        return 0
    elif winner == optimizingPlayer:
        return 10 - depth
    elif winner == opponent:
       return depth - 10

    if currentPlayer == optimizingPlayer:
        maxEval = float("-inf")

        for (x, y) in utils.getAllLegalMoves(board):
            board[x][y] = currentPlayer
            eval = minimax(board, depth + 1, opponent, optimizingPlayer, alpha, beta)
            board[x][y] = None
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha: # Pruning it
                break
        return maxEval
    else:
        minEval = float("inf")

        for (x, y) in utils.getAllLegalMoves(board):
            board[x][y] = currentPlayer
            eval = minimax(board, depth + 1, opponent, optimizingPlayer, alpha, beta)
            board[x][y] = None
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha: # Pruning it
                break
        return minEval
        

def bestMove(board, currentPlayer, optimizingPlayer):
    bestScore = float("-inf") if currentPlayer == optimizingPlayer else float("inf")
    bestMove = None
    opponent = utils.getOpponent(board)
    alpha = float("-inf")
    beta = float("inf")

    for (x, y) in utils.getAllLegalMoves(board):
        board[x][y] = currentPlayer
        moveScore = minimax(board, 0, opponent, optimizingPlayer, alpha, beta)
        board[x][y] = None

        if (currentPlayer == optimizingPlayer and moveScore > bestScore) or \
        (currentPlayer != optimizingPlayer and moveScore < bestScore):
            bestScore = moveScore
            bestMove = (x, y)

    return bestMove
    
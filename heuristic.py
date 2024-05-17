import engine as en
import utils

import copy

def alphaBetaPruning(board, currentPlayer):
    bestMove = None
    bestScore = None

    alpha = float("-inf")
    beta = float("inf")

    for move in utils.getAllLegalMoves(board):
        _board = copy.deepcopy(board)
        en.makeMove(_board, move, currentPlayer)

        opponent = utils.getOpponent(currentPlayer)
        score = minimaxScore(_board, opponent, currentPlayer, alpha, beta)

        if bestScore is None or score > bestScore:
            bestScore = score
            bestMove = move
        alpha = max(alpha, bestScore)
        if beta <= alpha:
            break
    return bestMove

def minimaxScore(board, currentPlayer, optimizePlayer, alpha, beta):
    winner = en.getWinner(board)
    if winner is not None:
        if winner == optimizePlayer:
            return 10
        else:
            return -10
    elif en.isBoardFull(board):
        return 0
    
    legalMoves = utils.getAllLegalMoves(board)

    if currentPlayer == optimizePlayer:
        bestScore = float("-inf")
        for move in legalMoves:
            _board = copy.deepcopy(board) # Creates new object and recursively populates with copies
            en.makeMove(_board, move, currentPlayer)

            opponent = utils.getOpponent(currentPlayer)
            score = minimaxScore(_board, opponent, optimizePlayer, alpha, beta)
            bestScore = max(bestScore, score)
            alpha = max(alpha, bestScore)

            if beta <= alpha:
                break # Cutting off beta
        return bestScore
    else:
        bestScore = float("-inf")
        for move in legalMoves:
            _board = copy.deepcopy(board) # Creates new object and recursively populates with copies
            en.makeMove(_board, move, currentPlayer)

            opponent = utils.getOpponent(currentPlayer)
            score = minimaxScore(_board, opponent, optimizePlayer, alpha, beta)
            bestScore = min(bestScore, score)
            alpha = min(alpha, bestScore)

            if beta <= alpha:
                break # Cutting off alpha
        return bestScore
    

def minimax_ai(board, who_am_i):
    best_move = None
    best_score = None

    for move in utils.getAllLegalMoves(board):
        _board = copy.deepcopy(board)
        en.makeMove(_board, move, who_am_i)

        opp = utils.getOpponent(who_am_i)
        score = _minimax_score(_board, opp, who_am_i)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move


def _minimax_score(board, player_to_move, player_to_optimize):
    winner = en.getWinner(board)
    if winner is not None:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif en.isBoardFull(board):
        return 0

    legal_moves = utils.getAllLegalMoves(board)

    scores = []
    for move in legal_moves:
        _board = copy.deepcopy(board)
        en.makeMove(_board, move, player_to_move)

        opp = utils.getOpponent(player_to_move)
        opp_best_response_score = _minimax_score(_board, opp, player_to_optimize)
        scores.append(opp_best_response_score)

    if player_to_move == player_to_optimize:
        return max(scores)
    else:
        return min(scores)
    


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
    
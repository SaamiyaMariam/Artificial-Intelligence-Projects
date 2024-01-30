"""
Tic Tac Toe Player using Minimax and Alpha-Beta Pruning
"""

import copy
import math
import random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in board:
        for j in i:
            if j:
                count += 1
    if count % 2 != 0:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()
    board_len = len(board)
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j] == EMPTY:
                res.add((i, j))
    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    curr_player = player(board)
    result_board = copy.deepcopy(board)
    (i, j) = action
    result_board[i][j] = curr_player
    return result_board

def get_horizontal_winner(board):
    # check horizontally
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val = board[i][0]
        for j in range(board_len):
            if board[i][j] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_vertical_winner(board):
    # check vertically
    winner_val = None
    board_len = len(board)
    for i in range(board_len):
        winner_val = board[0][i]
        for j in range(board_len):
            if board[j][i] != winner_val:
                winner_val = None
        if winner_val:
            return winner_val
    return winner_val

def get_diagonal_winner(board):
    # check diagonally
    winner_val = None
    board_len = len(board)
    winner_val = board[0][0]
    for i in range(board_len):
        if board[i][i] != winner_val:
            winner_val = None
    if winner_val:
        return winner_val

    winner_val = board[0][board_len - 1]
    for i in range(board_len):
        j = board_len - 1 - i
        if board[i][j] != winner_val:
            winner_val = None

    return winner_val

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_val = get_horizontal_winner(board) or get_vertical_winner(board) or get_diagonal_winner(board) or None
    return winner_val

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_val = winner(board)
    if winner_val == X:
        return 1
    elif winner_val == O:
        return -1
    return 0

# Minimax algorithm
def max_val(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v

def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return random.choice(list(actions(board)))

    curr_player = player(board)
    if curr_player == X:
        value = -math.inf
        action_to_return = None
        for action in actions(board):
            answer = min_val(result(board, action))
            if answer > value:
                value = answer
                action_to_return = action
    else:
        value = math.inf
        action_to_return = None
        for action in actions(board):
            result = max_val(result(board, action))
            if answer < value:
                value = answer
                action_to_return = action

    return action_to_return

# Alpha-Beta Pruning algorithm
def max_val(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_val(result(board, action), alpha, beta))
        if alpha >= value:
            return value
        alpha = max(alpha, value)
    return value

def min_val(board, alpha, beta):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_val(result(board, action), alpha, beta))
        if beta <= value:
            return value
        beta = min(beta, value)
    return value

def alpha_beta(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board == initial_state():
        return random.choice(list(actions(board)))

    curr_player = player(board)
    alpha = -math.inf
    beta = math.inf
    action_to_return = None

    if curr_player == X:
        value = -math.inf
        for action in actions(board):
            val = min_val(result(board, action), alpha, beta)
            if val > value:
                value = val
                action_to_return = action
            alpha = max(alpha, value)
    else:
        value = math.inf
        for action in actions(board):
            val = max_val(result(board, action), alpha, beta)
            if val < value:
                value = val
                action_to_return = action
            beta = min(beta, value)

    return action_to_return

if __name__ == "__main__":
    user = None
    board = initial_state()

    while not terminal(board):
        print_board(board)
        print("Player", player(board), "'s turn")
        if player(board) == X:
            action = minimax(board)
        else:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                action = (row, col)
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

        if action not in actions(board):
            print("Invalid move. Try again.")
            continue

        board = result(board, action)

    print_board(board)
    print("Game over.")
    if winner(board) is not None:
        print("Player", winner(board), "wins!")
    else:
        print("It's a tie!")

"""
Tic Tac Toe Player
"""

import math

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
    cells = [*board[0], *board[1], *board[2]]
    # cells = [cell for row in board for cell in row]
    return X if cells.count(X) == cells.count(O) else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i,j) for i,row in enumerate(board) for j,cell in enumerate(row) if cell == EMPTY]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    board[i][j] = player(board)
    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][1] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != EMPTY:
        return board[2][0]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    number = sum(1 for row in board for cell in row if cell == EMPTY)
    return (bool(winner(board)) or number == 0)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError

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
    return {(i,j) for i,row in enumerate(board) for j,cell in enumerate(row) if cell == EMPTY}

def result(board, action):
    """
    The result function takes a board and an action as input, and should return a new board state, without modifying the original board.
    If action is not a valid action for the board, your program should raise an exception.
    The returned board state should be the board that would result from taking the original input board, 
    and letting the player whose turn it is make their move at the cell indicated by the input action.
    Importantly, the original board should be left unmodified: since Minimax will ultimately require considering many different board states during its computation. 
    This means that simply updating a cell in board itself is not a correct implementation of the result function. 
    You'll likely want to make a deep copy of the board first before making any changes.
    """
    if action in actions(board):
        new_board = [row[:] for row in board]
        i, j = action
        new_board[i][j] = player(board)
        return new_board
    else:
        raise Exception("Not a valid action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
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
    It takes a board as input, and return the optimal move for the player to move on that board.
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
    """
    if terminal(board):
        return None
    move = None
    if player(board) == "X":
        v = float("-inf")
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > v:
                v = new_value
                move = action
    else:
        v = float("inf")
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < v:
                v = new_value
                move = action
    return move


def min_value(board):
    """
    Returns the minimum value among all actions
    """
    if terminal(board):
        return utility(board)
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    """
    Returns the maximum value among all actions
    """
    if terminal(board):
        return utility(board)
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


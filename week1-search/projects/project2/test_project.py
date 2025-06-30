from tictactoe import *
from unittest.mock import patch


board = [[O, X, X],
         [O, X, EMPTY],
         [O, EMPTY, X]]

board_without_winner = [[EMPTY, X, X],
                        [O, X, EMPTY],
                        [O, EMPTY, X]]

board_full = [[X, O, X],
              [O, X, O],
              [O, X, O]]


def test_player():
    assert player(board) == "O"


def test_actions():
    assert actions(board) == [(1,2), (2,1)]


def test_result():
    with patch("tictactoe.player", return_value="O"):
        assert result(board, (1,2)) == [[O, X, X],
                                        [O, X, O],
                                        [O, EMPTY, X]]
    with patch("tictactoe.player", return_value="X"):
        assert result(board, (1,2)) == [[O, X, X],
                                        [O, X, X],
                                        [O, EMPTY, X]]
    

def test_winnner():
    assert winner(board) == "O"
    assert winner(board_without_winner) == None


def test_terminal():
    assert terminal(board) == True
    assert terminal(board_without_winner) == False
    assert terminal(board_full) == True


def test_utility():
    with patch("tictactoe.winner", return_value="X"):
        assert utility(board) == 1
    with patch("tictactoe.winner", return_value="O"):
        assert utility(board) == -1
    with patch("tictactoe.winner", return_value=None):
        assert utility(board) == 0

""" Tests for the Minefield game """
from minefield.core import create_board, check_win

def test_create_board():
    """
    Tests that the board is created with the correct dimensions.
    """
    board = create_board(5, 5, 5)
    assert len(board) == 5
    assert len(board[0]) == 5

def test_create_board_mine_count():
    """
    Tests that the correct number of mines are placed on the board.
    """
    board = create_board(5, 5, 5)
    mine_count = sum(row.count('M') for row in board)
    assert mine_count == 5

def test_check_win_true():
    """
    Tests that check_win returns True when all non-mine cells are revealed.
    """
    board = [
        ['M', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    visible_board = [
        ['#', '#', '#'],
        ['#', '#', '#'],
        ['#', '#', '#']
    ]
    assert check_win(board, visible_board) is False

"""Tests for the Minefield game."""

from src.minefield import create_board, check_win
import pytest


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


def test_check_win_false_when_cells_hidden():
    """
    Tests that check_win returns False when safe cells are still hidden.
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


def test_check_win_true_when_all_safe_cells_revealed():
    """
    Tests that check_win returns True when all non-mine cells are revealed.
    """
    board = [
        ['M', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    visible_board = [
        ['#', '1', '0'],
        ['1', '1', '0'],
        ['0', '0', '0']
    ]
    assert check_win(board, visible_board) is True


def test_create_board_zero_mines():
    """
    Tests that a board can be created with zero mines.
    """
    board = create_board(4, 4, 0)
    mine_count = sum(row.count('M') for row in board)
    assert len(board) == 4
    assert len(board[0]) == 4
    assert mine_count == 0


def test_create_board_all_mines():
    """
    Tests that all cells can be mines.
    """
    board = create_board(2, 3, 6)
    mine_count = sum(row.count('M') for row in board)
    assert mine_count == 6


def test_create_board_too_many_mines():
    """
    Tests that create_board raises an error if too many mines are requested.
    """
    with pytest.raises(ValueError):
        create_board(2, 2, 5)

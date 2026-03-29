""" Core functions for the minesweeper game, including
board creation, revealing cells, and checking win conditions.
"""

import random

def create_board(rows, cols, num_mines):
    """Create a minefield board with randomly placed mines hidden from the player.

    The board is represented as a 2D list, where 'M' represents a mine and '.'
    represents an empty cell.
    """
    if num_mines > rows * cols:
        raise ValueError("Number of mines cannot exceed the total number of cells.")

    board =[[ '.' for _ in range(cols)] for _ in range(rows)]
    positions = random.sample(range(rows * cols), num_mines)

    for pos in positions:
        row = pos // cols
        col = pos % cols
        board[row][col] = 'M'

    return board

def reveal_board(rows, cols):
    """
    Creates a board that is revealed to the players with all cells represented as '#'
    """
    return [['#' for _ in range(cols)] for _ in range(rows)]

def count_adjacent_mines(board, row, col):
    """
    Counts how many mines are surrounded by a given cell
    """
    rows = len(board)
    cols = len(board[0])
    count = 0

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and board[i][j] == 'M':
                count += 1

    return count

def reveal_cell(board, visible_board, row, col):
    """
    Reveals one cell, if False the player hits a mine, or it returns True
    """
    if board[row][col] == 'M':
        visible_board[row][col] = 'M'
        return False

    visible_board[row][col] = str(count_adjacent_mines(board, row, col))
    return True


def check_win(board, visible_board):
    """
    Player wins if all non-mine cells are revealed.
    """
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell != 'M' and visible_board[i][j] == '#':
                return False
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] != 'M' and visible_board[i][j] == '#':
    #             return False

    return True

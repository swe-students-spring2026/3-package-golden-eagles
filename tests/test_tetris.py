import pathlib
import sys

import pytest


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

from tetris.core import (
    clear_full_rows,
    create_board,
    is_valid_position,
    place_piece,
    rotate_piece,
    spawn_piece,
)


def test_create_board_defaults():
    board = create_board(6, 8)

    assert len(board) == 6
    assert len(board[0]) == 8
    assert all(cell == 0 for row in board for cell in row)


def test_create_board_invalid_dimensions():
    with pytest.raises(ValueError):
        create_board(3, 8)

    with pytest.raises(ValueError):
        create_board(8, 3)


def test_create_board_invalid_types():
    with pytest.raises(TypeError):
        create_board("6", 8)

    with pytest.raises(TypeError):
        create_board(6, None)


def test_spawn_piece_valid_types():
    t_piece = spawn_piece("T")
    o_piece = spawn_piece("O")
    i_piece = spawn_piece("I")

    assert t_piece == [[0, 1, 0], [1, 1, 1]]
    assert o_piece == [[1, 1], [1, 1]]
    assert i_piece == [[1, 1, 1, 1]]


def test_spawn_piece_case_insensitive():
    assert spawn_piece("t") == spawn_piece("T")
    assert spawn_piece(" o ") == spawn_piece("O")


def test_spawn_piece_invalid_type():
    with pytest.raises(ValueError):
        spawn_piece("X")

    with pytest.raises(TypeError):
        spawn_piece(123)


def test_rotate_piece_t_piece():
    piece = [[0, 1, 0], [1, 1, 1]]
    rotated = rotate_piece(piece)

    assert rotated == [[1, 0], [1, 1], [1, 0]]
    assert len(rotated) == 3
    assert len(rotated[0]) == 2


def test_rotate_piece_o_piece():
    piece = [[1, 1], [1, 1]]
    rotated = rotate_piece(piece)

    assert rotated == [[1, 1], [1, 1]]
    assert len(rotated) == 2
    assert len(rotated[0]) == 2


def test_rotate_piece_invalid_input():
    with pytest.raises(TypeError):
        rotate_piece([])

    with pytest.raises(TypeError):
        rotate_piece("not a piece")

    with pytest.raises(ValueError):
        rotate_piece([[1, 0], [1]])


def test_is_valid_position_true_on_empty_board():
    board = create_board(6, 6)
    piece = spawn_piece("O")

    assert is_valid_position(board, piece, 0, 0) is True
    assert is_valid_position(board, piece, 2, 3) is True


def test_is_valid_position_false_out_of_bounds():
    board = create_board(6, 6)
    piece = spawn_piece("I")

    assert is_valid_position(board, piece, 0, 3) is False
    assert is_valid_position(board, piece, 6, 0) is False
    assert is_valid_position(board, piece, -1, 0) is False


def test_is_valid_position_false_on_collision():
    board = create_board(6, 6)
    piece = spawn_piece("O")
    board = place_piece(board, piece, 2, 2, value=9)

    assert is_valid_position(board, piece, 2, 2) is False
    assert is_valid_position(board, piece, 1, 2) is False


def test_is_valid_position_invalid_arguments():
    board = create_board(6, 6)
    piece = spawn_piece("O")

    with pytest.raises(TypeError):
        is_valid_position(board, piece, "1", 2)

    with pytest.raises(TypeError):
        is_valid_position(board, piece, 1, None)


def test_place_piece_places_cells_correctly():
    board = create_board(6, 6)
    piece = spawn_piece("O")
    updated_board = place_piece(board, piece, 1, 2, value=7)

    assert updated_board[1][2] == 7
    assert updated_board[1][3] == 7
    assert updated_board[2][2] == 7
    assert updated_board[2][3] == 7


def test_place_piece_does_not_mutate_original_board():
    board = create_board(6, 6)
    piece = spawn_piece("O")
    updated_board = place_piece(board, piece, 0, 0, value=5)

    assert board[0][0] == 0
    assert board[0][1] == 0
    assert updated_board[0][0] == 5
    assert updated_board[0][1] == 5


def test_place_piece_invalid_position():
    board = create_board(6, 6)
    piece = spawn_piece("I")

    with pytest.raises(ValueError):
        place_piece(board, piece, 0, 4)

    occupied_board = place_piece(board, spawn_piece("O"), 0, 0, value=1)

    with pytest.raises(ValueError):
        place_piece(occupied_board, spawn_piece("O"), 0, 0, value=1)


def test_place_piece_invalid_argument_types():
    board = create_board(6, 6)
    piece = spawn_piece("O")

    with pytest.raises(TypeError):
        place_piece(board, piece, "0", 0)

    with pytest.raises(TypeError):
        place_piece(board, piece, 0, None)


def test_clear_full_rows_no_rows_cleared():
    board = create_board(4, 4)
    new_board, cleared = clear_full_rows(board)

    assert cleared == 0
    assert new_board == board
    assert len(new_board) == 4


def test_clear_full_rows_single_row():
    board = create_board(4, 4)
    board[3] = [1, 1, 1, 1]

    new_board, cleared = clear_full_rows(board)

    assert cleared == 1
    assert len(new_board) == 4
    assert new_board[0] == [0, 0, 0, 0]


def test_clear_full_rows_multiple_rows():
    board = create_board(5, 4)
    board[1] = [1, 1, 1, 1]
    board[3] = [2, 2, 2, 2]
    board[4] = [0, 3, 0, 3]

    new_board, cleared = clear_full_rows(board)

    assert cleared == 2
    assert len(new_board) == 5
    assert new_board[0] == [0, 0, 0, 0]
    assert new_board[1] == [0, 0, 0, 0]
    assert new_board[4] == [0, 3, 0, 3]
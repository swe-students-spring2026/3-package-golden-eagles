PIECES = {
    "I": [[1, 1, 1, 1]],
    "O": [[1, 1], [1, 1]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "L": [[1, 0], [1, 0], [1, 1]],
    "J": [[0, 1], [0, 1], [1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "Z": [[1, 1, 0], [0, 1, 1]],
}


def _validate_dimensions(rows, cols):
    """
    Validate board dimensions.
    """
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError("rows and cols must both be integers.")
    if rows < 4 or cols < 4:
        raise ValueError("rows and cols must both be at least 4.")


def _validate_piece_matrix(piece):
    """
    Validate that piece is a non-empty rectangular 2D list of 0/1 values.
    """
    if not isinstance(piece, list) or not piece:
        raise TypeError("piece must be a non-empty 2D list.")

    row_length = None
    for row in piece:
        if not isinstance(row, list) or not row:
            raise TypeError("piece must be a non-empty 2D list.")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise ValueError("piece rows must all have the same length.")

        for cell in row:
            if cell not in (0, 1):
                raise ValueError("piece cells must be 0 or 1.")


def _validate_board(board):
    """
    Validate that board is a non-empty rectangular 2D list.
    """
    if not isinstance(board, list) or not board:
        raise TypeError("board must be a non-empty 2D list.")

    row_length = None
    for row in board:
        if not isinstance(row, list) or not row:
            raise TypeError("board must be a non-empty 2D list.")
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise ValueError("board rows must all have the same length.")


def create_board(rows, cols):
    """
    Create an empty Tetris board filled with zeros.
    """
    _validate_dimensions(rows, cols)
    return [[0 for _ in range(cols)] for _ in range(rows)]


def spawn_piece(piece_type):
    """
    Return a copy of the requested Tetris piece matrix.
    """
    if not isinstance(piece_type, str):
        raise TypeError("piece_type must be a string.")

    normalized = piece_type.upper().strip()
    if normalized not in PIECES:
        raise ValueError(f"Invalid piece type: {piece_type}")

    return [row[:] for row in PIECES[normalized]]


def rotate_piece(piece):
    """
    Rotate a piece 90 degrees clockwise.
    """
    _validate_piece_matrix(piece)
    rotated = [list(row) for row in zip(*piece[::-1])]
    return rotated


def is_valid_position(board, piece, row, col):
    """
    Check whether a piece can be placed at the given board position.
    """
    _validate_board(board)
    _validate_piece_matrix(piece)

    if not isinstance(row, int) or not isinstance(col, int):
        raise TypeError("row and col must both be integers.")

    board_rows = len(board)
    board_cols = len(board[0])

    for piece_row_index, piece_row in enumerate(piece):
        for piece_col_index, cell in enumerate(piece_row):
            if cell != 1:
                continue

            board_row = row + piece_row_index
            board_col = col + piece_col_index

            if board_row < 0 or board_row >= board_rows:
                return False
            if board_col < 0 or board_col >= board_cols:
                return False
            if board[board_row][board_col] != 0:
                return False

    return True


def place_piece(board, piece, row, col, value=1):
    """
    Place a piece on the board and return a new board.
    """
    _validate_board(board)
    _validate_piece_matrix(piece)

    if not isinstance(row, int) or not isinstance(col, int):
        raise TypeError("row and col must both be integers.")

    if not is_valid_position(board, piece, row, col):
        raise ValueError("Piece cannot be placed at the requested position.")

    new_board = [board_row[:] for board_row in board]

    for piece_row_index, piece_row in enumerate(piece):
        for piece_col_index, cell in enumerate(piece_row):
            if cell == 1:
                new_board[row + piece_row_index][col + piece_col_index] = value

    return new_board


def clear_full_rows(board):
    """
    Clear all full rows and return (new_board, cleared_count).
    """
    _validate_board(board)

    cols = len(board[0])
    rows = len(board)

    remaining_rows = [row[:] for row in board if not all(cell != 0 for cell in row)]
    cleared_count = rows - len(remaining_rows)

    new_rows = [[0 for _ in range(cols)] for _ in range(cleared_count)]
    new_board = new_rows + remaining_rows

    return new_board, cleared_count
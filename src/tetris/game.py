import curses
import random
import time

from .core import (
    PIECES,
    clear_full_rows,
    create_board,
    is_valid_position,
    place_piece,
    rotate_piece,
    spawn_piece,
)

BOARD_ROWS = 12
BOARD_COLS = 8
DROP_INTERVAL = 0.5


def _random_piece_type(random_generator):
    """
    Pick a random Tetris piece type.
    """
    return random_generator.choice(list(PIECES.keys()))


def _spawn_new_piece(board, random_generator):
    """
    Create a new active piece near the top-center of the board.
    Returns (piece, row, col).
    """
    piece = spawn_piece(_random_piece_type(random_generator))
    row = 0
    col = (len(board[0]) - len(piece[0])) // 2
    return piece, row, col


def _overlay_piece(board, piece, row, col):
    """
    Return a temporary board with the active piece drawn on top.
    """
    display_board = [board_row[:] for board_row in board]

    for piece_row_index, piece_row in enumerate(piece):
        for piece_col_index, cell in enumerate(piece_row):
            if cell != 1:
                continue

            board_row = row + piece_row_index
            board_col = col + piece_col_index

            if 0 <= board_row < len(display_board) and 0 <= board_col < len(display_board[0]):
                display_board[board_row][board_col] = 2

    return display_board


def _safe_addstr(stdscr, y, x, text):
    """
    Safely draw text without crashing if the terminal is too small.
    """
    height, width = stdscr.getmaxyx()

    if y < 0 or y >= height or x < 0 or x >= width:
        return

    available_width = width - x
    if available_width <= 0:
        return

    try:
        stdscr.addstr(y, x, text[:available_width])
    except curses.error:
        pass


def _terminal_is_large_enough(stdscr, board):
    """
    Check whether the terminal is large enough for the current game screen.
    """
    height, width = stdscr.getmaxyx()
    required_height = 8 + len(board)
    required_width = 2 * len(board[0]) + 4
    return height >= required_height and width >= required_width, required_height, required_width


def _draw_too_small_message(stdscr, required_height, required_width):
    """
    Draw a message explaining that the terminal is too small.
    """
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    _safe_addstr(stdscr, 0, 0, "Terminal window is too small for Tetris.")
    _safe_addstr(stdscr, 1, 0, f"Need at least: {required_width} columns x {required_height} rows")
    _safe_addstr(stdscr, 2, 0, f"Current size: {width} columns x {height} rows")
    _safe_addstr(stdscr, 4, 0, "Please enlarge the terminal window.")
    _safe_addstr(stdscr, 5, 0, "Press Q to quit.")
    stdscr.refresh()


def _draw_screen(stdscr, board, piece, piece_row, piece_col, score, game_over):
    """
    Draw the game screen.
    """
    stdscr.clear()

    large_enough, required_height, required_width = _terminal_is_large_enough(stdscr, board)
    if not large_enough:
        _draw_too_small_message(stdscr, required_height, required_width)
        return False

    _safe_addstr(stdscr, 0, 0, "Tetris (terminal)")
    _safe_addstr(stdscr, 1, 0, "A=left  D=right  S=down  W=rotate  Q=quit")
    _safe_addstr(stdscr, 2, 0, f"Score: {score}")

    display_board = _overlay_piece(board, piece, piece_row, piece_col)

    top_border = "+" + "--" * len(board[0]) + "+"
    _safe_addstr(stdscr, 4, 0, top_border)

    for row_index, row in enumerate(display_board):
        line = []
        for cell in row:
            if cell == 0:
                line.append(". ")
            else:
                line.append("X ")
        _safe_addstr(stdscr, 5 + row_index, 0, "|" + "".join(line) + "|")

    _safe_addstr(stdscr, 5 + len(board), 0, top_border)

    if game_over:
        _safe_addstr(stdscr, 7 + len(board), 0, "Game Over! Press Q to quit.")

    stdscr.refresh()
    return True


def play_game(stdscr):
    """
    Real-time terminal Tetris using curses.
    """
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    random_generator = random.Random()

    board = create_board(BOARD_ROWS, BOARD_COLS)
    score = 0
    game_over = False

    current_piece, piece_row, piece_col = _spawn_new_piece(board, random_generator)

    if not is_valid_position(board, current_piece, piece_row, piece_col):
        game_over = True

    last_drop_time = time.time()

    while True:
        screen_ready = _draw_screen(
            stdscr,
            board,
            current_piece,
            piece_row,
            piece_col,
            score,
            game_over,
        )

        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            break

        if not screen_ready:
            time.sleep(0.05)
            continue

        if not game_over:
            if key in (ord("a"), ord("A"), curses.KEY_LEFT):
                new_col = piece_col - 1
                if is_valid_position(board, current_piece, piece_row, new_col):
                    piece_col = new_col

            elif key in (ord("d"), ord("D"), curses.KEY_RIGHT):
                new_col = piece_col + 1
                if is_valid_position(board, current_piece, piece_row, new_col):
                    piece_col = new_col

            elif key in (ord("s"), ord("S"), curses.KEY_DOWN):
                new_row = piece_row + 1
                if is_valid_position(board, current_piece, new_row, piece_col):
                    piece_row = new_row

            elif key in (ord("w"), ord("W"), curses.KEY_UP):
                rotated_piece = rotate_piece(current_piece)
                if is_valid_position(board, rotated_piece, piece_row, piece_col):
                    current_piece = rotated_piece

        current_time = time.time()
        if not game_over and current_time - last_drop_time >= DROP_INTERVAL:
            new_row = piece_row + 1

            if is_valid_position(board, current_piece, new_row, piece_col):
                piece_row = new_row
            else:
                board = place_piece(board, current_piece, piece_row, piece_col, value=1)
                board, cleared = clear_full_rows(board)
                score += cleared

                current_piece, piece_row, piece_col = _spawn_new_piece(board, random_generator)
                if not is_valid_position(board, current_piece, piece_row, piece_col):
                    game_over = True

            last_drop_time = current_time

        time.sleep(0.03)


def main():
    curses.wrapper(play_game)
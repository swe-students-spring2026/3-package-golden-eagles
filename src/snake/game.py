import curses

from .core import change_direction, create_game_state, tick


def draw_board(stdscr, state):
    stdscr.clear()
    width = state["width"]
    height = state["height"]
    snake = state["snake"]
    food = state["food"]
    score = state["score"]

    stdscr.addstr(0, 0, f"Score: {score}  |  Use Arrow Keys to Move (Q to quit)")
    stdscr.addstr(1, 0, "-" * (width + 2))

    for y in range(height):
        stdscr.addstr(y + 2, 0, "|")
        for x in range(width):
            if (x, y) == snake[0]:
                stdscr.addstr(y + 2, x + 1, "O")
            elif (x, y) in snake:
                stdscr.addstr(y + 2, x + 1, "o")
            elif (x, y) == food:
                stdscr.addstr(y + 2, x + 1, "*")
            else:
                stdscr.addstr(y + 2, x + 1, " ")
        stdscr.addstr(y + 2, width + 1, "|")

    stdscr.addstr(height + 2, 0, "-" * (width + 2))
    stdscr.refresh()


def _map_key_to_direction(key):
    if key == curses.KEY_UP:
        return "UP"
    if key == curses.KEY_DOWN:
        return "DOWN"
    if key == curses.KEY_LEFT:
        return "LEFT"
    if key == curses.KEY_RIGHT:
        return "RIGHT"
    return None


def run_curses_game(stdscr, width=20, height=15, start_length=3, tick_ms=200):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(tick_ms)

    state = create_game_state(width=width, height=height, start_length=start_length)
    requested_dir = state["direction"]

    while not state["game_over"]:
        draw_board(stdscr, state)

        key = stdscr.getch()
        if key == ord("q") or key == ord("Q"):
            break

        mapped_direction = _map_key_to_direction(key)
        if mapped_direction is not None:
            requested_dir = change_direction(state["direction"], mapped_direction)

        state = tick(state, requested_dir)

    stdscr.nodelay(0)
    draw_board(stdscr, state)
    stdscr.addstr(state["height"] + 4, 0, f"Game Over! Final Score: {state['score']}")
    stdscr.addstr(state["height"] + 5, 0, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

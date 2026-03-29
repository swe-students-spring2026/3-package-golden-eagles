import time
import os
import curses
from .core import create_game_state, tick, change_direction

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

def curses_main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(200)
    
    state = create_game_state(width=20, height=15, start_length=3)
    requested_dir = state["direction"]

    while not state["game_over"]:
        draw_board(stdscr, state)
        
        # Handle input
        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break
        elif key == curses.KEY_UP:
            requested_dir = "UP"
        elif key == curses.KEY_DOWN:
            requested_dir = "DOWN"
        elif key == curses.KEY_LEFT:
            requested_dir = "LEFT"
        elif key == curses.KEY_RIGHT:
            requested_dir = "RIGHT"
            
        state = tick(state, requested_dir)

    stdscr.nodelay(0)
    draw_board(stdscr, state)
    stdscr.addstr(state["height"] + 4, 0, f"Game Over! Final Score: {state['score']}")
    stdscr.addstr(state["height"] + 5, 0, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

def main():
    try:
        curses.wrapper(curses_main)
    except Exception as e:
        print(f"Error starting game: {e}")

if __name__ == "__main__":
    main()

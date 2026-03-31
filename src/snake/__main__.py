import curses
from .game import run_curses_game

def main():
    try:
        curses.wrapper(run_curses_game)
    except Exception as e:
        print(f"Error starting game: {e}")

if __name__ == "__main__":
    main()

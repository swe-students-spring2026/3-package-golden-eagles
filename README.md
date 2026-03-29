## Golden Eagles

![Build Status](https://img.shields.io/badge/CI-pending-lightgrey)

Lightweight, reusable Python game modules built as an installable package.  
This repository is in active development for the course package exercise.

## Planned Game Module

- **Blackjack**:
- **Tetris**:A terminal-based Tetris module with reusable core logic for board creation, piece spawning, rotation, placement, collision checks, row clearing, and a playable curses-based demo.
- **Snake**: Grid-based snake movement with growth, food spawning, and collision rules.
- **Minesweeper**:
- **Dino Game**:

## Current Progress

- `core` default library containing basic class and functions
- `minefield` module exists with core functions and a terminal game loop.
- `snake` basics are started with importable core logic in `src/snake/core.py`.
- `tetris` module exists with importable core logic, row-clearing behavior, pytest coverage, and a terminal playable version.

# Module Details

## BlackJack

## Minefield

## Snake

### Tetris

The Tetris module provides reusable core functions for Tetris-style game logic and includes a terminal playable version using `curses`.

#### Functions

- `create_board(rows, cols)`  
  Create an empty Tetris board filled with zeros.

- `spawn_piece(piece_type)`  
  Return a copy of a Tetris piece matrix such as `"I"`, `"O"`, `"T"`, `"L"`, `"J"`, `"S"`, or `"Z"`.

- `rotate_piece(piece)`  
  Rotate a piece 90 degrees clockwise.

- `is_valid_position(board, piece, row, col)`  
  Check whether a piece can be placed at the given board position.

- `place_piece(board, piece, row, col, value=1)`  
  Place a piece on the board and return a new board.

- `clear_full_rows(board)`  
  Clear all full rows and return `(new_board, cleared_count)`.

#### Example

```python
from tetris.core import (
    clear_full_rows,
    create_board,
    is_valid_position,
    place_piece,
    rotate_piece,
    spawn_piece,
)

board = create_board(6, 6)
piece = spawn_piece("T")
rotated_piece = rotate_piece(piece)

if is_valid_position(board, rotated_piece, 0, 2):
    board = place_piece(board, rotated_piece, 0, 2)

board, cleared = clear_full_rows(board)

print("Board:", board)
print("Rows cleared:", cleared)
```
### Run Tetris
```bash
PYTHONPATH=src pipenv run python -m tetris
```
Controls: A = left, D = right, S = down, W = rotate, Q = quit.

If the terminal window is too small, the game will display a warning instead of crashing.

### Test Tetris
```bash
PYTHONPATH=src pipenv run pytest tests/test_tetris.py -v
```

## Development (WIP)

## Coming Next

- Add full packaging metadata for publishing to PyPI.
- Add CI workflow to test/build on multiple Python versions.
- Expand examples and function-level documentation for each game.
- Implement tests using pytest

## Team

- [Chen Chen]()
- [Gavin Chen]()
- [Jonas Chen](https://github.com/JonasChenJusFox)
- [Kyle Chen]()
- [Robin Chen](https://www.github.com/localhost433)
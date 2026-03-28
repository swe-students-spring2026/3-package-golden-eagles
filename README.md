# Golden Eagles

![Build Status](https://img.shields.io/badge/CI-pending-lightgrey)

Lightweight, reusable Python game modules built as an installable package.  
This repository is in active development for the course package exercise.

## Planned Game Modules

- **Blackjack**:
- **Tetris**:
- **Snake**: Grid-based snake movement with growth, food spawning, and collision rules.
- **Minesweeper**:
- **Dino Game**:

## Current Progress

- `minefield` module exists with core functions and a terminal game loop.
- `snake` basics are started with importable core logic in `src/snake/core.py`.

## Quick Usage
### Minefield
```bash
PYTHONPATH=src pipenv run python -m minefield
```

### Snake
```bash
PYTHONPATH=src pipenv run python -m snake
```

### Tetris
```bash
PYTHONPATH=src pipenv run python -m tetris
```

## Development (WIP)

## Coming Next

- Add full packaging metadata for publishing to PyPI.
- Add CI workflow to test/build on multiple Python versions.
- Expand examples and function-level documentation for each game.

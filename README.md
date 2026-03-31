# Golden Eagles

![Build Status](https://img.shields.io/badge/CI-pending-lightgrey)

Lightweight, reusable Python game modules built as an installable package.  
This repository is in active development for the course package exercise.

## Planned Game Module

<<<<<<< HEAD
- **Blackjack**: Terminal based blackjack game, emulating a mini game to play to pass some time
- **Tetris**:A terminal-based Tetris module with reusable core logic for board creation, piece spawning, rotation, placement, collision checks, row clearing, and a playable curses-based demo.
=======
- **Tetris**:A terminal-based Tetris module with reusable core logic for board creation, piece spawning, rotation, placement, collision checks, row clearing, and a playable curses-based demo.
- **Blackjack**: Plays a simple game of blackjack wihtin the terminal given the user and an AI dealer
- **Tetris**:
>>>>>>> e356938f10b1ba43b4710c472ae237c79a382227
- **Snake**: Grid-based snake movement with growth, food spawning, and collision rules.
- **Minefield**: Minefield is a puzzle game in which players reveal squares on a grid and use number clues to identify and avoid hidden mines. The objective is to clear all safe squares without triggering a mine.
- **Dino Game**:

## Current Progress

- `blackjack` nearly completed, missing two special functions surrounding split hands and the ace
- `core` default library containing basic class and functions
- `minefield` module exists with core functions and a terminal game loop.
- `snake` module exists with importable core logic, unit tests coverage, and a terminal playable version.
- `tetris` module exists with importable core logic, row-clearing behavior, pytest coverage, and a terminal playable version.

## Module Details

## Install configuration

#### Install Python:
1. Go to (python.org)[https://www.python.org/downloads/]
2. Click "Download Python 3.12" (or latest version)
3. Run the installer
4. Click "Install Now"

**If on Mac**
brew install python3

#### Install pipenv
python -m pip install pipenv

#### Enter project directory:
cd C:\Users\path

#### Install dependencies:
pipenv install build
pipenv install twine
pipenv install pytest

#### Run pipenv:
pipenv shell

#### Run package
Todo

### BlackJack
A command-line implementation of the card game Blackjack. Players play against a dealer with blackjack rules like hand splitting, ace value adjustment (1 or 11), and blackjack win conditions or tie conditions.

Run specifically blackjack, paste (in project root directory):
python -m src.blackjack.game

#### Documentation
1. Card
* `Constructor `
    - Card(suit, number)
    Creates a standard card with specific checks for attributes is_ace and is_face(J, Q, K)

* `Card.generate_deck()` - Static
    - Returns a generatated a full deck of 52 cards with suits and numbers
```def generate_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    # remember an Ace is 1 or 11
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    deck = []
    for suit in suits:
        for num in nums:
            card = Card(suit, num)
            deck.append(card)
    return deck
```

* `Card.blackjack_value(deck)` - Static
    - Changes deck to turn all face cards to a number value of 10

* `Card.pick_card(deck)` - Static
    - Removed a Card from the deck and returns the Card

* `Card.print_card()`
    - Return a nicely formatted card with suit and number in ASCII
```ace = Card("Hearts", 1)
print(ace.print_card())
# Output:
# ┌───────────┐
# │A         A│
# │♥         ♥│
# │           │
# │           │
# │           │
# │♥         ♥│
# │A         A│
# └───────────┘
```

* `Card.print_blank()` - Static
    - Return blank variation
```print(ace.print_blank())
# Output:
# ┌───────────┐
# │           │
# │           │
# │           │
# │           │
# │           │
# │           │
# │           │
# └───────────┘
```

2. Game
* `check_player_total(player_total)` - could be improved
    - Prints player bust if player_total > 21 
    - Prints player blackjack if player_total == 21
    - Returns player_total

* `check_dealer_total(dealer_total)`
    - Prints "Dealer Blackjack!" and returns 21 if dealer_total == 21
    - Prints "Dealer Bust. You win!" and returns True if dealer_total > 21
    - Returns False otherwise

* `check_dealer_natural(dealer_cards)`
    - Checks if dealer's first 2 cards total 21
    - Prints "Dealer has a natural Blackjack" if true
    - Returns: bool

* `check_natural_tie(player_total, dealer_cards)`
    - Compares player blackjack with dealer's natural blackjack
    - Prints "Tough tie!" or "You win this hand!"
    - Returns None

* `check_winner(player_total, dealer_total)`
    - Prints both player and dealer totals
    - Returns "Your hand busts. You lose" if player_total > 21
    - Returns "Your hand wins!" if player_total > dealer_total
    - Returns "Dealer wins!" if player_total < dealer_total
    - Returns "A tie is practically a loss" if equal

* `pause()`
    - Prints "Press Enter to continue..."
    - Waits for user to press Enter

* `print_dealer_hand(dealer_cards, players_turn=False)`
    - Prints dealer's cards in ASCII art
    - If players_turn=True, hides second card with blank
    - If players_turn=False, shows all cards

* `print_player_hand(player_cards)`
    - Prints single player hand in ASCII art
    - Example: `print_player_hand([Card("Hearts", 5), Card("Clubs", 8)])`

* `print_split_hand(player_cards)`
    - Prints multiple split hands with "Playing hand {hand_num}" labels
    - Example: `print_split_hand(hands)`

* `print_table(player_cards, dealer_cards, players_turn=False)`
    - Master print function, displays dealer + player cards
    - Automatically handles single hands (1D) and split hands (2D)
    - Example: `print_table(player_cards, dealer_cards, True)`

* `change_ace_value(total, cards, is_dealer=False)`
    - Adjusts ace from 1 to 11 if improves hand without busting
    - If is_dealer=True, uses dealer rules (must be between 17-21)
    - Returns: int (adjusted total)
    - Modifies card.num in-place
    - Example: `new_total = change_ace_value(11, [ace, ten])`

* `change_ace_value_split(hands_totals, hands)`
    - Adjusts aces for multiple split hands
    - Modifies hands_totals list in-place
    - Example: `change_ace_value_split(hand_totals, player_cards)`

* `split_hand(player_cards, deck)`
    - Recursively splits matching pairs into separate hands
    - Prompts user "Split the pair or Double Down? (A-split/D-double down)"
    - If "A", recursively calls split_hand on each new hand
    - If "D", returns [player_cards] without splitting
    - Returns: list of hands
    - Example: `hands = split_hand([Card("Hearts", 5), Card("Clubs", 5)], deck)`
    - `hand = [[Card("Hearts", 5), (random picked card)], [Card("Clubs", 5), (random picked card)]]`

* `player_hit_stand(player_total, player_cards, deck)`
    - Prompts user "Hit or Stand? (A-hit/D-stand)"
    - If "A", draws card from deck, adds to hand, returns new total
    - If "D", prints "You stand" and returns same total
    - Loops if invalid input
    - Returns player_total (updated)
    - Example: `new_total = player_hit_stand(13, hand, deck)`

* `player_turn(player_cards, dealer_cards, deck)`
    - Calculates initial hand total
    - Calls change_ace_value() to adjust aces
    - Calls check_player_total() - returns 21 if blackjack
    - Loops player_hit_stand(), adjusts aces , checks total
    - Returns total if >= 21 or stand
    - Returns: int (player_total)
    - Example: `total = player_turn(hand, dealer_cards, deck)`

* `dealer_hit_stand(dealer_cards, dealer_total, deck)`
    - Single decision: hits if dealer_total < 17, stands if >= 17
    - If hits: draws card, prints "Dealer hits", returns new total
    - If stands: prints "Dealer stands", returns same total
    - Returns: int (updated total)
    - Example: `new_total = dealer_hit_stand(dealer_cards, 15, deck)`

* `dealer_turn(player_cards, dealer_cards, deck)`
    - Calculates initial dealer total
    - Calls change_ace_value() with is_dealer=True
    - Loops: calls dealer_hit_stand(), adjusts aces, prints table
    - Calls check_dealer_total() - returns None if bust/blackjack
    - Ends loop if dealer_total >= 17
    - Returns: int (player_total) or None is bust
    - Example: `dealer_total = dealer_turn(player_cards, dealer_cards, deck)`


### Dino Game

### Minefield

The Minesweeper module provides reusable core functions for Minesweeper game logic,
this includes board creation, cell revealing, and win-condition checking

#### Functions

- `create_board(rows, cols, num_mins)`
  Creates an empty grid for the minefield/

- `reveal_board(rows, cols)`
  Creates the player's visible board with all cells hidden

- `count_adjacent_mines(board,row,col)`
  Returns the number of mines adjacent to a given cell.

- `reveal_cell(board, visible_board, row, col)`
    Reveals a selected cell on the visible board and returns whether the move was safe or not

- `check_win(board, visible_board)`
  Returns whehter all non-mine cells have been revealed

#### Run Minefield

```bash
PYTHONPATH=src pipenv run python -m minefield
```

## Controls

The game displays a grid with row and column numbers. Enter the row and column of the cell you want to reveal.

**Example:**

```text
  0 1 2 3 4 5
0 # # # # # #
1 # # # # # #
2 # # # # # #
3 # # # # # #
4 # # # # # #
5 # # # # # #
```

**Example Input:**
`2 3`

**Result:**
This reveals the cell located at **Row 2, Column 3**.

### Snake

The Snake module provides reusable core functions for classic Snake game logic and includes a terminal playable version using `curses`.

#### Functions

- `create_game_state(width, height, start_length=3, seed=None)`  
  Create the initial snake game state.

- `spawn_food(width, height, snake, random_generator)`  
  Pick a random unoccupied board cell for food.

- `change_direction(current_direction, requested_direction)`  
  Snake direction change, disallowing immediate reversal.

- `tick(state, requested_direction=None)`  
  Advance the game by one tick and returns the next state, checking for out-of-bounds walls, self-collision, and eating food.

#### Example

```python
from snake.core import create_game_state, tick

state = create_game_state(10, 10, start_length=3)
state = tick(state, requested_direction="UP")

print("Snake:", state["snake"])
print("Food:", state["food"])
print("Score:", state["score"])
print("Game Over:", state["game_over"])
```

#### Run Snake

```bash
PYTHONPATH=src pipenv run python -m snake
```

Controls: Arrow Keys = move, Q = quit.

#### Test Snake

```bash
PYTHONPATH=src pipenv run pytest tests/test_snake_core.py -v
```

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

#### Run Tetris

```bash
PYTHONPATH=src pipenv run python -m tetris
```

Controls: A = left, D = right, S = down, W = rotate, Q = quit.

If the terminal window is too small, the game will display a warning instead of crashing.

#### Test Tetris

```bash
PYTHONPATH=src pipenv run pytest tests/test_tetris.py -v
```

## Installation

## Example Programs

You can find example Python programs in the `examples/` directory that demonstrate each function's operations. Currently available:

- [Example Program](examples/demo.py)

## Development

To set up the development environment, install dependencies, and build/test the package:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/swe-students-spring2026/3-package-golden-eagles.git
   cd 3-package-golden-eagles
   ```

2. **Install dependencies using pipenv:**

   ```bash
   pipenv install --dev
   ```

3. **Activate the environment:**

   ```bash
   pipenv shell
   ```

4. **Run the test suite:**

   ```bash
   pytest
   ```

5. **Build the package:**

   ```bash
   python -m build
   ```

### Environment Variables & Starter Data

Currently, there are no strict imports or secret `.env` variables required for the project.

## Coming Next

- Add full packaging metadata for publishing to PyPI.
- Add CI workflow to test/build on multiple Python versions.
- Expand examples and function-level documentation for each game.
- Implement tests using pytest

## Team

<<<<<<< HEAD
- [Chen Chen](https://github.com/LoganHund)
- [Gavin Chen](https://github.com/OverYander)
=======
<<<<<<< HEAD
- [Chen Chen](https://github.com/OverYander)
- [Gavin Chen]()
=======
- [Chen Chen](https://github.com/LoganHund)
- [Gavin Chen](https://github.com/OverYander)
>>>>>>> 6429b7519d1d399b1195d3ad1ae7e39672ebebd0
>>>>>>> e356938f10b1ba43b4710c472ae237c79a382227
- [Jonas Chen](https://github.com/JonasChenJusFox)
- [Kyle Chen](https://github.com/KyleC55)
- [Robin Chen](https://github.com/localhost433)

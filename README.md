# Golden Eagles

![Build Status](https://img.shields.io/badge/CI-pending-lightgrey)

Lightweight, reusable Python game modules built as an installable package.  
This repository is in active development for the course package exercise.

## Planned Game Module

- **Blackjack**: Plays a simple game of blackjack wihtin the terminal given the user and an AI dealer
- **Tetris**:A terminal-based Tetris module with reusable core logic for board creation, piece spawning, rotation, placement, collision checks, row clearing, and a playable curses-based demo.
- **Snake**: Grid-based snake movement with growth, food spawning, and collision rules.
- **Minefield**: Minefield is a puzzle game in which players reveal squares on a grid and use number clues to identify and avoid hidden mines. The objective is to clear all safe squares without triggering a mine.
- **Dino Game**: Plays the out-of-internet dinosaur game on the terminal with selectable difficulty (speed)

## Current Progress

- `blackjack` nearly completed, missing two special functions surrounding split hands and the ace
- `core` default library containing basic class and functions for simple 2d games to run on the terminal
- `minefield` module exists with core functions and a terminal game loop.
- `snake` module exists with importable core logic, unit tests coverage, and a terminal playable version.
- `tetris` module exists with importable core logic, row-clearing behavior, pytest coverage, and a terminal playable version.
- `dinoGame` module imports from core default library and currently only supports windows os

## Module Details
### Core Library (`src/core`)
The core library provides a reusable foundation for building terminal-based 2D games.

#### Overview
- **`Sprite`** - represents any drawable object (player, obstacle, etc.)
- **`Board`** & **`ScrollingBoard`**  - manages a 2D grid and renders sprites, and `ScrollingBoard` extends `Board` with side-scrolling behavior

---

#### Sprite
The `Sprite` class represents an object/actor on the board.

- Stores:
  - position - `row`, `col`
  - shape - `mask`
  - dimensions - `height`, `width`
- Does **not** render itself — only holds state

**Functions**

- `__init__(row, col, mask, fill=" ")`  
  Initialize a sprite with position, shape (mask), and fill character.

- `move(direction, steps=1)`  
  Moves the sprite in a given direction (`up`, `down`, `left`, `right`).

- `alter(newMask, startingPoint="topLeft")`  
  Changes the sprite’s shape while preserving alignment based on a reference point (e.g., center, corners).

- `stringToMask(s)` *(static)*  
  Converts a multi-line string into a 2D mask (list of character lists).

- `maskToString(mask)` *(static)*  
  Converts a 2D mask back into a printable string format.

---

#### Board
The `Board` class represents the game environment and handles rendering.

---

**Functions**

- `__init__(rows, cols, fill=" ")`  
  Creates a board with given dimensions and default fill character.

- `redraw()`  
  Clears the grid and redraws all sprites onto the board.

- `setFill(fill)`  
  Updates the default fill character for empty cells.

- `reset(clearSprites=False)`  
  Clears the grid and optionally removes all sprites.

- `setCell(row, col, val)`  
  Sets a specific cell value (ignores out-of-bounds).

- `getCell(row, col)`  
  Returns the value of a specific cell.

- `getArea(row, col, height=1, width=1)`  
  Returns a sub-area of the board as a 2D list.

- `clearArea(row, col, height=1, width=1)`  
  Clears a region of the board back to the fill value.

- `addSprite(sprite, redraw=True)`  
  Adds a sprite to the board and optionally redraws.

- `removeSprite(sprite)`  
  Removes a sprite and redraws the board.

- `overlay(row, col, mask, fill=" ")`  
  Draws a mask onto the board at a given position.

- `spritesCollide(sprite1, sprite2)`  
  Checks if two sprites overlap (ignores transparent cells).

- `printBoard(row=0, col=0, height=20, width=50)`  
  Prints a portion of the board to the terminal.

- `copy()`  
  Returns a copy of the board grid.

---

#### ScrollingBoard
Extends `Board` to support side-scrolling behavior.

**Functions**

- `__init__(rows, cols, fill=" ", loadingZone=10)`  
  Initializes a board with an additional off-screen loading zone.

- `isOffScreenLeft(sprite)`  
  Checks if a sprite has moved completely off the left side.

- `inLoadingZone(sprite)`  
  Checks if a sprite is fully within the right-side loading zone.

- `scrollLeft(step=1, exclude=None)`  
  Moves all sprites left and removes off-screen sprites.

- `addSpriteToLoadingZone(sprite, offset=0)`  
  Adds a sprite just outside the visible board for later entry.

---

#### Basic Game Logic

The Dino Game builds on the core library’s **scrolling** and **sprite-based rendering** system.  
Instead of moving the player forward, the **environment scrolls left**, creating an endless runner effect while the dino remains mostly fixed horizontally.

---

#### Core Mechanics

- **Jump Behavior (`jump`)**  
  Applies an upward velocity to the dino when grounded, followed by gravity each tick to simulate a smooth jump arc.

- **Cactus Spawning (`spawnCactus`, `canSpawnCactus`)**  
  Obstacles are spawned randomly in the loading zone.  
  A minimum gap (`minGap`) is enforced to prevent overlapping or unfair spawns.

- **Collision Detection (`checkCollision`)**  
  Uses the core library’s sprite collision system to detect overlap between the dino and cacti.  
  Ends the game immediately on collision.

- **Scrolling Behavior**  
  The board continuously shifts left each tick, moving all sprites except the dino.  
  Off-screen objects are automatically removed.

- **Rendering Priority (`prioritizeDino`)**  
  Ensures the dino is always drawn on top of other sprites.

---

#### Game Logic

Each tick:
1. Handle input (jump)
2. Possibly spawn a cactus (with spacing check)
3. Scroll the environment left
4. Update dino position (velocity + gravity)
5. Check for collisions
6. Redraw the board and update score

---

#### Dino & Cactus Sprites

**Dino (Alive)**
```
    ___
   / o_|
<=/__/>>
  ⌄ ⌄
```

**Dino (Dead)**
```
    ___
   / x_|
<=/__/>>
  ⌄ ⌄
```

**Cactus 1**
```
 __
|^^| _
|^^|//
|^^|/
```
**Cactus 2**
``` 
 __
|^ |/
| ^|
```

**Cactus 3**
``` 
  __
\|^ |
 | ^|
```
**Cactus 4**
```
   __
_ |^^| _
\\|^^|//
 \|^^|/
```

---


#### Running the Game
- Run the game from the project root:
```bash
python -m src.dinoGame.game
```
0 You can specify the difficulty as a command-line argument:
```bash
python -m src.dinoGame.game [low|high|ramp]
```

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

## Example Programs

You can find example Python programs in the `examples/` directory that demonstrate each function's operations. Currently available:

- [Example Program](examples/demo.py)


## Prerequisites

- Install Python (use the version required by this project)
- Install pipenv:

```bash
python -m pip install pipenv
```

 ## Setup

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

## Team

- [Chen Chen](https://github.com/LoganHund)
- [Gavin Chen](https://github.com/OverYander)
- [Jonas Chen](https://github.com/JonasChenJusFox)
- [Kyle Chen](https://github.com/KyleC55)
- [Robin Chen](https://github.com/localhost433)

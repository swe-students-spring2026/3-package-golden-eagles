from .core import create_board, reveal_board, count_adjacent_mines, check_win, reveal_cell

def print_board(board):
    """
    Printing the board
    """
    for row in board:
        print(' '.join(row))
    print()

def play_game():
    """
    Game Loop
    """
    rows = 5
    cols = 5
    num_mines = 5

    board = create_board(rows, cols, num_mines)
    visible_board = reveal_board(rows, cols)

    print("Welcome to Minefield!")
    print("Enter row and column to reveal (e.g., '1 2'):")
    print()

    while True:
        print_board(visible_board)

        try:
            row, col = map(int, input("Choose a cell: ").split())
        except ValueError:
            print("Invalid input. Please enter row and column numbers separated by a space.")
            continue

        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("Invalid cell. Please choose a cell within the board.")
            continue

        alive = reveal_cell(board, visible_board, row, col)
        if not alive:
            print_board(visible_board)
            print("Game Over! You hit a mine.")
            break
        
        if check_win(board, visible_board):
            print_board(visible_board)
            print("Congratulations! You've cleared the minefield!")
            break
import time
import random
from src.core import ScrollingBoard

class dinoBoard(ScrollingBoard):
    def __init__(self, rows=20, cols=20, fill=" "):
        super().__init__(rows, cols, fill)


def intro():
    print("\033[?25l", end="")  # hide cursor
    for _ in range(3):
        for dots in [".", "..", "..."]:
            print(f"\rConnecting to internet{dots:<3}", end="")
            time.sleep(0.3)
    print()

    print("Connection Failed")
    time.sleep(1.0)

    for _ in range(3):
        for dots in [".", "..", "..."]:
            print(f"\rLaunching Dinosaur Game{dots:<3}", end="")
            time.sleep(0.3)
    print()

# intro()






# restores cursor when program exits
print("\033[?25h", end="") 
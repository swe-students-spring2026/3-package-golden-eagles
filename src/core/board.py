"""
    * This file contains basic board classes and functions for simple 2d games that can run on the terminal
    * In particular, board class and scrollingBoard class are implemented
    * They utilize the Sprite class as actors in the board environment
"""
from .sprites import Sprite

class Board:

    def __init__(self, rows, cols, fill=" "):
        self.rows = rows
        self.cols = cols
        self.fill = fill # default cell value for empty spaces
        self.grid = [[fill for _ in range(cols)] for _ in range(rows)]
        self.sprites = [] # list of sprites currently on the board

    # TODO: consider what to do with overlapping sprites
    def redraw(self):
        self.grid = [[self.fill for _ in range(self.cols)] for _ in range(self.rows)]
        for sprite in self.sprites:
            self.overlay(sprite.row, sprite.col, sprite.mask, sprite.fill)

    def setFill(self, fill):
        # modify default cell
        self.fill = fill

    def reset(self, clearSprites=False):
        self.grid = [[self.fill for _ in range(self.cols)] for _ in range(self.rows)]
        if clearSprites:
            self.sprites = []

    def setCell(self, row, col, val):
        # ignore out-of-bounds
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return False  # signal failure
        else:
            self.grid[row][col] = val  # set value
            return True  # signal success

    def getCell(self, row, col):
        # Get a single cell value 
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def getArea(self, row, col, height=1, width=1):
        # extract sub-area as 2D list and extract partially if out of bounds
        area = []
        for r in range(row, row + height):
            rowData = []
            for c in range(col, col + width):
                if 0 <= r < self.rows and 0 <= c < self.cols:
                    rowData.append(self.grid[r][c])  # valid cell
                else:
                    rowData.append(None)  # out of bounds
            area.append(rowData)
        return area
    
    def clearArea(self, row, col, height=1, width=1):
        for r in range(row, row + height):
            for c in range(col, col + width):
                self.setCell(r, c, self.fill)  # relies on setCell bounds check

    def addSprite(self, sprite, redraw=True):
            if sprite not in self.sprites:
                self.sprites.append(sprite)
                if redraw:
                    self.redraw()  # redraw to include new sprite
                else:
                    self.overlay(sprite.row, sprite.col, sprite.mask, sprite.fill)
                return True
            else:
                return False  # sprite already exists, do not add again

    def removeSprite(self, sprite):
        if sprite in self.sprites:
            self.sprites.remove(sprite)
            self.redraw()
            return True
        return False

    def overlay(self, row, col, mask, fill=" "):
        """
        * accepts: string (multiline), 1D list (treated as single row), or 2D list
        * lenient input: auto-normalizes to 2D representation before applying
        """
        if isinstance(mask, str):
            lines = mask.strip("\n").split("\n")
        elif isinstance(mask, list):
            if not mask:
                return
            if all(isinstance(line, str) for line in mask):
                lines = mask
            elif all(isinstance(line, list) for line in mask):
                lines = mask
            else:
                lines = [mask]
        else:
            return

        for r, line in enumerate(lines):
            for c, ch in enumerate(line):
                if ch != fill:
                    self.setCell(row + r, col + c, ch)

    def spritesCollide(self, sprite1, sprite2):
        h1 = len(sprite1.mask)
        w1 = max(len(row) for row in sprite1.mask)
        h2 = len(sprite2.mask)
        w2 = max(len(row) for row in sprite2.mask)

        if sprite1.row + h1 <= sprite2.row or sprite2.row + h2 <= sprite1.row:
            return False
        if sprite1.col + w1 <= sprite2.col or sprite2.col + w2 <= sprite1.col:
            return False

        for r1, row in enumerate(sprite1.mask):
            for c1, val1 in enumerate(row):
                if val1 == sprite1.fill:
                    continue

                board_r = sprite1.row + r1
                board_c = sprite1.col + c1

                r2 = board_r - sprite2.row
                c2 = board_c - sprite2.col

                if 0 <= r2 < len(sprite2.mask) and 0 <= c2 < len(sprite2.mask[r2]):
                    if sprite2.mask[r2][c2] != sprite2.fill:
                        return True

        return False

    # TODO: test how it looks
    def printBoard(self, row=0, col=0, height=20, width=50):
        r_end = min(self.rows, row + height)
        c_end = min(self.cols, col + width)

        print("+" + "-" * (c_end - col) + "+")
        for r in range(row, r_end):
            line = ""
            for c in range(col, c_end):
                line += self.grid[r][c]
            print("|" + line + "|")
        print("+" + "-" * (c_end - col) + "+")
    
    # TODO: incomplete
    def copy(self):
        # Return a deep copy of the board
        newBoard = Board(self.rows, self.cols, self.fill)
        newBoard.grid = [row[:] for row in self.grid]
        return newBoard

# board but with a scrollLeft method
# currently only supports leftward scrolling with 1 loading zone on the right
class ScrollingBoard(Board):
    def __init__(self, rows, cols, fill=" ", loadingZone=10):
            super().__init__(rows, cols, fill)
            self.loadingZone = loadingZone

    def isOffScreenLeft(self, sprite):
        return sprite.col + sprite.width <= 0
    
    # only returns true if completely in loading zone
    def inLoadingZone(self, sprite):
        return self.cols <= sprite.col < self.cols + self.loadingZone

    def scrollLeft(self, step=1, exclude=None):
        step = min(step, self.cols + self.loadingZone)

        if exclude is None:
            exclude = set()
        elif not isinstance(exclude, (set, list, tuple)):
            exclude = {exclude}
        else:
            exclude = set(exclude)

        for sprite in self.sprites:
            if sprite not in exclude:
                sprite.col -= step

        self.sprites = [
            sprite for sprite in self.sprites
            if not self.isOffScreenLeft(sprite)
        ]

        self.redraw()

    # doesn't check offset 
    def addSpriteToLoadingZone(self, sprite, offset=0):
        sprite.col = self.cols + offset
        self.addSprite(sprite)

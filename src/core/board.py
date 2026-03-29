"""
    * This file contains basic board classes and functions for simple 2d games that can run on the terminal
    * in particular, board class and scrollingBoard class are implemented
"""

class Board:
    def __init__(self, rows, cols, fill=" "):
        self.rows = rows
        self.cols = cols
        self.fill = fill
        self.grid = [[fill for _ in range(cols)] for _ in range(rows)]

    def setFill(self, fill):
        # modify default cell
        self.fill = fill

    def reset(self):            
        # Reset the board to the fill character
        for r in range(self.rows):
            for c in range(self.cols):
                self.grid[r][c] = self.fill

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

    def overlay(self, row, col, mask, transparent=" "):
        """
        * accepts: string (multiline), 1D list (treated as single row), or 2D list
        * lenient input: auto-normalizes to 2D representation before applying
        * parameters:
            1. self
            2. row - board row
            3. col - board column
            4. mask - can accept a variety of input types, this will be what is overlayed/added onto the board
            5. transparent - default cell
        """
                
        if isinstance(mask, str):
            lines = mask.strip("\n").split("\n")  # multiline string -> list of rows
        elif isinstance(mask, list):
            if len(mask) > 0 and isinstance(mask[0], str):
                lines = mask  # already list of strings (2D)
            else:
                lines = [mask]  # 1D list -> wrap as single row
        else:
            return  # invalid type, ignore

        for r, line in enumerate(lines):
            for c, ch in enumerate(line):
                if ch != transparent:
                    self.setCell(row + r, col + c, ch)  # overwrite
                    

    def render(self, row=0, col=0):
        # Return the board as a printable string (allow partial printing)
        if height is None:
            height = self.rows - row
        if width is None:
            width = self.cols - col

        # returns full board if no row or col specified
        area = self.getArea(row, col, height, width)

        lines = []
        for line in area:
            lines.append("".join(self.fill if cell is None else cell for cell in line))

        return "\n".join(lines)


    def copy(self):
        # Return a deep copy of the board
        newBoard = Board(self.rows, self.cols, self.fill)
        newBoard.grid = [row[:] for row in self.grid]
        return newBoard

# board but with a scrollLeft method
class ScrollingBoard(Board):
    def scrollLeft(self, fill=None, step=1, addedCells=None):
        # Scroll the board left by a certain number of steps, filling new space with fill character
        if fill is None:
            fill = self.fill
        for r in range(self.rows):
            for c in range(self.cols - step):
                self.grid[r][c] = self.grid[r][c + step]  # shift left
            for c in range(self.cols - step, self.cols):
                self.grid[r][c] = fill  # fill new rightmost cells
        # add new cells if provided (list of strings, one per row)
        if addedCells is not None:
            for r in range(min(self.rows, len(addedCells))):
                line = addedCells[r]
                for c in range(min(self.cols, len(line))):
                    self.grid[r][self.cols - step + c] = line[c]  # add new content on right

# scrollUp, scrollDown, scrollRight can be implemented similarly if needed

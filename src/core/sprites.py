"""
* basic actor class for sprites that can be moved and rendered on a board
* it does not alter its position on the board, but rather just stores its own position
"""

class Sprite:
    def __init__(self, row, col, mask, transparent=" "):
        self.row = row
        self.col = col
        self.height = len(mask)
        self.width = max(len(line) for line in mask)
        self.mask = mask
        self.transparent = transparent

    def move(self, direction, steps=1):
        if direction == "up":
            self.row -= steps
        elif direction == "down":
            self.row += steps
        elif direction == "left":
            self.col -= steps
        elif direction == "right":
            self.col += steps

    def alter(self, newMask, startingPoint="topLeft"):
        self.mask = newMask
        self.height = len(newMask)
        self.width = max(len(line) for line in newMask)
        if startingPoint == "topLeft":
            pass
        elif startingPoint == "topRight":
            self.col -= self.width - 1
        elif startingPoint == "bottomLeft":
            self.row -= self.height - 1
        elif startingPoint == "bottomRight":
            self.row -= self.height - 1
            self.col -= self.width - 1
        elif startingPoint == "center":
            self.row -= self.height // 2
            self.col -= self.width // 2
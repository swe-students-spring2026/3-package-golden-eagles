"""
* basic actor class for sprites that can be moved and rendered on a board
* it does not alter its position on the board, but rather just stores its own position
"""

class Sprite:
    # currently assumes non-empty mask 
    def __init__(self, row, col, mask, fill=" "):
        self.row = row
        self.col = col
        self.height = len(mask)
        self.width = max(len(line) for line in mask)
        self.mask = mask
        self.fill = fill

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
        old_height = self.height
        old_width = self.width

        new_height = len(newMask)
        new_width = max(len(line) for line in newMask)

        if startingPoint == "topLeft":
            pass
        elif startingPoint == "topRight":
            self.col += old_width - new_width
        elif startingPoint == "bottomLeft":
            self.row += old_height - new_height
        elif startingPoint == "bottomRight":
            self.row += old_height - new_height
            self.col += old_width - new_width
        elif startingPoint == "center":
            self.row += (old_height - new_height) // 2
            self.col += (old_width - new_width) // 2

        self.mask = newMask
        self.height = new_height
        self.width = new_width

    @staticmethod
    def stringToMask(s):
        return [list(line) for line in s.strip("\n").split("\n")]

    @staticmethod
    def maskToString(mask):
        return "\n".join("".join(row) for row in mask)
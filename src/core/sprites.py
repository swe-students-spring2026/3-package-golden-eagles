class Sprite:
    def __init__(self, row, col, mask, transparent=" "):
        self.row = row
        self.col = col
        self.mask = mask
        self.transparent = transparent
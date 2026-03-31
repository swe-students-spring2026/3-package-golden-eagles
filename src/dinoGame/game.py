import time
import msvcrt
import random
import sys
from src.core import ScrollingBoard
from src.dinoGame.dinoAssets import Dino, Cactus

def refresh(offset):
    sys.stdout.write(f"\033[{offset+1};1H")
    sys.stdout.flush()

class dinoBoard(ScrollingBoard):
    def __init__(self, difficulty, rows=20, cols=20, fill=" "):
        super().__init__(rows, cols, fill)
        self.difficulty = difficulty
        self.ground_row = rows - 1
        self.tick_count = 0
        self.score = 0
        self.running = True
        self.gravity = 0.45
        self.dino = Dino(self.ground_row - 3, 5)
        self.dino.y = self.dino.row
        self.addSprite(self.dino)

    def handleInput(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                self.dino.jump()

    def getSpeed(self):
        if self.difficulty == "low":
            return 2
        elif self.difficulty == "high":
            return 3
        elif self.difficulty == "ramp":
            return min(3 + self.tick_count // 80, 4)
        else:
            return 4

    def drawGround(self):
        for c in range(self.cols):
            self.setCell(self.ground_row, c, "_")

    # checks for overlapping/unfair cacti spawns
    def canSpawnCactus(self, minGap=25):
        cacti = [sprite for sprite in self.sprites if isinstance(sprite, Cactus)]
        if not cacti:
            return True

        rightmost = max(cacti, key=lambda cactus: cactus.col + cactus.width)
        return rightmost.col + rightmost.width <= self.cols + self.loadingZone - minGap

    def spawnCactus(self):
        cactus = Cactus(self.ground_row - 3, self.cols)
        self.addSpriteToLoadingZone(cactus, offset=random.randint(0, self.loadingZone - 1))
    
    # allows dino to be always drawn on top
    def prioritizeDino(self):
        if self.dino in self.sprites:
            self.sprites.remove(self.dino)
            self.sprites.append(self.dino)
    
    def updateDino(self):
        if not self.dino.grounded:
            self.dino.y += self.dino.vel
            self.dino.vel += self.gravity
            self.dino.row = round(self.dino.y)

        ground_top = self.ground_row - self.dino.height + 1
        if self.dino.row >= ground_top:
            self.dino.row = ground_top
            self.dino.y = ground_top
            self.dino.vel = 0
            self.dino.grounded = True

    def checkCollision(self):
        for sprite in self.sprites:
            if sprite is not self.dino and self.spritesCollide(self.dino, sprite):
                self.running = False
                self.dino.die()
                return

    def tick(self):
        self.tick_count += 1
        self.handleInput()
        if random.random() < 0.12 and self.canSpawnCactus():
            self.spawnCactus()

        self.scrollLeft(self.getSpeed(), exclude=self.dino)
        self.updateDino()
        self.checkCollision()
        self.reset()
        self.drawGround()
        self.prioritizeDino()
        self.redraw()
        self.score += 1

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

intro()

def run_game(difficulty="low"):
    offset = 2   
    board = dinoBoard(difficulty, rows=12, cols=50)

    reserved_lines = offset + board.rows + 4 # extra lines for score and spacing
    print("\n" * reserved_lines, end="")# push game down
    # print("\033[?25l", end="")  # can hide cursor

    while board.running:
        refresh(offset)
        board.tick()
        board.printBoard(height=board.rows, width=board.cols)
        print(f"Score: {board.score}   Difficulty: {difficulty}")
        time.sleep(0.15)

    print("Game Over")

if __name__ == "__main__":
    run_game("ramp")

# restores cursor when program exits
print("\033[?25h", end="")
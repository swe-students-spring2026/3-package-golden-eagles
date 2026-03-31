import random
from src.core import Sprite

__all__ = ["Dino", "Cactus"]

DINO_ALIVE = r"""
    ___
   / o_|
<=/__/>>
  ⌄ ⌄
""".strip("\n")

DINO_DEAD = r"""
    ___
   / x_|
<=/__/>>
  ⌄ ⌄
""".strip("\n")


CACTUS1 = r"""
 __
|^^| _
|^^|//
|^^|/
""".strip("\n")

CACTUS2 = r"""
 __
|^ |/
| ^|
""".strip("\n")

CACTUS3 = r"""
  __
\|^ |
 | ^|
""".strip("\n")

CACTUS4 = r"""
   __
_ |^^| _
\\|^^|//
 \|^^|/
""".strip("\n")


class Dino(Sprite):
    def __init__(self, row, col):
        super().__init__(row, col, DINO_ALIVE)
        self.vel = 0
        self.grounded = True
        self.aliveMask = DINO_ALIVE
        self.deadMask = DINO_DEAD

    # TODO: fine-tune jump strength and gravity
    def jump(self, strength=-3):
        if self.grounded:
            self.vel = strength
            self.grounded = False

    def die(self):
        self.alter(self.deadMask)

CACTUS_LIST = [CACTUS1, CACTUS2, CACTUS3, CACTUS4]

class Cactus(Sprite):
    def __init__(self, row, col, type=None):
        if type is None:
            type = random.randint(0, len(CACTUS_LIST) - 1)

        self.type = type
        mask = CACTUS_LIST[type]
        super().__init__(row, col, mask)
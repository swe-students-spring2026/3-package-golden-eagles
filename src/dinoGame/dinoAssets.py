from src.core import Sprite
__all__ = ["DINO", "CACTUS1", "CACTUS2", "CACTUS3", "CACTUS4"]

DINO_ALIVE = r"""
    ___
   / o_|
<=/__/>>
  ⌄ ⌄
"""

DINO_DEAD = r"""
    ___
   / x_|
<=/__/>>
  ⌄ ⌄
"""


CACTUS1 = r"""
 __
|^^| _
|^^|//
|^^|/
"""

CACTUS2 = r"""
 __
|^ |/
| ^|
"""

CACTUS3 = r"""
  __
\|^ |
 | ^|
"""

CACTUS4 = r"""
   __
_ |^^| _
\\|^^|//
 \|^^|/
"""

class Dino(Sprite):
    def __init__(self, row, col):
        super().__init__(row, col, DINO_ALIVE)
        self.vel = 0
        self.grounded = True
        self.aliveMask = DINO_ALIVE
        self.deadMask = DINO_DEAD

    # TODO: finish the jump method
    # needs to be async, prevent input until jump "animation" finish
    def jump(self):
        return None

# TODO: finish the cactus class
CACTUS_LIST = [CACTUS1, CACTUS2, CACTUS3, CACTUS4]
class Cactus(Sprite):
    def __init__(self, row, col, type=0):
        super().__init__(row, col, CACTUS_LIST[type])

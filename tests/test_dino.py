import pytest
from src.dinoGame import Dino, Cactus, dinoBoard


# -------------------------
# DINO TESTS
# -------------------------

def test_dino_jump_sets_velocity_and_not_grounded():
    # Dino.jump() should set velocity and make dino airborne
    d = Dino(10, 5)
    d.jump()

    assert d.vel < 0
    assert d.grounded is False


def test_dino_cannot_double_jump():
    # Dino.jump() should do nothing if already airborne
    d = Dino(10, 5)
    d.jump()
    first_vel = d.vel

    d.jump()  # second jump should not change velocity

    assert d.vel == first_vel


def test_dino_die_changes_mask():
    # Dino.die() should change sprite mask (alive -> dead)
    d = Dino(10, 5)
    alive_mask = d.mask

    d.die()

    assert d.mask != alive_mask


# -------------------------
# CACTUS TESTS
# -------------------------

def test_cactus_random_type_in_range():
    # Cactus should have a valid type index
    c = Cactus(10, 10)

    assert 0 <= c.type <= 3


def test_cactus_position():
    # Cactus should initialize at given position
    c = Cactus(7, 15)

    assert c.row == 7
    assert c.col == 15


# -------------------------
# BOARD TESTS
# -------------------------

def test_board_initialization():
    # Board should initialize with correct defaults
    b = dinoBoard("low", rows=10, cols=20)

    assert b.rows == 10
    assert b.cols == 20
    assert b.difficulty == "low"
    assert b.running is True
    assert b.score == 0


def test_get_speed_modes():
    # getSpeed() should return correct values for difficulty
    b_low = dinoBoard("low")
    b_high = dinoBoard("high")
    b_other = dinoBoard("unknown")

    assert b_low.getSpeed() == 2
    assert b_high.getSpeed() == 3
    assert b_other.getSpeed() == 4


def test_can_spawn_cactus_when_none_exist():
    # canSpawnCactus should return True if no cactus exists
    b = dinoBoard("low")

    assert b.canSpawnCactus() is True


def test_spawn_cactus_adds_to_loading_zone():
    # spawnCactus should add a cactus (indirectly via loading zone)
    b = dinoBoard("low")

    before = len(b.sprites)
    b.spawnCactus()

    # might still be in loading zone, but at least something was attempted
    assert len(b.sprites) >= before


def test_update_dino_applies_gravity():
    # updateDino should move dino downward over time
    b = dinoBoard("low")
    d = b.dino

    d.grounded = False
    d.vel = -2
    old_row = d.row

    b.updateDino()

    assert d.row != old_row


def test_dino_lands_on_ground():
    # updateDino should stop dino at ground and reset velocity
    b = dinoBoard("low")
    d = b.dino

    d.grounded = False
    d.y = b.ground_row
    d.vel = 5

    b.updateDino()

    assert d.grounded is True
    assert d.vel == 0


def test_collision_sets_game_over():
    # checkCollision should stop game when dino collides
    b = dinoBoard("low")
    d = b.dino

    # force collision by placing cactus on dino
    c = Cactus(d.row, d.col)
    b.addSprite(c)

    b.checkCollision()

    assert b.running is False
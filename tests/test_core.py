"""
Currently only a skeleton file
TODO: Write tests for Board class
"""
from core import Board, ScrollingBoard, Sprite

def test_board_set_and_get_cell():
    b = Board(3, 3)

    assert b.setCell(1, 1, "X") is True
    assert b.getCell(1, 1) == "X"
    assert b.setCell(5, 5, "Y") is False
    assert b.getCell(5, 5) is None


def test_board_reset():
    b = Board(2, 2, ".")
    b.setCell(0, 0, "X")
    b.setCell(1, 1, "Y")

    b.reset()

    assert b.getCell(0, 0) == "."
    assert b.getCell(1, 1) == "."
    assert b.fill == "."


def test_board_overlay():
    b = Board(3, 3)
    b.overlay(0, 0, ["AB", "C "])

    assert b.getCell(0, 0) == "A"
    assert b.getCell(0, 1) == "B"
    assert b.getCell(1, 0) == "C"
    assert b.getCell(1, 1) == " "


def test_add_and_remove_sprite():
    b = Board(4, 4)
    s = Sprite(1, 1, ["X"])

    assert b.addSprite(s) is True
    assert b.getCell(1, 1) == "X"
    assert b.addSprite(s) is False
    assert b.removeSprite(s) is True
    assert b.removeSprite(s) is False


def test_sprite_move():
    s = Sprite(5, 5, ["X"])

    s.move("up")
    assert s.row == 4

    s.move("left", 2)
    assert s.col == 3

    s.move("down", 3)
    assert s.row == 7

    s.move("right", 4)
    assert s.col == 7


def test_sprite_alter():
    s = Sprite(5, 5, ["XX", "XX"])

    s.alter(["X"], startingPoint="bottomRight")

    assert s.height == 1
    assert s.width == 1
    assert s.row == 6
    assert s.col == 6


def test_string_mask_conversion():
    mask = Sprite.stringToMask("AB\nCD")

    assert mask == [["A", "B"], ["C", "D"]]
    assert Sprite.maskToString(mask) == "AB\nCD"
    assert len(mask) == 2


def test_scrolling_board_scroll_left():
    b = ScrollingBoard(2, 5)
    s = Sprite(0, 3, ["X"])
    b.addSprite(s)

    b.scrollLeft(2)

    assert s.col == 1
    assert b.getCell(0, 1) == "X"
    assert b.getCell(0, 3) == " "


def test_scrolling_board_loading_zone():
    b = ScrollingBoard(2, 5, loadingZone=3)
    s = Sprite(0, 0, ["X"])

    b.addSpriteToLoadingZone(s, offset=1)

    assert s.col == 6
    assert b.inLoadingZone(s) is True
    assert b.isOffScreenLeft(s) is False

def test_sprites_collide_ignores_fill():
    b = Board(5, 5)

    s1 = Sprite(1, 1, ["X "], fill=" ")
    s2 = Sprite(1, 2, [" X"], fill=" ")

    assert b.spritesCollide(s1, s2) is False  # bounding boxes overlap, solid pixels do not
    assert b.spritesCollide(s1, Sprite(1, 1, ["X"], fill=" ")) is True
    assert b.spritesCollide(s2, Sprite(1, 3, ["X"], fill=" ")) is True
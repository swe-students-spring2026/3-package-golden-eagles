import pathlib
import sys
import random
import pytest


PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

from snake.core import change_direction, create_game_state, tick, spawn_food


def test_create_game_state_defaults():
    state = create_game_state(width=8, height=8, start_length=3, seed=42)

    assert state["width"] == 8
    assert state["height"] == 8
    assert len(state["snake"]) == 3
    assert state["direction"] == "RIGHT"
    assert state["score"] == 0
    assert state["game_over"] is False
    assert state["food"] not in state["snake"]


def test_create_game_state_invalid_inputs():
    with pytest.raises(ValueError):
        create_game_state(width=3, height=8)

    with pytest.raises(ValueError):
        create_game_state(width=8, height=3)

    with pytest.raises(ValueError):
        create_game_state(width=8, height=8, start_length=1)

    with pytest.raises(ValueError):
        create_game_state(width=5, height=8, start_length=6)


def test_change_direction_prevents_reverse():
    assert change_direction("RIGHT", "LEFT") == "RIGHT"
    assert change_direction("UP", "DOWN") == "UP"
    assert change_direction("left", "up") == "UP"


def test_change_direction_valid():
    assert change_direction("RIGHT", "UP") == "UP"
    assert change_direction("UP", "LEFT") == "LEFT"
    assert change_direction("LEFT", "DOWN") == "DOWN"
    assert change_direction("DOWN", "RIGHT") == "RIGHT"


def test_change_direction_invalid_inputs():
    with pytest.raises(ValueError):
        change_direction("RIGHT", "DIAGONAL")

    with pytest.raises(ValueError):
        change_direction("FORWARD", "LEFT")

    with pytest.raises(TypeError):
        change_direction("UP", None)

    with pytest.raises(TypeError):
        change_direction(123, "LEFT")


def test_tick_moves_snake_one_step():
    state = create_game_state(width=8, height=8, start_length=3, seed=1)
    head_before = state["snake"][0]

    next_state = tick(state)

    assert next_state["snake"][0] == (head_before[0] + 1, head_before[1])
    assert len(next_state["snake"]) == len(state["snake"])
    assert next_state["score"] == 0
    assert next_state["game_over"] is False


def test_tick_eats_food_and_grows():
    state = create_game_state(width=8, height=8, start_length=3, seed=1)
    head_x, head_y = state["snake"][0]
    state["food"] = (head_x + 1, head_y)

    next_state = tick(state)

    assert next_state["score"] == 1
    assert len(next_state["snake"]) == len(state["snake"]) + 1
    assert next_state["snake"][0] == (head_x + 1, head_y)
    assert next_state["game_over"] is False


def test_tick_sets_game_over_on_wall_collision():
    state = create_game_state(width=4, height=6, start_length=2, seed=5)
    state["snake"] = [(3, 3), (2, 3)]
    state["direction"] = "RIGHT"

    next_state = tick(state)

    assert next_state["game_over"] is True
    assert next_state["score"] == 0
    assert next_state["direction"] == "RIGHT"


def test_spawn_food_valid_position():
    random_generator = random.Random(42)
    snake = [(0, 0), (1, 0), (2, 0)]
    width, height = 5, 5
    food = spawn_food(width, height, snake, random_generator)

    assert food is not None
    assert isinstance(food, tuple)
    assert len(food) == 2
    assert 0 <= food[0] < width
    assert 0 <= food[1] < height
    assert food not in snake


def test_spawn_food_board_full():
    random_generator = random.Random(42)
    width, height = 2, 2
    snake = [(0, 0), (0, 1), (1, 0), (1, 1)]
    food = spawn_food(width, height, snake, random_generator)

    assert food is None
    assert len(snake) == 4
    assert snake[0] == (0, 0)


def test_tick_sets_game_over_on_self_collision():
    state = create_game_state(width=10, height=10, start_length=5, seed=5)
    # Arrange snake in a loop about to hit itself
    state["snake"] = [(5, 5), (6, 5), (6, 6), (5, 6), (4, 6)]
    state["direction"] = "DOWN"

    next_state = tick(state)

    assert next_state["game_over"] is True
    assert next_state["score"] == 0
    assert next_state["direction"] == "DOWN"
    assert len(next_state["snake"]) == 5
    assert next_state["snake"][0] == (5, 5)


def test_tick_invalid_requested_direction_raises():
    state = create_game_state(width=8, height=8, start_length=3, seed=7)

    with pytest.raises(ValueError):
        tick(state, requested_direction="DIAGONAL")

    with pytest.raises(TypeError):
        tick(state, requested_direction=0)

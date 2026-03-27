import random

DIRECTIONS = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
}

OPPOSITE_DIRECTIONS = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT",
}


def _normalize_direction(direction):
    """
    Validate and normalize a direction string.
    """
    if not isinstance(direction, str):
        raise TypeError("Direction must be string.")
    normalized = direction.upper().strip()
    if normalized not in DIRECTIONS:
        raise ValueError(f"Invalid direction: {direction}")
    return normalized


def create_game_state(width, height, start_length=3, seed=None):
    """
    Create the initial snake game state.
    """
    if width < 4 or height < 4:
        raise ValueError("Board width and height must both be at least 4.")
    if start_length < 2:
        raise ValueError("start_length must be at least 2.")
    if start_length > width:
        raise ValueError("start_length cannot be larger than board width.")

    random_generator = random.Random(seed)
    start_x = width // 2
    start_y = height // 2
    snake = [(start_x - offset, start_y) for offset in range(start_length)]
    food = spawn_food(width, height, snake, random_generator)

    return {
        "width": width,
        "height": height,
        "snake": snake,
        "direction": "RIGHT",
        "food": food,
        "score": 0,
        "game_over": False,
        "rng": random_generator,
    }


def spawn_food(width, height, snake, random_generator):
    """
    Pick a random unoccupied board cell for food.
    """
    occupied_positions = set(snake)
    open_cells = [
        (column, row)
        for row in range(height)
        for column in range(width)
        if (column, row) not in occupied_positions
    ]
    if not open_cells:
        return None
    return random_generator.choice(open_cells)


def change_direction(current_direction, requested_direction):
    """
    Snake direction change, disallowing immediate reversal.
    """
    normalized_current = _normalize_direction(current_direction)
    normalized_requested = _normalize_direction(requested_direction)

    if OPPOSITE_DIRECTIONS[normalized_current] == normalized_requested:
        return normalized_current
    return normalized_requested


def _next_head_position(head_position, direction):
    """
    Compute the next head coordinate for a direction.
    """
    dx, dy = DIRECTIONS[direction]
    return (head_position[0] + dx, head_position[1] + dy)


def tick(state, requested_direction=None):
    """
    Advance the game by one tick and returns the next state.
    """
    if state["game_over"]:
        return state.copy()

    current_direction = state["direction"]
    if requested_direction is not None:
        current_direction = change_direction(current_direction, requested_direction)

    snake = state["snake"]
    current_head = snake[0]
    new_head = _next_head_position(current_head, current_direction)
    width = state["width"]
    height = state["height"]
    food = state["food"]

    ate_food = new_head == food
    collision_body = snake if ate_food else snake[:-1]

    out_of_bounds = (
        new_head[0] < 0
        or new_head[0] >= width
        or new_head[1] < 0
        or new_head[1] >= height
    )
    hit_body = new_head in collision_body

    if out_of_bounds or hit_body:
        new_state = state.copy()
        new_state["direction"] = current_direction
        new_state["game_over"] = True
        return new_state

    new_snake = [new_head, *snake]
    new_score = state["score"]
    new_food = food

    if ate_food:
        new_score += 1
        new_food = spawn_food(width, height, new_snake, state["rng"])
    else:
        new_snake.pop()

    return {
        **state,
        "snake": new_snake,
        "direction": current_direction,
        "food": new_food,
        "score": new_score,
        "game_over": False,
    }

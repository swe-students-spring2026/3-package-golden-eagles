from .core import create_game_state


def main():
    state = create_game_state(width=12, height=12, start_length=3)
    print("Snake basics are ready.")
    print(f"Board: {state['width']} by {state['height']}, score={state['score']}")


if __name__ == "__main__":
    main()

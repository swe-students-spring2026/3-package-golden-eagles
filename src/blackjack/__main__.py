from .game import start_blackjack
from .card import Card

if __name__ == '__main__':
    start_blackjack(Card.generate_deck())
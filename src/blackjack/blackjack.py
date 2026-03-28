from random import choice
from card import Card

def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")
    player_card1 = choice(deck)
    dealer_card_shown = choice(deck)


start_blackjack(Card.generate_deck())

# python src/blackjack/blackjack.py
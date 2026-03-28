from random import choice
from card import Card

def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")

    player_card1 = Card.pick_card(deck)
    dealer_card_shown = Card.pick_card(deck)
    player_card2 = Card.pick_card(deck)
    dealer_card_hidden = Card.pick_card(deck)

    print("Dealers:")
    dealer_card_shown.print_card()
    Card.print_blank()

    print("Your cards:")
    player_card1.print_card()
    player_card2.print_card()




start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
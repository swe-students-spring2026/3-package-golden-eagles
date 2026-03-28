from random import choice
from card import Card

def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")

    player_card1 = Card.pick_card(deck)
    dealer_card_shown = Card.pick_card(deck)
    player_card2 = Card.pick_card(deck)
    dealer_card_hidden = Card.pick_card(deck)

    # print(f"Player's cards: {player_card1.num} of {player_card1.suit}, {player_card2.num} of {player_card2.suit}")
    # print(f"Dealer's card: {dealer_card_shown.num} of {dealer_card_shown.suit}, {dealer_card_hidden.num} of {dealer_card_hidden.suit}")
    # for card in deck:
    #     print(f"{card.num} of {card.suit}")
    player_card1.print_card()




start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
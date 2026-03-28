from random import choice
from card import Card

def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")

    player_card1 = Card.pick_card(deck)
    dealer_card_shown = Card.pick_card(deck)
    player_card2 = Card.pick_card(deck)
    dealer_card_hidden = Card.pick_card(deck)

    player_cards = [player_card1, player_card2]
    dealer_cards = [dealer_card_shown]
    print_table(player_cards, dealer_cards, True)

def print_table(player_cards, dealer_cards, players_turn):
    if(players_turn):
        print("Dealers:")
        for card in dealer_cards:
            print(card.print_card())
        print(Card.print_blank())
    else:
        print("Dealers:")
        for card in dealer_cards:
            print(card.print_card())

    print("Your cards:")
    for card in player_cards:
        print(card.print_card())

def stand_hit(player_total, deck):
    while True:
        print("Hit or Stand? (H-hit/X-stand)")
        x = input()

        if x.upper() == "H":
            new_card = Card.pick_card(deck)
            player_total += new_card.num
            print("You drew:")
            print(new_card.print_card())

        elif x.upper() == "X":
            return "stand"
        else:
            print("Invalid input: Enter 'H' for hit or 'X' for stand")

start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
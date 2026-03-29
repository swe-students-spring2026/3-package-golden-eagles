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

    player_total = sum(card.num for card in player_cards)
    while True:
        if not hit_stand(player_total, player_cards, deck):
            break
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

def hit_stand(player_total, player_cards, deck):
    while True:
        print("Hit or Stand? (A-hit/D-stand)")
        x = input()

        if x.upper() == "A":
            new_card = Card.pick_card(deck)
            player_cards.append(new_card)
            player_total += new_card.num
            print("You drew:")
            print(new_card.print_card())
            return True
        elif x.upper() == "D":
            print("You stand")
            return False
        else:
            print("Invalid input: Enter 'A' for hit or 'D' for stand")
        
def pause():
    print("Press Enter to continue...")
    input()

start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
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
    if(check_player_total(player_total)):
        return
    while True:
        if not hit_stand(player_total, player_cards, deck):
            break
        print_table(player_cards, dealer_cards, True)

def print_table(player_cards, dealer_cards, players_turn):
    if(players_turn):
        print("Dealers:")
        split_cards = [dealer_cards[0].print_card().split('\n'), Card.print_blank().split('\n')]
        for index in range(len(split_cards[0])):
            line = ""
            for card in split_cards:
                line += card[index] + "   "
            print(line)
    else:
        split_cards = list(map(lambda card: ard.print_card().split('\n'), dealer_cards))
        for index in range(len(split_cards[0])):
            line = ""
            for card in split_cards:
                line += card[index] + "   "
            print(line)

    print("Your cards:")
    split_cards = list(map(lambda card: card.print_card().split('\n'), player_cards))
    for index in range(len(split_cards[0])):
        line = ""
        for card in split_cards:
            line += card[index] + "   "
        print(line)
        

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

def check_player_total(player_total):
    if(player_total == 21):
        print("Blackjack! You win!")
        return True
    if player_total > 21:
        print("Bust. Dealer wins")
        return True
    return False

def check_dealer_total(dealer_total):
    if(dealer_total == 21):
        print("Blackjack! Dealer wins")
        return True
    if dealer_total > 21:
        print("Bust. You win!")
        return True
    return False

def check_winner(player_total, dealer_total):
    if player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins!")
    else:
        print("A tie is practically a loss")

def pause():
    print("Press Enter to continue...")
    input()

start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
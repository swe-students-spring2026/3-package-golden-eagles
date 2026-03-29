from random import choice
from .card import Card

def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")

    # pick cards
    player_card1 = Card.pick_card(deck)
    dealer_card_shown = Card.pick_card(deck)
    player_card2 = Card.pick_card(deck)
    dealer_card_hidden = Card.pick_card(deck)

    # help print the cards
    player_cards = [player_card1, player_card2]
    dealer_cards = [dealer_card_shown]
    print_table(player_cards, dealer_cards, True)

    # check for blackjack or bust
    player_total = sum(card.num for card in player_cards)
    if(check_player_total(player_total)):
        return
    
    # player turn
    while True:
        player_total = hit_stand(player_total, player_cards, deck)
        if(not player_total):
            print("Dealers turn\n")
            pause()
            break
        if(check_player_total(player_total)):
            return
        pause()
        print_table(player_cards, dealer_cards, True)
    
    # check dealer blackjack or bust
    dealer_cards.append(dealer_card_hidden)
    dealer_total = sum(card.num for card in dealer_cards)
    if(check_dealer_total(dealer_total)):
        return

    # dealer turn
    while True:
        print_table(player_cards, dealer_cards, False)
        pause()
        dealer_total = dealer_turn(dealer_cards, dealer_total, deck)
        if(not dealer_total):
            break
        if(check_dealer_total(dealer_total)):
            return
        pause()

    # check winner
    print(check_winner(player_total, dealer_total))

# print dealer cards and player cards depending on turn
def print_table(player_cards, dealer_cards, players_turn):
    # dealer
    print("Dealers:")
    # if dealer 2nd card must still be hidden 
    if(players_turn):
        split_cards = [dealer_cards[0].print_card().split('\n'), Card.print_blank().split('\n')]
        for index in range(len(split_cards[0])):
            line = ""
            for card in split_cards:
                line += card[index] + "   "
            print(line)
    # dealers turn so show all cards
    else:
        split_cards = list(map(lambda card: card.print_card().split('\n'), dealer_cards))
        for index in range(len(split_cards[0])):
            line = ""
            for card in split_cards:
                line += card[index] + "   "
            print(line)

    # player
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
            # print(f"new card {new_card.suit} {new_card.num}")

            print("You drew:")
            print(new_card.print_card())
            # print(f"Your new total is {player_total}")
            return player_total
        elif x.upper() == "D":
            print("You stand")
            return False
        else:
            print("Invalid input: Enter 'A' for hit or 'D' for stand")

def dealer_turn(dealer_cards, dealer_total, deck):
    while True:
        if(dealer_total < 17):
            new_card = Card.pick_card(deck)
            dealer_cards.append(new_card)
            dealer_total += new_card.num

            print("Dealer hits")
            print("Dealer drew:")
            print(new_card.print_card())
            return dealer_total
        else:
            print("Dealer stands")
            return False

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
        return "You win!"
    elif player_total < dealer_total:
        return "Dealer wins!"
    else:
        return "A tie is practically a loss"

def pause():
    print("Press Enter to continue...")
    input()

# start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py
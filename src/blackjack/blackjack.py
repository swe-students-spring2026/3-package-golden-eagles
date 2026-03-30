from random import choice
from card import Card

# check player total for blackjack or bust
def check_player_total(player_total):
    if(player_total == 21):
        print("Blackjack! You win!")
        return True
    if player_total > 21:
        print("Bust. You lose!")
        return True
    return False

# check dealer total for blackjack or bust
def check_dealer_total(dealer_total):
    if(dealer_total == 21):
        print("Dealer Blackjack! You lose!")
        return True
    if dealer_total > 21:
        print("Dealer Bust. You win!")
        return True
    return False

# check winner at end of game
def check_winner(player_total, dealer_total):
    print(f"Player total end: {player_total}")
    print(f"Dealer total end: {dealer_total}")
    if player_total > dealer_total:
        return "You win!"
    elif player_total < dealer_total:
        return "Dealer wins!"
    else:
        return "A tie is practically a loss"

# intermediate pause for user flow
def pause():
    print("Press Enter to continue...")
    input()

# print dealer cards and player cards depending on turn
def print_table(player_cards, dealer_cards, players_turn=False):
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

# check if ace is in hand
def ace_check(total, cards):
    for card in cards:
        if(card.is_ace and card.num == 1):
            if(total + 10 <= 21 and total + 10 > total):
                return total + 10
    return total

# ace can be 1 or 11 
def change_ace_value(total, cards, is_dealer=False):
    if(is_dealer):
        for card in cards:
            if(card.is_ace and total + 10 >= 17 and total + 10 <= 21):
                card.num = 11
                return total + 10
        return total
    
    for card in cards:
        if(card.is_ace and card.num == 1 and total + 10 == 21):
            card.num = 11
            return total + 10
    return total

# Player turn, 2 options, hit for new card or stand to end turn
def hit_stand(player_total, player_cards, deck):
    while True:
        print("Hit or Stand? (A-hit/D-stand)")
        x = input()

        # hit
        if x.upper() == "A":
            new_card = Card.pick_card(deck)
            player_cards.append(new_card)
            player_total += new_card.num

            print("You drew:")
            print(new_card.print_card())
            return player_total
        
        # stand
        elif x.upper() == "D":
            print("You stand")
            return player_total
        
        # wrong input
        else:
            print("Invalid input: Enter 'A' for hit or 'D' for stand")

# Dealer turn, automatically hit until 17 or higher then stand
def dealer_turn(dealer_cards, dealer_total, deck):
    while True:
        # hit 
        if(dealer_total < 17):
            new_card = Card.pick_card(deck)
            dealer_cards.append(new_card)
            dealer_total += new_card.num

            print("Dealer hits")
            print("Dealer drew:")
            print(new_card.print_card())
            return dealer_total
        # stand
        else:
            print("Dealer stands")
            return dealer_total

# main game
def start_blackjack(deck):
    print("Lazy huh? Lets run a round of blackjack")
    print("Dealing cards...")

    # pick cards
    Card.blackjack_value(deck)  
    player_card1 = Card.pick_card(deck)
    dealer_card_shown = Card.pick_card(deck)
    player_card2 = Card.pick_card(deck)
    dealer_card_hidden = Card.pick_card(deck)

    # help print the cards
    player_cards = [player_card1, player_card2]
    dealer_cards = [dealer_card_shown, dealer_card_hidden]
    print_table(player_cards, dealer_cards, True)

    # check for blackjack or bust
    player_total = sum(card.num for card in player_cards)
    player_total = change_ace_value(player_total, player_cards)

    if(check_player_total(player_total)):
        return
    
    # player turn
    while True:
        did_player_stand = player_total
        player_total = hit_stand(player_total, player_cards, deck)
        player_total = change_ace_value(player_total, player_cards)
        if(check_player_total(player_total)):
            return
        if(did_player_stand == player_total):
            print("Dealers turn\n")
            pause()
            break
        pause()
        print_table(player_cards, dealer_cards, True)
    
    # check dealer blackjack or bust
    # check initial total before ace is changed to 11
    print("Unveiling dealers hidden card")
    print_table(player_cards, dealer_cards)
    pause()

    dealer_total = sum(card.num for card in dealer_cards)
    dealer_total = change_ace_value(dealer_total, dealer_cards, True)
    if(check_dealer_total(dealer_total)):
        return

    # dealer turn
    while True:
        dealer_total = dealer_turn(dealer_cards, dealer_total, deck)
        dealer_total = change_ace_value(dealer_total, dealer_cards, True)
        print_table(player_cards, dealer_cards)
        if(check_dealer_total(dealer_total)):
            return
        if(dealer_total >= 17):
            break
        pause()

    # check winner
    print(check_winner(ace_check(player_total, player_cards), dealer_total))

start_blackjack(Card.generate_deck())
# python src/blackjack/blackjack.py

# when dealer blackjacks off first two cards
# user desnt even see them
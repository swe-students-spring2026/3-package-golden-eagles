import pytest
from src.blackjack import Card, check_player_total, check_dealer_total, check_winner, change_ace_value

# python -m pytest tests/test_blackjack.py
# python3 -m pytest tests/test_blackjack.py
# when testing make sure start_blackjack is not being called in blackjack.py

# Test cases for the card class and deck generation
class TestCard:
    def test_card_creation(self):
        # test card creation     
        heart = Card("Hearts", 5)
        assert heart.suit == "Hearts"
        assert heart.num == 5

        diamond = Card("Diamonds", 7)
        assert diamond.suit == "Diamonds"
        assert diamond.num == 7

        club = Card("Clubs", 1)
        assert club.suit == "Clubs"
        assert club.num == 1

        spade = Card("Spades", 9)
        assert spade.suit == "Spades"
        assert spade.num == 9

    def test_deck_creation(self):
        deck = Card.generate_deck()
        assert len(deck) == 52

        for card in deck:
            assert isinstance(card, Card)
            assert card.suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            assert card.num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
    def test_blackjack_value(self):
        deck = Card.generate_deck()
        Card.blackjack_value(deck)

        for card in deck:
            assert isinstance(card, Card)
            assert card.suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            assert card.num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            if(card.is_face):
                assert card.num == 10
            if(card.is_ace):
                assert card.num == 1

    def test_pick_card(self):
        deck = Card.generate_deck()
        initial_length = len(deck)

        card = Card.pick_card(deck)

        assert len(deck) == initial_length-1
        assert isinstance(card, Card)
        assert card not in deck

"""
Don't think we can test user input functions
"""
# Test cases for game logic and function of blackjack
class TestBlackjack:
    def test_check_player_total(self):
        # test math logic for player total
        assert check_player_total(21) == 21
        assert check_player_total(22) == 22
        assert check_player_total(20) == 20

    def test_check_dealer_total(self):
        # test math logic for dealer total
        assert check_dealer_total(21) == 21
        assert check_dealer_total(22) == True
        assert check_dealer_total(20) == False

    def test_check_winner(self):
        # test winner logic
        assert check_winner(22, 19) == 'Your hand busts. You lose'
        assert check_winner(20, 19) == 'Your hand wins!'
        assert check_winner(19, 20) == 'Dealer wins!'
        assert check_winner(20, 20) == 'A tie is practically a loss'

    def test_change_ace_value_player(self):
        # This first half is for player
        # test ace is not 11 when it would go over
        cards = [Card('Hearts', 1), Card('Hearts', 10),  Card('Hearts', 1)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards) == 12

        # test ace is 11 to reach 21
        cards = [Card('Hearts', 1), Card('Hearts', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards) == 21

        # test ace is 1 to reach 21
        cards = [Card('Hearts', 1), Card('Hearts', 10), Card('Clubs', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards) == 21
    
        # test no ace
        cards = [Card('Hearts', 10), Card('Hearts', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards) == 20
    
    def test_change_ace_value_dealer(self):
        # 2nd half is for dealer
        # test ace is 11 when total becomes 17 or more
        for i in range(6, 9):
            cards = [Card('Hearts', 1), Card('Hearts', i)]
            total = sum(card.num for card in cards)
            temp = change_ace_value(total, cards, True)
            assert temp >= 17 and temp <= 21

        # test ace is not 11 when it would go over
        cards = [Card('Hearts', 1), Card('Hearts', 10), Card('Hearts', 1)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards, True) == 12

        # test ace is 11 to reach 21
        cards = [Card('Hearts', 1), Card('Hearts', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards, True) == 21

        # test ace is 1 to reach 21
        cards = [Card('Hearts', 1), Card('Hearts', 10), Card('Clubs', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards, True) == 21
    
        # test no ace
        cards = [Card('Hearts', 10), Card('Hearts', 10)]
        total = sum(card.num for card in cards)
        assert change_ace_value(total, cards, True) == 20
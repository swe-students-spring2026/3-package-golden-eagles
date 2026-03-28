import pytest
from src.blackjack import Card

# python -m pytest tests/test_blackjack.py

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

    def test_pick_card(self):
        deck = Card.generate_deck()
        initial_length = len(deck)

        card = Card.pick_card(deck)

        assert len(deck) == initial_length - 1
        assert card not in deck

# Test cases for game logic and function of blackjack
# class TestBlackjack:
#     def test_start_blackjack(self, capsys):


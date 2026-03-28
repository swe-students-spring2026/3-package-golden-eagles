import pytest
from src.BlackJack.blackjack import Card

# pytest tests/test_blackjack.py

def test_card_creation():
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

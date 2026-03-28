from random import choice

class Card():
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num

    @staticmethod
    def generate_deck():
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        # remember an Ace is 1 or 11
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

        deck = []
        for suit in suits:
            for num in nums:
                card = Card(suit, num)
                deck.append(card)
        return deck
    
    @staticmethod
    def pick_card(deck):
        card = choice(deck)
        deck.remove(card)
        return card
    # │, ─, ┌, ┐,└, ┘
    def print_card(self):
        suits = {
            "Hearts": "♥",
            "Diamonds": "♦",
            "Clubs": "♣",
            "Spades": "♠"
        }

        royal = {
            1: "A",
            11: "J",
            12: "Q",
            13: "K"
        }

        suit = suits[self.suit]
        num = royal.get(self.num, str(self.num))

        if(num == "10"):
            print(f"┌─────────┐")
            print(f"│{num}     {num}│")
            print(f"│{suit}       {suit}│")
            print(f"│         │")
            print(f"│{suit}       {suit}│")
            print(f"│{num}     {num}│")
            print(f"└─────────┘")
        else:
            print(f"┌─────────┐")
            print(f"│{num}       {num}│")
            print(f"│{suit}       {suit}│")
            print(f"│         │")
            print(f"│{suit}       {suit}│")
            print(f"│{num}       {num}│")
            print(f"└─────────┘")
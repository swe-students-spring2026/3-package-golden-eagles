from random import choice

class Card():
    def __init__(self, suit, num):
        self.suit = suit
        self.num = num
        self.is_ace = 'A' if num == 1 else None

        royal = {
            11: "J",
            12: "Q",
            13: "K"
        }
        self.is_face = royal.get(self.num) if self.num in royal else None

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
    def blackjack_value(deck):
        for card in deck:
            if card.is_face:
                card.num = 10
    
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

        suit = suits[self.suit]
        if(self.is_ace):
            num = self.is_ace
        elif(self.is_face):
            num = self.is_face
        else:
            num = str(self.num)

        # can make them specific for every number but this works for now
        if(num == "10"):
            return f"""┌───────────┐
│{num}       {num}│
│{suit}         {suit}│
│           │
│           │
│           │
│{suit}         {suit}│
│{num}       {num}│
└───────────┘
"""
        else:
            return f"""┌───────────┐
│{num}         {num}│
│{suit}         {suit}│
│           │
│           │
│           │
│{suit}         {suit}│
│{num}         {num}│
└───────────┘
"""
           
    @staticmethod
    def print_blank():
        return """┌───────────┐
│           │
│           │
│           │
│           │
│           │
│           │
│           │
└───────────┘
"""
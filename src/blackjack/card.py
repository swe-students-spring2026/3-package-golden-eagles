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


# def blackjack():
#     # waste time with a game of blackjack
    
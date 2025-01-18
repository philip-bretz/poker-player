from poker.card import Suit, Rank, Card, CardCollection


class FrenchDeck(CardCollection):
    def __init__(self):
        cards = [Card(rank, suit) for suit in Suit for rank in Rank]
        super().__init__(cards)

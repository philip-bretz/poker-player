from dataclasses import dataclass
from enum import StrEnum

class Suit(StrEnum):
    SPADES = "spades"
    CLUBS = "clubs"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"


class Rank(StrEnum):
    ACE = "ace"
    TWO = "two"
    THREE = "three"
    FOUR = "four"
    FIVE = "five"
    SIX = "six"
    SEVEN = "seven"
    EIGHT = "eight"
    NINE = "nine"
    TEN = "ten"
    JACK = "jack"
    QUEEN = "queen"
    KING = "king"


@dataclass(frozen=True)
class Card:
    rank: Rank
    suit: Suit

    def __repr__(self) -> str:
        return f"Card({self.rank.value.capitalize()} of {self.suit.value.capitalize()})"


class CardCollection:
    def __init__(self, cards: list[Card]):
        self._cards = cards

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, index: int) -> Card:
        return self._cards[index]

    def shuffle(self) -> None:
        raise NotImplementedError

    def pop_top(self) -> Card:
        return self._cards.pop()

    def add_top(self, card: Card) -> None:
        self._cards.append(card)

    def __repr__(self) -> str:
        cards_txt = "["
        for card in self._cards:
            cards_txt += f"\n {card}"
        cards_txt += "\n]"
        return cards_txt

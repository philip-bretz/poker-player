from enum import StrEnum

from poker.card import Suit, Rank, Card, RANK_NUMERIC


class SuitOrdering(StrEnum):
    EQUAL = "equal"
    ALPHABETICAL = "alphabetical"


SUIT_MAP_ALPHA: dict[Suit, int] = {
    Suit.CLUBS: 0,
    Suit.DIAMONDS: 1,
    Suit.HEARTS: 2,
    Suit.SPADES: 3,
}


def build_ordering(aces_high: bool = True, suit_ordering: SuitOrdering = SuitOrdering.ALPHABETICAL) -> dict[Card, float]:
    rank_map = RANK_NUMERIC
    if aces_high:
        rank_map = {rank: rank_map[rank] if rank != Rank.ACE else rank_map[Rank.KING] + 1 for rank in rank_map.keys()}
    match suit_ordering:
        case SuitOrdering.EQUAL:
            return {Card(rank, suit): float(rank_map[rank]) for suit in Suit for rank in Rank}
        case SuitOrdering.ALPHABETICAL:
            return {Card(rank, suit): rank_map[rank] + SUIT_MAP_ALPHA[suit] / 4 for suit in Suit for rank in Rank}
        case _:
            raise NotImplementedError

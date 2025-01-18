from poker.card import Card, Rank, Suit


def _separate_by_rank(cards: list[Card]) -> dict[Rank, list[Card]]:
    cards_by_rank: dict[Rank, list[Card]] = {rank: [] for rank in Rank}
    for card in cards:
        cards_by_rank[card.rank].append(card)
    return cards_by_rank


def _separate_by_suit(cards: list[Card]) -> dict[Suit, list[Card]]:
    cards_by_suit: dict[Suit, list[Card]] = {suit: [] for suit in Suit}
    for card in cards:
        cards_by_suit[card.suit].append(card)
    return cards_by_suit


def _high_card(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    if len(cards) < 1:
        return None
    sorted_cards = sorted(cards, key=lambda card: ordering[card])
    return sorted_cards[-1]


def _one_pair(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    if len(cards) < 2:
        return None
    cards_by_rank = _separate_by_rank(cards)
    # List of rank-grouped (sorted) cards >= 2
    pairs = [
        sorted(cards_by_rank[rank], key=lambda card: ordering[card]) for rank in cards_by_rank.keys() if len(cards_by_rank) >= 2
    ]
    if len(pairs) < 1:
        return None
    sorted_pairs = sorted(pairs, key=lambda cards: ordering[cards[-1]])
    return sorted_pairs[-1][-1]


def _two_pair(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    if len(cards) < 4:
        return None
    cards_by_rank = _separate_by_rank(cards)
    # List of rank-grouped (sorted) cards >= 2
    pairs = [
        sorted(cards_by_rank[rank], key=lambda card: ordering[card]) for rank in cards_by_rank.keys() if len(cards_by_rank) >= 2
    ]
    if len(pairs) < 2:
        return None
    sorted_pairs = sorted(pairs, key=lambda cards: ordering[cards[-1]])
    return sorted_pairs[-1][-1]


def _three_of_a_kind(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    if len(cards) < 3:
        return None
    cards_by_rank = _separate_by_rank(cards)
    # List of rank-grouped (sorted) cards >= 3
    triples = [
        sorted(cards_by_rank[rank], key=lambda card: ordering[card]) for rank in cards_by_rank.keys() if len(cards_by_rank) >= 3
    ]
    if len(triples) < 1:
        return None
    sorted_triples = sorted(triples, key=lambda cards: ordering[cards[-1]])
    return sorted_triples[-1][-1]


def _full_house(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    if len(cards) < 5:
        return None
    cards_by_rank = _separate_by_rank(cards)
    # List of rank-grouped (sorted) cards >= 3
    triples = [
        sorted(cards_by_rank[rank], key=lambda card: ordering[card]) for rank in cards_by_rank.keys() if len(cards_by_rank) >= 3
    ]
    if len(triples) < 1:
        return None
    sorted_triples = sorted(triples, key=lambda cards: ordering[cards[-1]])
    selected_triple = sorted_triples[-1]
    # List of rank-grouped (sorted) cards >= 2, that are not the selected triple
    pairs = [
        sorted(
            cards_by_rank[rank], 
            key=lambda card: ordering[card],
        ) for rank in cards_by_rank.keys() if len(cards_by_rank) >= 2 and rank != selected_triple[-1].rank
    ]
    if len(pairs) < 1:
        return None
    sorted_pairs = sorted(pairs, key=lambda cards: ordering[cards[-1]])
    selected_pair = sorted_pairs[-1]
    sorted_hand = sorted(selected_pair + selected_triple, key=lambda card: ordering[card])
    return sorted_hand[-1]


def _straight(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    raise NotImplementedError


def _flush(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    raise NotImplementedError


def _straight_flush(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    raise NotImplementedError


def _five_of_a_kind(cards: list[Card], ordering: dict[Card, float]) -> Card | None:
    raise NotImplementedError


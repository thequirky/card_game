from __future__ import annotations

import random

from card.card import Card


class Pile:
    def __init__(self, name: str, cards=None) -> None:
        if cards is None:
            cards = list()
        self.name = name.strip().capitalize()
        self.cards = cards

    @classmethod
    def from_seed(cls, seed: str, name: str) -> Pile:
        if not seed:
            return cls(name=name)
        cards = [CHARACTER_TO_CARD[c] for c in seed]
        return cls(name=name, cards=cards)

    def is_empty(self) -> bool:
        return not self.cards

    def shuffle(self) -> None:
        if self.is_empty():
            raise ValueError("Cannot shuffle an empty pile.")
        random.shuffle(self.cards)

    def add(self, card: Card) -> None:
        if not card:
            raise ValueError("Cannot add None to the pile.")
        if not isinstance(card, Card):
            raise TypeError("Can only add a Card object to the pile.")
        if self.is_empty():
            self.cards = [card]
            return
        self.cards.append(card)

    def reshuffle(self, other_pile: Pile) -> None:
        if not other_pile.cards:
            raise ValueError("Cannot reshuffle with None.")
        if not isinstance(other_pile, Pile):
            raise TypeError("Can only reshuffle with a Pile object.")
        self.cards.extend(other_pile.cards)
        self.shuffle()

    def draw_top(self) -> Card:
        if self.is_empty():
            raise ValueError("Cannot draw top card from an empty pile.")
        return self.cards.pop()

    def draw_random(self) -> Card:
        if self.is_empty():
            raise ValueError("Cannot darw a random card from an empty pile.")
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        pile_str = ", ".join([card.name for card in self.cards])
        return f"{self.name} pile -> [{pile_str}]"

    def __repr__(self) -> str:
        return f"Pile=(name='{self.name}', cards={self.cards})"


CHARACTER_TO_CARD = {"A": Card.Ace, "K": Card.King, "Q": Card.Queen, "J": Card.Joker}

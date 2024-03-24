from __future__ import annotations

import random
from enum import Enum


class Card(Enum):
    Ace = 3
    King = 2
    Queen = 1
    Joker = 0

    def __str__(self) -> str:
        return f"[{self.name}]"


CHARACTER_TO_CARD = {"A": Card.Ace, "K": Card.King, "Q": Card.Queen, "J": Card.Joker}


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
        return cls(name=name, cards=[CHARACTER_TO_CARD[c] for c in seed])

    def is_empty(self) -> bool:
        return not self.cards

    def shuffle(self, other: Pile = None) -> None:
        if other:
            self.cards.extend(other.cards)
        random.shuffle(self.cards)

    def add(self, card: Card) -> None:
        if self.is_empty():
            self.cards = [card]
        else:
            self.cards.append(card)

    def draw_top(self) -> Card:
        return self.cards.pop()

    def draw_random(self) -> Card:
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        pile_str = ", ".join([card.name for card in self.cards])
        return f"{self.name} pile -> [{pile_str}]"

    def __repr__(self) -> str:
        return f"Pile=(name='{self.name}', cards={self.cards})"

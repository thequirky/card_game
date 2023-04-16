from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum


class Card(Enum):
    Ace = 3
    King = 2
    Queen = 1
    Joker = 0

    def __str__(self) -> str:
        return f"[{self.name}]"


CHARACTER_TO_CARD = {"A": Card.Ace, "K": Card.King, "Q": Card.Queen, "J": Card.Joker}


@dataclass
class Pile:
    name: str | None = field(default=None, compare=False)
    cards: list[Card] | None = field(default_factory=list)

    @classmethod
    def from_seed(cls, seed: str, name: str) -> Pile:
        if not seed:
            return cls(cards=field(default_factory=list), name=name)
        cards = [CHARACTER_TO_CARD[c] for c in seed]
        return cls(cards=cards, name=name)

    @property
    def is_empty(self) -> bool:
        return not self.cards

    def shuffle(self) -> None:
        if not self.cards:
            raise TypeError("Cannot shuffle an empty pile.")
        random.shuffle(self.cards)

    def add_to_top(self, card: Card) -> None:
        if not card:
            raise TypeError("Cannot add None to the pile.")
        if not isinstance(card, Card):
            raise TypeError("Can only add a Card object to the pile.")
        self.cards.append(card)

    def get_top_card(self) -> Card:
        if self.is_empty:
            raise TypeError("Cannot get top card from an empty pile.")
        return self.cards.pop()

    def get_random_card(self) -> Card:
        if self.is_empty:
            raise TypeError("Cannot get a random card from an empty pile.")
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        if self.is_empty:
            return f"The {self.name} pile is empty."
        pile_str = ", ".join([card.name for card in self.cards])
        return f"The {self.name} pile is: [{pile_str}]"

    def __repr__(self) -> str:
        return f"Pile=(name='{self.name}', cards={self.cards})"

if __name__ == "__main__":
    pile = Pile.from_seed(seed="AAAAKKKQQQQJJJJ", name="test")
    pile.shuffle()
    print(pile)

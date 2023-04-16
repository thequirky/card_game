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
    def __init__(self, name: str, cards: list[Card] | None = None) -> None:
        self.name = name.strip().capitalize()
        if not cards:
            self.cards = [] 
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
        if not self.cards:
            raise ValueError("Cannot shuffle an empty pile.")
        random.shuffle(self.cards)

    def add(self, card: Card) -> None:
        if not card:
            raise ValueError("Cannot add None to the pile.")
        if not isinstance(card, Card):
            raise TypeError("Can only add a Card object to the pile.")
        if not self.cards:
            self.cards = [card]
            return
        self.cards.append(card)

    def reshuffle(self, pile: Pile) -> None:
        if not pile.cards:
            raise ValueError("Cannot reshuffle with None.")
        if not isinstance(pile, Pile):
            raise TypeError("Can only reshuffle with a Pile object.")
        self.cards.extend(pile.cards)
        self.shuffle()

    def draw_top(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot draw top card from an empty pile.")
        return self.cards.pop()

    def draw_random(self) -> Card:
        if not self.cards:
            raise ValueError("Cannot darw a random card from an empty pile.")
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        pile_str = ", ".join([card.name for card in self.cards])
        return f"{self.name} pile -> [{pile_str}]"

    def __repr__(self) -> str:
        return f"Pile=(name='{self.name}', cards={self.cards})"
    

if __name__ == "__main__":
    pile = Pile.from_seed(seed="AAKKQQJJ", name="test")
    print(pile)
    pile.shuffle()
    print(pile)

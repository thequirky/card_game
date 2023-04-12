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


STR_TO_CARD = {"A": Card.Ace, "K": Card.King, "Q": Card.Queen, "J": Card.Joker}


@dataclass
class Pile:
    name: str | None = field(default=None, compare=False)
    cards: list[Card] | None = field(default_factory=list)

    @classmethod
    def from_str(cls, seed_str: str, name: str) -> Pile:
        if not seed_str:
            return cls(cards=field(default_factory=list), name=name)
        cards = [STR_TO_CARD[s] for s in seed_str]
        return cls(cards=cards, name=name)

    @property
    def is_empty(self) -> bool:
        return not self.cards

    def shuffle(self) -> None:
        if self.cards:
            random.shuffle(self.cards)

    def add_to_top(self, card: Card) -> None:
        if not card:
            raise TypeError("Cannot add None to the pile...")
        if not isinstance(card, Card):
            raise TypeError("Can only add a Card object to the pile...")
        self.cards.append(card)

    def get_top_card(self) -> Card:
        if self.is_empty:
            raise TypeError("Cannot get top card from an empty pile...")
        return self.cards.pop()

    def get_random_card(self) -> Card:
        if self.is_empty:
            raise TypeError("Cannot get a random card from an empty pile...")
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        pile_str = ", ".join([card.name for card in self.cards])
        return f"The {self.name} pile is: [{pile_str}]"


if __name__ == "__main__":
    print("\nCreate discard pile:")
    discard_pile = Pile("discard")
    print(discard_pile)

    print("\nCreate game pile:")
    pile = Pile("game")
    print(pile)

    print("\nCompare two empty piles:")
    assert pile == discard_pile
    print("compared ok")

    print("\nCreate pile from string")
    pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="from string")
    print(pile)

    print("\nShuffle cards in pile")
    pile.shuffle()
    print(pile)

    print("\nPick card from top of pile")
    card = pile.get_top_card()
    print(f"Removed: {card}")
    print(pile)

    print(f"\nAdd picked card {card} to discard pile")
    discard_pile.add_to_top(card)
    print(discard_pile)

    print("\nAdd a new card to the top of the pile")
    new_card = Card.Ace
    pile.add_to_top(new_card)
    print(f"Added {new_card} on top:")
    print(pile)

    print("\nRemove a random card from the pile:")
    random_card = pile.get_random_card()
    print(f"Removed: {random_card}")
    print(pile)

    print(f"\nAdd removed card {random_card} to the discard pile:")
    discard_pile.add_to_top(random_card)
    print(discard_pile)

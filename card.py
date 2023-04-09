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
    name: str = field(default=None, compare=False)
    cards: list[Card] = field(default_factory=list)

    @classmethod
    def from_str(cls, seed_str: str, name: str) -> Pile:
        if not seed_str:
            return cls(cards=field(default_factory=list), name=name)
        cards = [STR_TO_CARD[s] for s in seed_str]
        return cls(cards=cards, name=name)

    @property
    def is_empty(self) -> bool:
        return not self.cards

    def shuffle_cards(self) -> None:
        if self.cards:
            random.shuffle(self.cards)

    def add_card_to_top(self, card: Card) -> None:
        if not card:
            raise Exception("Cannot add None to the pile...")
        if not isinstance(card, Card):
            raise TypeError("Can only add Card objects to the pile...")
        self.cards.append(card)

    def get_top_card(self) -> Card:
        if self.is_empty:
            raise Exception("Cannot get top card from an empty pile...")
        return self.cards.pop()

    def get_random_card(self) -> Card:
        if self.is_empty:
            raise Exception("Cannot get a random card from an empty pile...")
        random_idx = random.randint(0, len(self.cards) - 1)
        return self.cards.pop(random_idx)

    def __str__(self) -> str:
        pile_str = ", ".join([card.name for card in self.cards])
        return f"The {self.name} pile is: [{pile_str}]"


if __name__ == "__main__":
    print("create discarded cards pile:")
    discard_pile = Pile("discarded cards")
    print(discard_pile)

    print("create game pile:")
    pile = Pile("game")
    print(pile)

    print("compare two empty piles:")
    assert pile == discard_pile
    print("compared ok")

    print("create pile from string")
    pile = Pile.from_str(seed_str="AKKQQQJJJJ", name="from string")
    print(pile)

    print("shuffle cards in pile")
    pile.shuffle_cards()
    print(pile)

    print("pick card from top of pile")
    top_card = pile.get_top_card()
    print(f"removed top card: {top_card}")
    print(pile)

    print("add picked card to discard pile")
    discard_pile.add_card_to_top(top_card)
    discard_pile.name = "discard pile after adding card to top"
    print(discard_pile)

    print("\nAdd a new card to the top of the pile")
    new_card = Card.Ace
    pile.add_card_to_top(card=new_card)
    print(f"added {new_card} on top:")
    print(pile)

    print("\nRemove a random card from the pile:")
    random_card = pile.get_random_card()
    print(f"removed random card: {random_card}")
    print(pile)

    print("\nAdd removed card to the new pile:")
    discard_pile.add_card_to_top(random_card)
    print("removed cards pile now has:")
    print(discard_pile)

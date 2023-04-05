from __future__ import annotations

import random
from copy import copy
from dataclasses import dataclass, field
from enum import Enum


class Card(Enum):
    Ace = 3
    King = 2
    Queen = 1


STR_TO_CARD = {"A": Card.Ace, "K": Card.King, "Q": Card.Queen}


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

    def shuffle_cards(self) -> None:
        if self.cards:
            new_cards = copy(self.cards)
            random.shuffle(new_cards)
            self.cards = new_cards

    def add_cards_to_top(self, cards_to_add: Card | list[Card]) -> None:
        if not cards_to_add:
            return
        new_cards = copy(self.cards)
        if isinstance(cards_to_add, list):
            new_cards.extend(cards_to_add)
        elif isinstance(cards_to_add, Card):
            new_cards.append(cards_to_add)
        else:
            raise ValueError("Can only add Card objects to the pile")
        self.cards = new_cards

    def get_top_card(self) -> Card:
        if self.cards:
            new_cards = copy(self.cards)
            top_card = new_cards.pop()
            self.cards = new_cards
            return top_card

    def get_random_card(self) -> Card:
        if self.cards:
            new_cards = copy(self.cards)
            random_idx = random.randint(0, len(self.cards) - 1)
            random_card = new_cards.pop(random_idx)
            self.cards = new_cards
            return random_card


if __name__ == "__main__":
    print("create discarded cards pile:")
    discard_pile = Pile(name="discarded cards pile")
    print(discard_pile)

    print("create game pile:")
    pile = Pile(name="game pile")
    print(pile)

    print("compare two empty piles:")
    assert pile == discard_pile
    print("compared ok")

    print("create pile from string")
    pile = Pile.from_str(seed_str="AAKKKQQQ", name="from string")
    print(pile)

    print("shuffle cards in pile")
    pile.shuffle_cards()
    print(pile)

    print("discard card from top of pile")
    top_card = pile.get_top_card()
    print(f"removed top card: {top_card}")
    print(pile)

    print("add removed top card from pile to discarded pile")
    discard_pile.add_cards_to_top(cards_to_add=top_card)
    discard_pile.name = "discarded pile after adding card to top"
    print("discarded pile now has:")
    print(discard_pile)

    print("add a new card to the top of the pile")
    new_card = Card.Ace
    pile.add_cards_to_top(cards_to_add=new_card)
    print(f"added {new_card} on top:")
    print(pile)

    print("remove a random card from the pile")
    random_card = pile.get_random_card()
    print(f"removed random card: {random_card}")
    print(pile)

    print("add removed card to the new pile")
    discard_pile.add_cards_to_top(cards_to_add=random_card)
    print("removed cards pile now has:")
    print(discard_pile)

    print("add multiple cards on top of the pile")
    new_cards = [Card.Ace, Card.Ace]
    pile.add_cards_to_top(cards_to_add=new_cards)
    print(f"added {new_cards} on top:")
    print(pile)

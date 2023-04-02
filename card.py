from __future__ import annotations

import random
from copy import copy
from dataclasses import dataclass, field
from enum import Enum


class Card(Enum):
    ACE = "Ace"
    KING = "King"
    QUEEN = "Queen"
    NO_CARD = ""


CARD_VALUE = {
    Card.ACE: 3,
    Card.KING: 2,
    Card.QUEEN: 1,
    Card.NO_CARD: 0,
}

STR_TO_CARD = {"A": Card.ACE, "K": Card.KING, "Q": Card.QUEEN}


@dataclass
class PileType:
    name: str = field(default=None, compare=False)
    cards: list[Card] = field(default_factory=list)


class Pile(PileType):
    @classmethod
    def from_str(cls, pile_str: str, name: str) -> Pile:
        if not pile_str:
            return cls(cards=[Card.NO_CARD], name=name)
        cards = [STR_TO_CARD[s] for s in pile_str]
        return cls(cards=cards, name=name)

    def shuffle_cards(self) -> None:
        if self.cards:
            new_pile = copy(self.cards)
            random.shuffle(new_pile)
            self.cards = new_pile

    def add_cards_to_top(self, new_cards: Card | list[Card]) -> None:
        if not new_cards:
            return
        new_pile = copy(self.cards)
        if isinstance(new_cards, list):
            new_pile.extend(new_cards)
        elif isinstance(new_cards, Card):
            new_pile.append(new_cards)
        else:
            raise ValueError("Can only add Card objects to the pile")
        self.cards = new_pile

    def get_top_card(self) -> Card:
        if self.cards:
            new_pile = copy(self.cards)
            top_card = new_pile.pop()
            self.cards = new_pile
            return top_card

    def get_random_card(self) -> Card:
        if self.cards:
            new_pile = copy(self.cards)
            random_idx = random.randint(0, len(self.cards) - 1)
            random_card = new_pile.pop(random_idx)
            self.cards = new_pile
            return random_card


if __name__ == "__main__":
    # create empty deck
    empty_pile = Pile(name="empty pile")
    print(empty_pile.cards)

    # compare
    pile = Pile(name="another empty pile")
    assert pile == empty_pile

    # create deck from string
    pile = Pile.from_str(pile_str="AKKQQQ", name="pile created from string")
    print(pile)

    # shuffle deck
    pile.shuffle_cards()
    print("after shuffling once:")
    print(pile)

    # remove top card from deck
    top_card = pile.get_top_card()
    print(f"removed top card: {top_card}")
    print(pile)

    # add removed card(s) to a new pile
    removed_cards_pile = Pile()
    removed_cards_pile.add_cards_to_top(new_cards=top_card)
    print("removed cards pile now has:")
    print(removed_cards_pile)

    # add a new card to the deck
    new_card = Card.ACE
    pile.add_cards_to_top(new_cards=new_card)
    print(f"added {new_card} on top:")
    print(pile)

    # remove a random card from the deck
    random_card = pile.get_random_card()
    print(f"removed random card: {random_card}")
    print(pile)

    # add removed card to the new pile
    removed_cards_pile.add_cards_to_top(new_cards=random_card)
    print("removed cards pile now has:")
    print(removed_cards_pile)

    # add multiple cards on top of the deck
    new_cards = [Card.ACE, Card.ACE]
    pile.add_cards_to_top(new_cards=new_cards)
    print(f"added {new_cards} on top:")
    print(pile)
